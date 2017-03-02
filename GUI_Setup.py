#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
INFO-F106
Can't Stop - Partie 3
Fichier : GUI_Setup.py

Nom : Pierrot
Prénom : Arthur
Matricule : 000422751
"""

import sys
from PyQt4 import QtGui, QtCore


class GUI_Setup(QtGui.QWidget):
    """ Class that handle the graphique side of the game """
    
    def __init__(self, parent=None):
        self.app = QtGui.QApplication(sys.argv)
        super(GUI_Setup, self).__init__(parent)
        self.playerBoxes = []
        self.setup_ui()
        self.show()
    
    def setup_ui(self):
        """ Function performing the initialisation of the players list according to the preferences expressed by the
        user. Returns a list of booleans indicating whether the player is controlled by the computer (True) or not
        (False).
        """
        
        layout = QtGui.QVBoxLayout()
        
        selectPlayersL = QtGui.QLabel(self)
        selectPlayersL.setText('Select Players')
        font = QtGui.QFont()
        font.setPixelSize(40)
        selectPlayersL.setFont(font)
        
        layout.addWidget(selectPlayersL)
        
        for i in range(4):
            self.playerBoxes.append(self.initPlayerBox(i + 1))
            layout.addWidget(self.playerBoxes[-1])
        
        okBTN = QtGui.QPushButton(self)
        okBTN.setText('Ok')
        QtCore.QObject.connect(okBTN, QtCore.SIGNAL('clicked()'), self.app.quit)
        layout.addWidget(okBTN)
        
        self.setLayout(layout)
        self.setWindowTitle('Setup Game')
        self.setWindowIcon(QtGui.QIcon("monk.png"))
        
    @staticmethod
    def initPlayerBox(i):
        """ Create a playerBox with two radioButtons"""
        playerBox = QtGui.QGroupBox('Player ' + str(i))
        
        userRB = QtGui.QRadioButton(playerBox)
        userRB.setIcon(QtGui.QIcon('user.png'))
        userRB.setText('User')
        
        cpuRB = QtGui.QRadioButton(playerBox)
        cpuRB.setIcon(QtGui.QIcon('cpu.png'))
        cpuRB.setText('CPU')
        cpuRB.setChecked(True)
        
        if i > 2:
            playerBox.setCheckable(True)
            playerBox.setChecked(False)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(userRB)
        layout.addWidget(cpuRB)
        
        playerBox.setLayout(layout)
        
        return playerBox

    def getPlayers(self):
        """ Return the list of the players. If the player is an AI, the value is True, else it's False """
        players = []
        for playerBox in self.playerBoxes:
            if not playerBox.isCheckable() or playerBox.isChecked():
                # I look at the second QRadioButton, the cpuRB
                players.append(playerBox.findChildren(QtGui.QRadioButton)[1].isChecked())
        
        return players
