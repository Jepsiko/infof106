#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
INFO-F106
Can't Stop - Partie 3
Fichier : GUI.py

Nom : Pierrot
Prénom : Arthur
Matricule : 000422751
"""

import sys

from PyQt4 import QtGui


class GUI(QtGui.QWidget):
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        super(GUI, self).__init__()
        self.app.exec_()
