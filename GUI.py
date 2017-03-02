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
from PyQt4 import QtGui, QtCore
from Jeu import Jeu


class GUI(QtGui.QWidget):
    """ Class that handle the graphique side of the game """
    
    def __init__(self):
        self.jeu = Jeu()
        self.res_dice = []
        self.dices = []
        self.checkBoxes = []
        self.freeRoutes = 3
        
        self.diceButton = QtGui.QPushButton()
        self.stopButton = QtGui.QPushButton()
        self.goButton = QtGui.QPushButton()
        self.board = QtGui.QPixmap()
        
        self.app = QtGui.QApplication(sys.argv)
        self.app.setStyleSheet("QGroupBox {border: 1px solid gray;}")
        super(GUI, self).__init__()
        
        self.setup_ui()
        
        self.show()
        self.app.exec_()
    
    def setup_ui(self):
        """ Setup the interface """
        
        canevas = QtGui.QLabel(self)
        canevas.setText("Board")

        infoLayout = QtGui.QHBoxLayout()
        infoLayout.addWidget(self.setup_diceBox())
        infoLayout.addWidget(self.setup_turnBox())
        infoLayout.addWidget(self.setup_chooseRouteBox())

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(canevas)
        mainLayout.addLayout(infoLayout)
        self.setLayout(mainLayout)
        self.setWindowTitle("Can't Stop")
        self.setWindowIcon(QtGui.QIcon("monk.png"))
    
    def display_board(self):
        pass
    
    def setup_diceBox(self):
        """ Setup the diceBox """
        diceBox = QtGui.QGroupBox()
        
        layout = QtGui.QGridLayout()
        
        for x in range(4):
            label = QtGui.QLabel(diceBox)
            self.dices.append(label)
            layout.addWidget(label, x % 2, x)
        diceBox.setLayout(layout)
        
        return diceBox
    
    def setup_turnBox(self):
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
        
        self.diceButton = QtGui.QPushButton(turnBox)
        self.diceButton.setIcon(QtGui.QIcon("dice.png"))
        QtCore.QObject.connect(self.diceButton, QtCore.SIGNAL('clicked()'), self.roll_dice)
        
        self.stopButton = QtGui.QPushButton(turnBox)
        self.stopButton.setIcon(QtGui.QIcon("stop.png"))
        
        layoutButton = QtGui.QHBoxLayout()
        layoutButton.addWidget(self.diceButton)
        layoutButton.addWidget(self.stopButton)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(playerTurnL)
        layout.addLayout(layoutButton)
        turnBox.setLayout(layout)
        
        return turnBox
    
    def setup_chooseRouteBox(self):
        """ Setup the chooseRouteBox """
        
        chooseRouteBox = QtGui.QGroupBox()
        
        chooseRouteL = QtGui.QLabel(chooseRouteBox)
        chooseRouteL.setText("Choose route")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPixelSize(20)
        chooseRouteL.setFont(font)
        
        self.goButton = QtGui.QPushButton(chooseRouteBox)
        self.goButton.setIcon(QtGui.QIcon("monk.png"))
        self.goButton.setText("GO!")
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.goButton.setFont(font)
        QtCore.QObject.connect(self.goButton, QtCore.SIGNAL("clicked()"), self.go)
        
        freeL = QtGui.QLabel(chooseRouteBox)
        freeL.setText("Free: " + str(self.freeRoutes))
        
        goFreeLayout = QtGui.QVBoxLayout()
        goFreeLayout.addWidget(self.goButton)
        goFreeLayout.addWidget(freeL)
        
        subLayout = QtGui.QHBoxLayout()
        subLayout.addLayout(self.setup_checkBoxes())
        subLayout.addLayout(goFreeLayout)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(chooseRouteL)
        layout.addLayout(subLayout)
        chooseRouteBox.setLayout(layout)
        
        return chooseRouteBox
    
    def setup_checkBoxes(self):
        """ Setup the checkBoxes with all the radioButtons """
        grid = QtGui.QGridLayout()
        for x in range(2):
            listeCB = []
            for y in range(3):
                checkB = QtGui.QCheckBox()
                listeCB.append(checkB)
                grid.addWidget(checkB, y, x)
            self.checkBoxes.append(listeCB)
                
        return grid
    
    def roll_dice(self):
        """ Roll the dices and update the images and the checkButtons's text"""
        self.res_dice = self.jeu.throw_dice()
            
        combinaisons = self.jeu.get_combinaisons(self.res_dice)
        nbCombi = len(combinaisons)
        
        for i in range(len(self.dices)):
            image = QtGui.QPixmap("dice" + str(self.res_dice[i]) + ".png")
            self.dices[i].setPixmap(image)
        
        for x in range(2):
            for y in range(3):
                if (nbCombi % 2)-1 == 0 == x and y == nbCombi//2 or y < nbCombi//2:
                    self.checkBoxes[x][y].setText(str(combinaisons.pop()))
                    self.checkBoxes[x][y].setCheckable(True)
                else:
                    self.checkBoxes[x][y].setText("")
                    self.checkBoxes[x][y].setCheckable(False)

        self.diceButton.setEnabled(False)
        self.stopButton.setEnabled(False)
        
        if self.jeu.is_blocked(self.res_dice):
            print("bloqué")
        
    def clear_dice(self):
        """ Clear the diceBox """
        for i in range(len(self.dices)):
            self.dices[i].clear()

    def go(self):
        """ Action when we push the Go Button """

        self.diceButton.setEnabled(True)
        self.stopButton.setEnabled(True)
        self.clear_dice()
        self.display_board()
