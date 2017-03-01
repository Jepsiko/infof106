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
    """ Class that handle the graphique side of the game """
    
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        super(GUI, self).__init__()
        self.setup_ui()
        self.show()
        self.app.exec_()
    
    def setup_ui(self):
        """ Setup the interface """
        
        canevas = QtGui.QLabel(self)
        canevas.setText("Board")
               
        diceBox = QtGui.QGroupBox()

        infoLayout = QtGui.QHBoxLayout()
        infoLayout.addWidget(diceBox)
        infoLayout.addWidget(self.setup_turnBox())
        infoLayout.addWidget(self.setup_chooseRouteBox())

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(canevas)
        mainLayout.addLayout(infoLayout)
        self.setLayout(mainLayout)
    
    def display_board(self):
        pass
    
    @staticmethod
    def setup_turnBox():
        """ Setup the TurnBox """
        turnBox = QtGui.QGroupBox()
        
        playerTurnL = QtGui.QLabel(turnBox)
        playerTurnL.setText("Yellow's Turn")
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setPixelSize(20)
        playerTurnL.setFont(font)
        
        rollDiceB = QtGui.QPushButton(turnBox)
        rollDiceB.setIcon(QtGui.QIcon("dice.png"))
        
        stopB = QtGui.QPushButton(turnBox)
        stopB.setIcon(QtGui.QIcon("stop.png"))
        
        layoutButton = QtGui.QHBoxLayout()
        layoutButton.addWidget(rollDiceB)
        layoutButton.addWidget(stopB)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(playerTurnL)
        layout.addLayout(layoutButton)
        turnBox.setLayout(layout)
        
        return turnBox
    
    @staticmethod
    def setup_chooseRouteBox():
        """ Setup the chooseRouteBox """
        
        chooseRouteBox = QtGui.QGroupBox()
        
        chooseRouteL = QtGui.QLabel(chooseRouteBox)
        chooseRouteL.setText("Choose route")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        chooseRouteL.setFont(font)
        
        # TODO : Setup the radioBoxes, the button GO and the label Free
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(chooseRouteL)
        chooseRouteBox.setLayout(layout)
        
        return chooseRouteBox
