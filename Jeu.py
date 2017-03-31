# -*- coding: utf-8 -*-
"""
THIS FILE CONTAINS THE CLASS JEU
"""

from Gui import *
from Joueur import *
import _thread
import time

__author__ = "Luciano Porretta"
__copyright__ = "Copyright 2017, Luciano Porretta"
__credits__ = ["Luciano Porretta "]
__license__ = "ULB Theaching License"
__version__ = "1.0"
__maintainer__ = "Luciano Porretta"
__email__ = "luciano.porretta@ulb.ac.be"
__status__ = "Beta"


class Jeu(object):
    def __init__(self, ui):
        self.n_players = None
        self.end_game = False
        self.winning_player = None
        self._active_players = None
        self.players = {}
        self._colors = {1: 'Red', 2: 'Green', 3: 'Blue', 4: 'Yellow'}
        self._round = 0
        self._game_won = None
        
        self._ui = ui
        self._ui.RollButton.clicked.connect(self.RollButtonHandler)
        self._ui.StopButton.clicked.connect(self.StopButtonHandler)
        self._ui.GoButton.clicked.connect(self.GoButtonHandler)
    
    def wait_end_round(self, n):
        """This method refresh the Main Windows catching all the events""
        Parameters
        ----------
        n : int
        """
        while not self.players[n]._end_round:
            QtGui.qApp.processEvents()
            time.sleep(0.05)
    
    def select_players(self):
        """This method extract the players selection from the Setup Frame"""
        self.n_players, self._active_players = Gui.extract_radio(self._ui)
        print("# of players: ", self.n_players, "vector for AI: ", self._active_players)
    
    def create_players(self):
        """This method create the players instances"""
        count = 0
        for i in range(4):
            if self._active_players[i] == 'Active':
                count += 1
                self.players[count] = Joueur(count, False, self._colors[i + 1], self._ui)
            elif self._active_players[i] == 'CPU':
                count += 1
                self.players[count] = Joueur(count, True, self._colors[i + 1], self._ui)
        
        for i in self.players:
            print("Giocatore {}: id={} Color={} AI={}".format(i, self.players[i]._id, self.players[i]._color,
                                                              self.players[i].isAI))
        return count
    
    def get_other_players(self, _id):
        """
        Return a list of the other players's id
        
        Parameters
        ----------
        _id : int
        
        Return
        ----------
        list
        """
        
        other_players = []
        for i in range(1, len(self.players)+1):
            if self.players[i].get_id() != _id:
                other_players.append(self.players[i])
        return other_players
    
    def checkBox1Handler(self):
        """This method handle the events of the checkbox 1"""
        self.players[self._round]._mutex_box(1)
    
    def checkBox2Handler(self):
        """This method handle the events of the checkbox 2"""
        self.players[self._round]._mutex_box(2)
    
    def checkBox3Handler(self):
        """This method handle the events of the checkbox 3"""
        self.players[self._round]._mutex_box(3)
    
    def checkBox4Handler(self):
        """This method handle the events of the checkbox 4"""
        self.players[self._round]._mutex_box(4)
    
    def checkBox5Handler(self):
        """This method handle the events of the checkbox 5"""
        self.players[self._round]._mutex_box(5)
    
    def checkBox6Handler(self):
        """This method handle the events of the checkbox 6"""
        self.players[self._round]._mutex_box(6)
    
    def RollButtonHandler(self):
        """This method handle the events of Roll button"""
        self.players[self._round].throw_dices()
    
    def StopButtonHandler(self):
        """This method handle the events of Stop button"""
        self.players[self._round].stop_round()
    
    def GoButtonHandler(self):
        """This method handle the events of GO button"""
        self.players[self._round].choose_route()
    
    def check_top(self, player):
        """This method checks the end of the game""
        Parameters
        ----------
        player : int
        """
        self.end_game, self.winning_player = self.players[player].there_is_a_winner()
    
    def board_setup(self, player):
        """This method refresh setup the board with default values
        Parameters
        ----------
        n : int
        """
        self._ui.RollButton.setDisabled(False)
        self._ui.StopButton.setDisabled(True)
        self._ui.GoButton.setDisabled(True)
        self._ui.set_Command_Title(self.players[player]._color)
        self._ui.set_Free_Bonzos("3")  # UPDATE THE LEFT BONZOS
        self._ui.checkBox[1].stateChanged.connect(self.checkBox1Handler)
        self._ui.checkBox[2].stateChanged.connect(self.checkBox2Handler)
        self._ui.checkBox[3].stateChanged.connect(self.checkBox3Handler)
        self._ui.checkBox[4].stateChanged.connect(self.checkBox4Handler)
        self._ui.checkBox[5].stateChanged.connect(self.checkBox5Handler)
        self._ui.checkBox[6].stateChanged.connect(self.checkBox6Handler)
        for i in range(1, 7):
            self._ui.checkBox[i].setEnabled(True)
            self._ui.checkBox[i].setChecked(False)
    
    def play_round(self):
        """This method manage the rounds"""
        self._game_won = False
        self._round = (self._round % self.n_players) + 1  # SELECTE ROUND PLAYER
        # print("Round: ", self._round)
        self.board_setup(self._round)  # SETUP BOARD
        playerOn = self.players[self._round]
        playerOn._end_round = False
        if playerOn.isAI:  # IF PLAYER AI
            playerOn.AI(self)
        else:  # IF PLAYER NOT AI
            self.wait_end_round(self._round)
        self.check_top(self._round)
        return self.winning_player
    
    def reset_bonzes(bonzes):
        """ Empties the bonzes dictionary."""
        bonzes.clear()
