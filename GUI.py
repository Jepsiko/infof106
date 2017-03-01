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

    def initPlayerBox(self, i):
        playerBox = QtGui.QGroupBox('Player ' + str(i))
    
        userCB = QtGui.QRadioButton(playerBox)
        userCB.setIcon(QtGui.QIcon('user.png'))
        userCB.setText('User')
    
        cpuCB = QtGui.QRadioButton(playerBox)
        cpuCB.setIcon(QtGui.QIcon('cpu.png'))
        cpuCB.setText('CPU')
        cpuCB.setChecked(True)
    
        if i > 2:
            playerBox.setCheckable(True)
            playerBox.setChecked(False)
    
        layout = QtGui.QHBoxLayout()
        layout.addWidget(userCB)
        layout.addWidget(cpuCB)
    
        playerBox.setLayout(layout)
    
        return playerBox

    def setup_players(self):
    
        selectPlayersL = QtGui.QLabel(self)
        selectPlayersL.setText('Select Players')
        font = QtGui.QFont()
        font.setPixelSize(40)
        selectPlayersL.setFont(font)
    
        layout = QtGui.QVBoxLayout()
        layout.addWidget(selectPlayersL)
    
        playerBoxes = []
    
        for i in range(4):
            playerBoxes.append(self.initPlayerBox(i + 1))
            layout.addWidget(playerBoxes[-1])
    
        okBTN = QtGui.QPushButton(self)
        okBTN.setText('Ok')
        QtCore.QObject.connect(okBTN, QtCore.SIGNAL('clicked()'), self.app.quit)
        layout.addWidget(okBTN)
    
        self.setLayout(layout)
        self.setWindowTitle('Setup Game')
        self.show()
        self.app.exec_()
    
        players = []
        for playerBox in playerBoxes:
            if not playerBox.isCheckable() or playerBox.isChecked():
                players.append(playerBox.findChildren(QtGui.QRadioButton)[1].isChecked())
    
        return players