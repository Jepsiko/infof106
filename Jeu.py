#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
INFO-F106
Can't Stop - Partie 3
Fichier : Jeu.py

Nom : Pierrot
Prénom : Arthur
Matricule : 000422751
"""

from GUI import GUI
import itertools
import random
import os
import time


class Jeu:
    """Class that handle the whole game"""
    
    def __init__(self):
        """ Initialisation of all the variables needed for the game.
    
        Keywords arguments:
        n_pawns -- Integer representing the number of players
        """
        
        self.HEIGHT = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}  # voie_id : h_max
        self.MIN_DICE = 1
        self.MAX_DICE = 6
        self.N_DICE = 4
        self.N_BONZES = 3
        self.MAX_HEIGHT = max(self.HEIGHT.values())
        self.PAWNS_COLORS = {
            0: 31,  # Red
            1: 32,  # Green
            2: 33,  # Yellow
            3: 34  # Blue
        }
        
        self.SYMBOLS = {
            "bonze": "O",  # Bonze symbol
            "pawn": "I",  # Pawn symbol - Alternative chr(9873)
            "invalid": "X",  # Invalid cell symbol
            "empty": " "
        }
        
        self.P = 0.5
        self.CSI = "\x1B["
        self.OFFSET = 2  # To account for the fact that the game board is indexed from 2 onwards
        
        self.gui = GUI()
        self.bonzes = {}
        self.players = self.gui.setup_players()
        self.pawns = [{} for _ in range(len(self.players))]
        self.blocked_routes = set()
        
        # Set a given seed for repeatability
        random.seed(17)

    # Section 2.2.2 - Affichage en couleur

    def print_color(self, color, text, sep):
        """ Prints colored text

        Keyword arguments:
        color -- Integer representing the ANSI code of the color
        text -- String to be colored
        sep -- Separator to be used at the end of the string
        """
        print(self.CSI + str(color) + "m" + text + self.CSI + "0m", end=sep)

    # Section 2.2.3 - Remaniement fonctions
    def check_top(self, player_pawns):
        """ Check if three pawns/bonzes have reached simultaneously the top of the corresponding routes.

        Keyword arguments:
            bonzes -- Dictionary representing the pawns/bonzes
        """
        pawns_on_top = 0
        if len(player_pawns) < 3:
            return False
        else:
            for route in player_pawns:
                if player_pawns[route] == self.HEIGHT[route]:
                    pawns_on_top += 1
    
            if pawns_on_top >= 3:
                return True
            else:
                return False

    def game_round(self, current_player):
        """ Implementation of a game round.

        Keyword arguments:
        pawns -- Dictionary representing the pawns
        bonzes -- Dictionary representing the bonzes
        blocked_routes -- Set representing the blocked ways
        current_player -- Integer id of the current player
        AI -- Boolean indicating whether the player is controlled by the AI or not
        """

        self.reset_bonzes()
        self.display_board(self.pawns, self.bonzes)
        stop_round = False
        game_won = False
        AI = self.players[current_player]
        
        while not stop_round:
            if self.move_bonzes(self.choose_dice(self.throw_dice(), current_player, AI), self.pawns,
                                self.bonzes, self.blocked_routes, current_player, AI):
                if self.check_top(self.pawns[current_player]):
                    stop_round = True
                    game_won = True
                    print("Vous avez gagné !")
                    self.display_board(self.pawns, self.bonzes)
        
                if not game_won:
                    stop_round = self.decide_stop(AI)
        
                if stop_round:
                    self.save_pawns(self.bonzes, self.pawns, self.blocked_routes, current_player)
    
            else:
                print("Vous êtes bloqué !")
                stop_round = True

        return game_won

    def move_bonzes(self, chosen_routes, pawns, bonzes, blocked_routes, player_id, AI):
        """ Implementation of the business logic to move bonzes.

        Keyword arguments:
        chosen_routes -- 2-tuple containing the chosen routes
        pawns -- Dictionary representing the pawns
            bonzes -- Dictionary representing the bonzes
        blocked_routes -- Set representing the blocked ways
        current_player -- Integer id of the current player
        AI -- Boolean indicating whether the player is controlled by the AI or not
        """

        successful_dice_throw = False
        routes_with_bonzes = []
        routes_to_place_bonzes = []
        # Count the number of available bonzes
        available_bonzes = self.N_BONZES - len(bonzes)

        # Check selected routes
        for route in chosen_routes:
            # Whether a bonze is present...
            if route in bonzes:
                routes_with_bonzes.append(route)
            # ... or not
            else:
                if not (route in blocked_routes):
                    routes_to_place_bonzes.append(route)

        # Move bonzes that are already present
        for route in routes_with_bonzes:
            if bonzes[route] < self.HEIGHT[route]:
                jump = 1
                # If there are other players pawns, jump above them
                while self.exists_pawn(route, bonzes[route] + jump, player_id):
                    jump += 1
            
                    # If the top is reached stop at the top
                if (bonzes[route] + jump) > self.HEIGHT[route]:
                    bonzes[route] = self.HEIGHT[route]
                else:
                    bonzes[route] += jump
        
                successful_dice_throw = True

        # Place bonzes
        if len(routes_to_place_bonzes) >= 2:  # If there are 2 routes available
            if available_bonzes >= 2:  # And 2 or more bonzes to place
                for route in routes_to_place_bonzes:  # Place both of them
                    available_bonzes = self.place_bonze(route, pawns, bonzes, available_bonzes, player_id)
                    successful_dice_throw = True
            else:
                # Otherwise, if there is only a single available bonze but multiple available ways
                # let the player choose where to place it
                if available_bonzes == 1:
                    if not AI:
                        chosen_route = self.choose_route_human(routes_to_place_bonzes)
                    else:
                        chosen_route = self.choose_route_AI(routes_to_place_bonzes)

                    self.place_bonze(chosen_route, pawns, bonzes, available_bonzes, player_id)
                    successful_dice_throw = True

        else:
            if len(routes_to_place_bonzes) == 1:
                # If there is a single route available
                if available_bonzes >= 1:  # And at least one available bonze
                    self.place_bonze(routes_to_place_bonzes[0], pawns, bonzes, available_bonzes, player_id)
                    successful_dice_throw = True

        return successful_dice_throw

    def place_bonze(self, route, pawns, bonzes, available_bonzes, player_id):
        """ Place a bonze in the selected route, skipping pawns if necessary.

        Keywords arguments
        route -- Integer representing the target route
        pawns -- Dictionary representing the pawns
        bonzes -- Dictionary representing the bonzes
        available_bonzes -- Integer representing the number of available bonzes
        """
        # If there is already a pawn of the player in the chosen route, put the bonze
        # after the pawn
        offset = -1
        if route in pawns[player_id]:
            # If the top is reached then stop at the top
            if (pawns[player_id].get(route) + 1) > self.HEIGHT[route]:
                bonzes[route] = self.HEIGHT[route]
            else:
                bonzes[route] = pawns[player_id].get(route)
                offset = bonzes[route]
        else:
            offset = 1

        # If there are other players pawns, jump above them
        while self.exists_pawn(route, offset, player_id):
            offset += 1
        bonzes[route] = offset

        return available_bonzes - 1

    # Section 2.2.3 - Autres fonctions

    # noinspection PyTypeChecker
    def choose_dice_human(self, res_dice, player_id):
        """ Choice of the pair of dice that should be chosen to advance the bonzes - Human Version

        Keywords arguments:
        res_dice -- 4-tuple containing the result of the 4-dice throw
        player_id -- Integer id of the current player
        """
        dice_index_selected = None

        while dice_index_selected is None:
            self.print_color(self.PAWNS_COLORS[player_id], "[Joueur {0}]".format(player_id + 1), " ")
            selection_string = input(
                "Choisir les indices des premières deux dés -> {1} : ".format(player_id + 1, res_dice))
            dice_index_selected = self.select_dice_verification(selection_string)

        dice_index_not_selected = [i for i in range(self.N_DICE) if i not in dice_index_selected]

        return tuple(
            (sum([res_dice[x] for x in dice_index_selected]), sum([res_dice[x] for x in dice_index_not_selected])))

    @staticmethod
    def choose_route_human(available_routes):
        """ Implementation of the random choice among different available routes. - Human version

        Keywords arguments:
        available_routes -- 2-tuple containing the routes among which the route should be chosen
        """
        valid_input = False
        chosen_route = -1

        while not valid_input:
            selection_string = input(
                "Voies disponibles: {0} - Saisir l'indice (0-1) de la voie à utiliser : ".format(available_routes))
            if len(selection_string) == 1 and selection_string.isdigit():
                try:
                    chosen_route = int(selection_string)
                except ValueError:
                    print("Erreur de conversion en entier - choix des voies. Réessayer, svp.")
                    time.sleep(1)
        
                if 0 <= chosen_route <= 1:
                    valid_input = True
                else:
                    print("Veuillez saisir un numero compris entre 0 et 2. Réessayer, svp.")
                    time.sleep(1)
            else:
                print("Mauvais encodage du numero des joueurs. Réessayer, svp.")
                time.sleep(1)

        return available_routes[chosen_route]

    @staticmethod
    def decide_stop_human():
        """ Implementation of the decision whether to stop or not at the end of a game round - Human version
        """
        valid_input = False
        stop = False

        while not valid_input:
            selection_string = input("Voulez-vous (C)ontinuer ou (A)rrêter? ")
            # The player decides to continue
            if selection_string == "C":
                print("On continue!")
                stop = False
                valid_input = True
            # The player decides to stop
            elif selection_string == "A":
                print("Vous vous arrêtez !")
                stop = True
                valid_input = True
            else:
                print("Option non permise. Réessayer, svp.")

        return stop

    @staticmethod
    def is_blocked(res_dice, blocked_routes, bonzes):
        """ Check whether a player is blocked or not.

        Keywords arguments:
        res_dice -- 4-tuple containing the result of the 4-dice throw
        blocked_routes -- Set representing the blocked ways
        bonzes -- Dictionary representing the bonzes
        """

        available_routes = {i for i in range(2, 13)}.difference(blocked_routes)
        possible_routes = {sum(i) for i in itertools.combinations(res_dice, 2)}
        bonze_routes = {key for key in bonzes}
        return len(possible_routes.intersection(bonze_routes).intersection(available_routes)) == 0

    # Section 2.2.4 - AI

    def choose_dice_AI(self, res_dice, player_id):
        """ Choice of the pair of dice that should be chosen to advance the bonzes - AI Version

        Keywords arguments:
        res_dice -- 4-tuple containing the result of the 4-dice throw
        player_id -- Integer id of the current player
        """
        self.print_color(self.PAWNS_COLORS[player_id], "[Joueur {0}]".format(player_id + 1), " ")
        "En train de choisir les indices des premières deux dés -> {1} : ".format(player_id + 1, res_dice)
        time.sleep(1)
        shuffled_dices = list(res_dice)
        random.shuffle(shuffled_dices)
        return tuple((sum(shuffled_dices[:(self.N_DICE // 2)]), sum(shuffled_dices[(self.N_DICE // 2):])))

    @staticmethod
    def choose_route_AI(available_routes):
        """ Implementation of the random choice among different available routes. - AI version

        Keywords arguments:
        available_routes -- 2-tuple containing the chosen routes
        """
        return random.choice(available_routes)

    def decide_stop_AI(self):
        """ Implementation of the random decision between stopping the game round or continuing it. - AI version.
        """
        return False if random.random() < self.P else True

    # Fonctions Partie 1

    def reset_bonzes(self):
        """ Empties the bonzes dictionary.

        Keywords arguments:
        bonzes -- Dictionary representing the bonzes
        """
        self.bonzes.clear()

    def throw_dice(self):
        """ Simulate a 4-dice throw. """
        return tuple(random.randint(self.MIN_DICE, self.MAX_DICE) for _ in range(self.N_DICE))

    # Auxiliary functions

    def clean_route(self, route, player_id):
        """ Clean a route (remove all the pawns) once one pawn has reached the top and blocked it.

        Keywords arguments:
        route -- Integer representing the route to block
        pawns -- Dictionary representing the pawns
        player_id -- Integer id of the current player
        """
        # Remove all the pawns that are in a blocked route
        for i in range(len(self.pawns)):
            if i != player_id and self.pawns[i].get(route):
                del self.pawns[i][route]

    def exists_pawn(self, route, height, player_id):
        """ Verify whether a pawn exists in a given position of the game board.

        Keywords arguments:
        route -- Integer representing the route to verify
        height -- Integer represnting the height to verify
        pawns -- Dictionary representing the pawns
        """
        # Check if there is a pawn in the route "route" at height "height"
        for i in range(len(self.pawns)):
            if self.pawns[i].get(route) == height and i != player_id:
                return True
        return False

    def save_pawns(self, bonzes, pawns, blocked_routes, current_player):
        """ Function to replace the bonzes with the current player's pawns once his turn has ended.

        Keywords arguments:
        bonzes -- Dictionary representing the bonzes
        pawns -- Dictionary representing the pawns
        current_player -- Integer id of the current player
        """
        # Merge pawns and bonzes
        if not pawns[current_player]:
            pawns[current_player] = bonzes.copy()
        else:
            pawns[current_player].update(bonzes)

        # pawns[current_player] = {**pawns[current_player], **bonzes}

        for route in pawns[current_player]:
            # If one of the pawn reaches the top, then block the route and clean the route
            if pawns[current_player][route] == self.HEIGHT[route]:
                blocked_routes.add(route)
                self.clean_route(route, current_player)

                self.reset_bonzes()

    def choose_dice(self, res_dice, current_player, AI):
        """ Wrapper function for the homonym functions for AI and human players.

        Keyword arguments:
        res_dice -- 4-tuple containing the result of the thrown dice
        current_player -- Integer id of the current player
        AI -- Boolean indicating whether the player is controlled by the AI or not
        """
        return self.choose_dice_AI(res_dice, current_player) if AI else self.choose_dice_human(res_dice, current_player)

    def decide_stop(self, AI):
        """ Wrapper function for the homonym functions for AI and human players.c
        Keyword arguments:
        AI -- Boolean indicating whether the player is controlled by the AI or not
        """
        return self.decide_stop_AI() if AI else self.decide_stop_human()

    @staticmethod
    def print_logo():
        """ Prints a fancy logo for the application. """

        print("   +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+")
        print("  ~~~~:::::::::::::::::::::::::::::~~~~")
        print("  ~~:::::::::::::::::::::::::::::::::::~~")
        print("  ~:::::::::::::::::::::::::::::::::::::~=")
        print("  ~::::::::::,::,:,::::,:::,:,::::::::::~=")
        print("  :::~==++~,,,===,,,===,,==,=  =======:::=")
        print("  ::=       ,=7   ,,=    =  : ,        ::=")
        print("  :~=   ,,,,,=     ,=       ,,,,=    ::::=")
        print("  ::I   ,,,,=  7   ,=       ,,,,=    ::::=")
        print("  :::   ===:=       =  ,    ,,,,=    ,:::~")
        print("  ,,:,,    ,  ,,,   ,  ,,,  ,,,,,    ,:,,~")
        print("  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,~")
        print("  ,,,,~~~~,~~~~~~~~~,,,,::,,,,~~~~~~,,,,,~")
        print("  ,,=      =         ==      ,=       I,,~")
        print("  ,,I    ,,,,,=    ,==   ,=   =    ,+  ,,~")
        print("  ,,=     ,,,,=    ,=    ,=        =+  ,,~")
        print("  ,,,,     ,,,=    ,=    ,=           ,,,=")
        print("  ,,===    ,,,=    ,,=   ==   =    ,,,,,,=")
        print("  :,,     ,,,,,    ,,,,      ,,    ,,,,,:=")
        print("  :,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:=")
        print("  ::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,::=")
        print("  :::,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:::")
        print("  :::::,,,,,,,,,,,,,,,,,,,,,,,,,,,:::::")
        print("   =:::::::::::::::::::::::::::::::::=")
        print("     +===========================+")

    # noinspection PyTypeChecker
    def display_board(self, pawns, bonzes):
        """ Print the game board.

        Keyword arguments:
        pawns -- Dictionary representing the pawns
            bonzes -- Dictionary representing the bonzes
        """
        # Initialize board
        board = [[self.SYMBOLS["invalid"] for _ in range(len(self.HEIGHT.keys()))] for _ in range(self.MAX_HEIGHT + 1)]

        # os.system('cls' if os.name == 'nt' else 'clear')
        # print_logo()
        print()

        # Set the empty cells as empty
        for v in self.HEIGHT:
            for h in range(self.HEIGHT[v] + 1):
                board[h][v - self.OFFSET] = []

        # Put the bonzes in the proper positions
        for b in bonzes:
            board[bonzes[b]][b - self.OFFSET] = self.SYMBOLS["bonze"]

        # Put the pawns in the proper positions
        for pawns_player in pawns:
            for p in pawns_player:
                board[pawns_player[p]][p - self.OFFSET] = self.SYMBOLS["pawn"]

        # Print the board in reversed order as required
        for i in reversed(range(1, self.MAX_HEIGHT + 1)):
            print(str(i), end="\t")
            for j in range(len(self.HEIGHT.keys())):
                for symbol in board[i][j]:
                    if symbol == self.SYMBOLS["pawn"]:
                        for k in range(len(pawns)):
                            if pawns[k].get(j + self.OFFSET) == i:
                                # Avoid raising KeyError exception returning a default -1
                                self.print_color(self.PAWNS_COLORS[k], str(symbol), "")
                    else:
                        print(str(symbol), end="")
                print("\t", end="")
            print("")
        print("\t", end="")
        for v in self.HEIGHT:
            if v < 10:
                print(str(v), end="\t")
            else:
                print(str(v), end="\t")
        print("\n")

        return None

    def select_dice_verification(self, selection_string):
        """ Verification of the input string, checking that the string has the correct length, does not contains
        duplicates, nor non-numeric characters. Return a list of tuple (row_index,col_index= with one element for every
        card encoded by the user.
        """
        dice_index_selected = []

        # Verify that the input string has exactly 3 characters: 2 numbers + 1 spaces
        if len(selection_string) != 3:
            print("Mauvais encodage des des. Réessayer, svp.")
            return None

        selection_list = selection_string.split(" ")

        # Verify that splitting the string according to the spaces yields to two elements
        if len(selection_list) != 2:
            print("Mauvais encodage des des. Réessayer, svp.")
            return None

        # Verify the absence of duplicates in the list.
        if len(selection_list) != len(set(selection_list)):
            print("Presence des des dupliqueés. Réessayer, svp.")
            return None

        # Verify that every token after the split of the list is correctly encoded
        for die_str in selection_list:
            index = self.select_die_verification(die_str)
            if index is None:
                return None
            dice_index_selected.append(index)

        return dice_index_selected

    def select_die_verification(self, die_str):
        """ Verification of the input string, checking that the string has the correct length, does not contains
        duplicates, nor non-numeric characters. Return a list of tuple (row_index,col_index= with one element for
        every card encoded by the user.
        """
        # Verify that a token is exactly two characters long, and then try to parse every element as an integer
        if len(die_str) == 1:
            try:
                # Python indexes : 0 ... n-1
                index = int(die_str[0]) - 1
            except ValueError:
                print("Erreur de conversion en entier, index ligne. Réessayer, svp.")
                return None

        else:
            print("Mauvais encodage du dé. Réessayer, svp.")
            return None

        if index < 0 or index > self.N_DICE:
            print("Indice du dé incorrect. Réessayer,svp")
            return None

        return index

    def select_player_number_verification(self):
        """ Verification of the input string for the choice of the number of players. """
        valid_input = False
        n_players = -1

        while not valid_input:
            # Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_logo()
            selection_string = input("\nVeuillez entrer le nombre des joueurs [2-4] : ")
    
            if len(selection_string) == 1 and selection_string.isdigit():
                try:
                    n_players = int(selection_string)
                except ValueError:
                    print("Erreur de conversion en entier - numéro des joueurs. Réessayer, svp.")
                    time.sleep(1)
                if 2 <= n_players <= 4:
                    valid_input = True
                else:
                    print("Veuillez entrer un numero compris entre 2 et 4. Réessayer, svp.")
                    time.sleep(1)
            else:
                print("Mauvais encodage du numero des joueurs. Réessayer, svp.")
                time.sleep(1)

        return n_players

    def select_player_type_verification(self, index):
        """ Verification of the input string for the choice of the player. """
        valid_input = False
        player_AI = False

        while not valid_input:
            # Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_logo()
            selection_string = input(
                "\nVeuillez choisir le type du joueur {0} [(H)umain/(A)I] : ".format(index + 1))
            if selection_string == "H":
                player_AI = False
                valid_input = True
            elif selection_string == "A":
                player_AI = True
                valid_input = True
            else:
                print("Mauvais encodage du type des joueurs. Réessayer, svp.")
                time.sleep(1)

        return player_AI

    def print_winning_message(self, winning_player):
        """ Print the winning message for the player that won the game.

        Keyword arguments:
        winning_player - Integer id of the winning player
        """
        print("Bravo ", end="")
        self.print_color(self.PAWNS_COLORS[winning_player], "Joueur {0}".format(winning_player + 1), "")
        print("!", end="")
