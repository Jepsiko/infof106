#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
INFO-F106
Can't Stop - Partie 3
Fichier : Joueur.py

Nom : Pierrot
Prénom : Arthur
Matricule : 000422751
"""


class Joueur:
    """ Class that represent a player """
    
    def __init__(self, ID, AI):
        self.ID = ID
        self.AI = AI
        
    def getID(self):
        """ Return the ID of the player """
        return self.ID
    
    def isAI(self):
        """ Return True is the player is an AI """
        return self.AI
    
    def __str__(self):
        return ("Computer " if self.isAI() else "Player ") + str(self.getID())
