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