# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
THIS FILE CONTAINS THE MAIN LOOP OF THE GAME

Nom : Pierrot
Prénom : Arthur
Matricule : 000422751
Année d'étude : BA2-INFO
INFO-F106 - Partie 4
"""
import sys
from PyQt4 import QtCore, QtGui
from Gui import *
from Jeu import *
from Joueur import *

__author__ = "Luciano Porretta"
__copyright__ = "Copyright 2017, Luciano Porretta"
__credits__ = ["Luciano Porretta "]
__license__ = "ULB Theaching License"
__version__ = "1.0"
__maintainer__ = "Luciano Porretta"
__email__ = "luciano.porretta@ulb.ac.be"
__status__ = "Beta"

if __name__ == "__main__":
    try:
        app = QtGui.QApplication(sys.argv)  # CREATE THE APPLICATION
        Main = QtGui.QMainWindow()  # CREATE MAIN WINDOW
        Setup = QtGui.QDialog()  # CREATE DIALOG
        uiMain = Gui()  # CREATE AN INSTANCE OF GUI
        uiMain.MainUi(Main)  # INIT MAIN WINDOW
        uiMain.SelectUi(Setup)  # INT DIALOG
        Game = Jeu(uiMain)  # CREATE AN INSTANCE OF GUI
        uiMain.ok_button.clicked.connect(lambda: Game.select_players())  # CONNECT DIALOG OK BUTTON WITH GAME FUNCITON
        Setup.exec_()  # SHOW DIALOG WITHOUT AND WAIT TO BE DONE
        n_players = Game.create_players()
        # print(n_players, " player are created")   # DEBUG PRINT
        Main.show()  # SHOW MAIN WINDOW
        winner = None  # DECLARE WINNER VARIABLE
        while not Game.end_game:  # WAIT THE GAME TO END
            # Game round - Main function
            winner = Game.play_round()  # PLAY ROUNG
        # SETUP END GAME MESSAGE
        the_end = QtGui.QWidget()
        QtGui.QMessageBox.information(the_end, "End Game", "The player {} won!!!".format(winner), 0)
        sys.exit(app.exec_())
    except Exception as error:
        """ THIS EXEPTION CATCH ALL THE ERRORS AND DISPLAY THEM IN A WARNING MESSAGE"""
        error = QtGui.QWidget()
        QtGui.QMessageBox.warning(error, "Error", "{}".format(repr(error)))
        error.show()
