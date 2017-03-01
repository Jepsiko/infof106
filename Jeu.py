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
import cantstopFunctions


class Jeu:
    """Classe qui gère le jeu complet"""
    
    def __init__(self):
        """
        Initialise les attributs HEIGHT, P, bonzes, players, pawns et blocked_routes
        """
        
        self.HEIGHT = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
        self.P = 40  # Probabilité en pourcentage
        
        self.gui = GUI()
        self.bonzes = {}
        self.players = self.gui.setup_players()
        self.pawns = [{} for _ in range(len(self.players))]
        self.blocked_routes = set()
        
        # Partie du prof
        winning_player = -1
        current_player = 0
        
        bonzes, pawns, blocked_ways = self.gui.init(len(self.players))
        end_game = False
        
        while not end_game:
            # If the current players has already used some pawns, then reload his position
            # if pawns[current_player]:
            #    bonzes = pawns[current_player].copy()
            
            # Display game board
            # cantstopFunctions.display_board(pawns,bonzes)
            
            end_game = cantstopFunctions.game_round(pawns, bonzes, blocked_ways, current_player,
                                                    self.players[current_player])
            
            # If a player has won the game, pick it as the game winner
            if end_game:
                winning_player = current_player
            
            # Move to the next player
            current_player = (current_player + 1) % len(self.players)
        
        # Show informations about the winning player
        cantstopFunctions.print_winning_message(winning_player)
