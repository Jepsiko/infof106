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
        return self.ID
    
    def isAI(self):
        return self.AI
