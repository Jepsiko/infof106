#!/usr/bin/env python
# −∗− coding: utf−8 −∗−

"""
INFO-F106
Can't Stop - Partie 3
Fichier : cantstop.py

Nom : Pierrot
Prénom : Arthur
Matricule : 000422751
"""

from GUI import GUI

if __name__ == "__main__":
    
    gui = GUI()
    """
    n_players = jeu.get_n_players()
    
    winning_player = -1
    current_player = 0
    end_game = False
    
    while not end_game:
        # If the current players has already used some pawns, then reload his position
        # if pawns[current_player]:
        #    bonzes = pawns[current_player].copy()
        
        # Display game board
        # cantstopFunctions.display_board(pawns,bonzes)
        
        end_game = jeu.game_round(current_player)
        
        # If a player has won the game, pick it as the game winner
        if end_game:
            winning_player = current_player
        
        # Move to the next player
        current_player = (current_player + 1) % n_players
    
    # Show informations about the winning player
    jeu.print_winning_message(winning_player)
"""
