# -*- coding: utf-8 -*-
"""
THIS FILE CONTAINS THE CLASS JOUEUR

Nom : Pierrot
Prénom : Arthur
Matricule : 000422751
Année d'étude : BA2-INFO
INFO-F106 - Partie 4
"""
import random, time, copy
from Gui import *
from Jeu import *
from PyQt4 import QtCore, QtGui
import time

__author__ = "Luciano Porretta"
__copyright__ = "Copyright 2017, Luciano Porretta"
__credits__ = ["Luciano Porretta "]
__license__ = "ULB Theaching License"
__version__ = "1.0"
__maintainer__ = "Luciano Porretta"
__email__ = "luciano.porretta@ulb.ac.be"
__status__ = "Beta"

MIN_DICE = 1
MAX_DICE = 6
N_DICE = 4
HEIGHT = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
BLOCKED = []
BOARD = {}
PAUSE = 0.5
AI_MSG = 0.5  # SPEED (FAST: 0.5, NORMAL: 2.5)
AI_MAX_STEPS = 10
ALPHA = 1  # Ponderation of the score with jump
BETA = 10  # Ponderation of the score with distance


class Joueur(object):
    def __init__(self, id, ai, color, ui, difficulty=0):
        self._id = id
        self._color = color
        self._pawns = {}
        self._bonzes = {}
        self._max_bonzes = 3
        self.isAI = ai
        self.difficulty = difficulty
        self._ui = ui
        self._end_round = False
        self._dices_pairs = None
        # for i in range(1, 7):
        #     self._ui.checkBox[i].stateChanged.connect(lambda: self._mutex_box(i))
    
    def _mutex_box(self, n):
        """This method manage the route selection""
        Parameters
        ----------
        n : int
        """
        # print("_mutex_box called with n=", n) # DEBUG PRINT
        if (n == 1 or n == 4) and self._ui.checkBox[n].isChecked():
            self._ui.checkBox[2].setEnabled(False)
            self._ui.checkBox[5].setEnabled(False)
            self._ui.checkBox[3].setEnabled(False)
            self._ui.checkBox[6].setEnabled(False)
        elif (n == 2 or n == 5) and self._ui.checkBox[n].isChecked():
            self._ui.checkBox[1].setEnabled(False)
            self._ui.checkBox[4].setEnabled(False)
            self._ui.checkBox[3].setEnabled(False)
            self._ui.checkBox[6].setEnabled(False)
        elif (n == 3 or n == 6) and self._ui.checkBox[n].isChecked():
            self._ui.checkBox[1].setEnabled(False)
            self._ui.checkBox[4].setEnabled(False)
            self._ui.checkBox[2].setEnabled(False)
            self._ui.checkBox[5].setEnabled(False)
        elif (n == 1 or n == 4) and self._ui.checkBox[n].isChecked():
            self._ui.checkBox[2].setEnabled(False)
            self._ui.checkBox[5].setEnabled(False)
            self._ui.checkBox[3].setEnabled(False)
            self._ui.checkBox[6].setEnabled(False)
        else:
            self._ui.updateSelectFrame(self._dices_pairs, self._bonzes, BLOCKED,
                                       self._max_bonzes)  # UPDATE SELECT FRAME
    
    def dice_options(self, dices):
        """This method calculate all the sum pairs of the dices
        Parameters
        ----------
        dices : tuple

        Returns
        ----------
        list

        """
        return [dices[0] + dices[1], dices[0] + dices[2], dices[0] + dices[3],
                dices[2] + dices[3], dices[1] + dices[3], dices[2] + dices[1]]
    
    def throw_dices(self):
        """This method simulate a 4-dice throw. """
        self._ui.SelectFrame.setDisabled(False)  # ENABLE FRAME
        self._ui.StopButton.setDisabled(True)  # DISABLE STOP BUTTON
        throw = tuple(random.randint(MIN_DICE, MAX_DICE) for i in range(N_DICE))  # GET DICES RESULT IN A TUPLE
        self._ui.updateDiceFrame(throw)  # DRAW DICES ON DICE FRAME
        self._ui.RollButton.setDisabled(True)  # DISABLE ROLL BUTTON
        self._ui.GoButton.setDisabled(False)  # ENABLE GO BUTTON
        self._dices_pairs = self.dice_options(throw)
        self._ui.updateSelectFrame(self._dices_pairs, self._bonzes, BLOCKED, self._max_bonzes)  # UPDATE SELECT FRAME
        # print(throw,self._dices_pairs)  # DEBUG PRINT
    
    def stop_round(self):
        """This method manage a end of round when the Stop button is clicked. """
        self._ui.StopButton.setDisabled(True)  # DISABLE STOP BUTTON
        self.save_pions()  # SAVE BONZOS POSITIONS
        self.check_blocked_route()  # CHECK BLOCKED ROUTE
        # print("Pion à placer:", self._pawns)    # DEBUG PRINT
        self.reset_bonzes()  # RESET BONZOS IN uiMAINE AND self._bonzes
        # print("Stop")                           # DEBUG PRINT
        self._end_round = True  # SET END OF THE ROUND
    
    def choose_route(self):
        """This method manage the route selection when the GO button is clicked"""
        label = None
        active = None
        label, active = Gui.extract_checkbox(self._ui)  # EXTRACT SELECTET CHECKBOXES
        # check is selection is good
        if self.check_selection(label, active):
            # uiMain.GoButton.setDisabled(True)             # DISABLE GO BUTTON
            self._ui.StopButton.setDisabled(False)  # DISABLE STOP BUTTON
            # uiMain.SelectFrame.setDisabled(True)          # DISABLE FRAME
            if self.count_active(active) > 0:
                for i in range(6):
                    if active[i]:  # CHECK IF CHECKBOX[i] IS SELECTED
                        if label[i] in self._bonzes:  # CHECK IF BONZO IS PALCED IN COLUMN
                            self.move_bonzo(label[i])
                        else:
                            self.place_bonzo(label[i])
                # print("Route selection status: ", label, active)       # DEBUG PRINT
                self._ui.RollButton.setDisabled(False)  # ENABLE ROLL BUTTON
                self._ui.GoButton.setDisabled(True)  # DISABLE GO BUTTON
                Gui.uncheckSelectFrame(self._ui)  # RESET SELECT FRAME CHECKBOXES
                Gui.set_Free_Bonzos(self._ui,
                                    str(self._max_bonzes - len(self._bonzes)))  # RESET SELECT FRAME CHECKBOXES
                # else:
                #     self.show_error_message("Lost your Bonzes")
    
    def check_selection(self, label, active):
        """This method check the route selection
        Parameters
        ----------
        label : list
        active: list

        Returns
        ----------
        bool

        """
        flag = True
        error = QtGui.QWidget()
        # label, active = Gui.extract_checkbox(self._ui)  # EXTRACT SELECTET CHECKBOXES
        n = self.count_active(active)
        if n > 2:  # CHECH IF MORE THAN TWO ROUTES ARE CHOOSEN
            flag = False
            self.show_error_message("You can choose max 2 path x time")
        elif n > self.bonzesLeft():  # CHECK IF THE SELECTION CONTAINS ROUTES WIHT BONZES
            # checklist is the intersection fo the two list
            labelist = set([label[i] for i in range(6) if active[i]])
            checklist = labelist.intersection(self._bonzes.keys())
            stoplist = labelist.intersection(BLOCKED)
            
            if len(checklist) == 0:
                if len(labelist) != 1:
                    flag = False
                    self.show_error_message("Not enugh Bonzes")
            if len(stoplist) != 0:
                flag = False
                self.show_error_message("The route selected is blocked")
        elif n == 0:
            flag = False
            for key, value in self._bonzes.items():
                self._ui.removePion(key, value)  # PLACE PION ON THE MAIN WINDOW
            self.reset_bonzes()
            self._end_round = True  # RETURN END OF THE ROUND
            if self.isAI:
                self.show_AI_message("Lost your Bonzes")
            else:
                self.show_error_message("Lost your Bonzes")
        return flag
    
    def bonzesLeft(self):
        """This method return left bonzes """
        return self._max_bonzes - len(self._bonzes)
    
    def place_bonzo(self, column):
        """This method manage the bonzos emplacement
        Parameters
        ----------
        column : int

        """
        row = self.next_free(column)
        self._bonzes[column] = row  # SAVE BONZO'S POSITION
        self._ui.placeBonzo(column, row)  # PLACE BONZO IN GUI
    
    def move_bonzo(self, column):
        """This method manage the bonzos movements
        Parameters
        ----------
        column : int

        """
        if self._bonzes[column] == HEIGHT[column] - 1:  # IF BONZO EXCEEDS MAX_HEIGHT
            row = HEIGHT[column] - 1
        else:
            row = self._bonzes[column]
            self._ui.removeBonzo(column, row)
            row = self.next_row(column)
            self._bonzes[column] = row  # SAVE BONZO'S POSITION
            self._ui.placeBonzo(column, row)  # PLACE BONZO IN GUI
    
    def pion_on_board(self, column, player):
        """This method look for pion on the board
        Parameters
        ----------
        column : int
        player : int

        Return
        ----------
        int
        """
        row = -1
        if column in BOARD:
            for value in BOARD[column]:
                if value[1] == player:
                    row = value[0]
        return row
    
    def next_row(self, column):
        """This method look for the next row
        Parameters
        ----------
        column : int

        Return
        ----------
        int
        """
        maximum = max(self._bonzes[column] + 1, self.next_free(column))
        if column in BOARD:
            vector = [x for x, y in BOARD[column]]
            while maximum in vector and maximum < HEIGHT[column]:
                maximum += 1
        return maximum
    
    def next_free(self, column):
        """This method look for the next free spot in a column
        Parameters
        ----------
        column : int

        Return
        ----------
        int
        """
        row = self.pion_on_board(column, self._color)
        if row > 0:
            vector = [x for x, y in BOARD[column]]
            while row in vector and row < HEIGHT[column]:
                row += 1
        elif column in BOARD:
            row = self.next_spot(column)
        else:
            row = 0
        return row
    
    def next_spot(self, column):
        """This method look for the next spot
        when pions of other players are ont the board
        Parameters
        ----------
        column : int

        Return
        ----------
        int
        """
        # if column not in BOARD:
        #     return 0
        val = [x for x, y in BOARD[column]]
        i = 0
        while i in val and i < HEIGHT[column]:
            i += 1
        return i
    
    def count_active(self, list):
        """This method counts the number of active checkbox
        Parameters
        ----------
        list : list

        Return
        ----------
        int
        """
        count = 0
        for value in list:
            if value:
                count += 1
        return count
    
    def show_error_message(self, msg):
        """This method pop up a dialog message on the GUI
        Parameters
        ----------
        msg : str
        """
        error = QtGui.QWidget()
        QtGui.QMessageBox.warning(error, "Error", "{}".format(msg))
        error.show()
        # error.exec_()
    
    def there_is_a_winner(self):
        """ Thin method check if three pawns/bonzes
        have reached simultaneously the top of the corresponding routes.
        """
        pawns_on_top = 0
        if (len(self._pawns) < 3):
            return False, 0
        else:
            for route in self._pawns:
                if self._pawns[route] == HEIGHT[route] - 1:
                    pawns_on_top += 1
            if (pawns_on_top >= 3):
                return True, self._id
            else:
                return False, 0
    
    def check_blocked_route(self):
        """ Thin method block the routes"""
        for key, value in self._pawns.items():
            if value == HEIGHT[key] - 1:
                self._ui.lock_route(key)
                BLOCKED.append(key)
    
    def save_pions(self):
        """ Thin method save the pions at the end of the round"""
        for key, value in self._pawns.items():  # FOR ALL PAWNS
            if key in self._bonzes:
                self._ui.removePion(key, value)  # REMOVE PION ON THE MAIN WINDOW
                BOARD[key].remove((value, self._color))  # REMOVE PION ON THE BOARD
        for key, value in self._bonzes.items():
            self._ui.placePion(key, value, self._color)  # PLACE PION ON THE MAIN WINDOW
            self._pawns[key] = value
        
        # self._pawns = copy.deepcopy(self._bonzes)
        # self._pawns = self._bonzes.copy()
        self.save_board(self._bonzes)
    
    def save_board(self, dict):
        """This method save the board status
        Parameters
        ----------
        dict : dict
        """
        for key, value in dict.items():
            if key in BOARD:
                BOARD[key].append((value, self._color))
                BOARD[key].sort()
            else:
                BOARD[key] = [(value, self._color)]
    
    def reset_bonzes(self):
        """ Empties the bonzes dictionary and remove their representation on th main window"""
        self._bonzes.clear()
        
    def get_id(self):
        """
        Return the id
        
        Return
        ---------
        int
        """
        return self._id
    
    # AI SECTION
    def show_AI_message(self, msg):
        """This method shows AI message on the Mian Window
        Parameters
        ----------
        msg : str
        """
        self._ui.set_AI_message(msg)
        QtGui.qApp.processEvents()
        time.sleep(AI_MSG)
    
    def showAI(self):
        """This method refresh the Main Window"""
        self._ui.lockCommandFrame()
        self._ui.lockSelectFrame()
        QtGui.qApp.processEvents()
    
    def AI_choose_route(self, game):
        """This method search for a route for the AI
        Returns
        ----------
        list
        """
        dice = None
        other_players = game.get_other_players(self._id)
        scores = [self.AI_score_voie_with_jump(voie, other_players) for voie in range(2, 13)]
        if self.difficulty == 1:
            other_scores = [self.AI_score_voie_with_distance(voie) for voie in range(2, 13)]
            scores = [ALPHA*scores[i]+BETA*other_scores[i] for i in range(len(scores))]
        try:
            dice = self.AI_compute_best_shot(scores)
        except:
            pass
        if dice == 1 or dice == 4:
            boxes = [1, 4]
        if dice == 2 or dice == 5:
            boxes = [2, 5]
        if dice == 3 or dice == 6:
            boxes = [3, 6]
        return boxes
    
    def AI_choice(self, game):
        """This method simulate the choice of the route for the AI
        Returns
        ----------
        list
        """
        boxes = self.AI_choose_route(game)
        labels = [int(self._ui.checkBox[boxes[0]].text()), int(self._ui.checkBox[boxes[1]].text())]
        labelist = set(labels)
        checklist = labelist.intersection(self._bonzes.keys())
        stoplist = labelist.intersection(BLOCKED)
        
        if len(stoplist) != 0:  # BOTH ROUTE BLOCKED
            self.show_AI_message("Route blocked")
            return (None, None)
        
        if self.bonzesLeft() < 2:  # CHECK IF THE SELECTION CONTAINS ROUTES WIHT BONZES
            if len(checklist) == 0:
                if self.bonzesLeft() == 1:
                    self.show_AI_message("I choose {} ".format(labels[0]))
                    res = (boxes[0], None)
                else:
                    self.show_AI_message("No choice")
                    res = (None, None)
            elif len(checklist) == 2:
                self.show_AI_message("I choose {} and {}".format(labels[0], labels[1]))
                res = (boxes[0], boxes[1])
            else:
                if self.bonzesLeft() == 1:
                    self.show_AI_message("I choose {} and {}".format(labels[0], labels[1]))
                    res = (boxes[0], boxes[1])
                else:
                    if labels[0] in self._bonzes:
                        self.show_AI_message("I choose {} ".format(labels[0]))
                        res = (boxes[0], None)
                    else:
                        self.show_AI_message("I choose {} ".format(labels[1]))
                        res = (boxes[1], None)
        else:
            self.show_AI_message("I choose {} and {}".format(labels[0], labels[1]))
            res = (boxes[0], boxes[1])
        return res
    
    def AI(self, game):
        """
        This method simulate the AI behavior
        
        Parameters
        ----------
        game : Jeu
        """
        stop = False
        step = 0
        while not stop:
            self.show_AI_message("I'm player {}".format(self._color))
            self.showAI()
            self.show_AI_message("Rolling the dices ...")
            # time.sleep(PAUSE)
            self.throw_dices()
            self.showAI()
            self.show_AI_message("Thinking ...")
            # time.sleep(PAUSE)
            choice = self.AI_choice(game)
            # choice = random.randint(MIN_DICE, MAX_DICE)
            # self.show_AI_message("I choose {}".format(choice))
            for i in range(2):
                if choice[i]:
                    self._ui.checkBox[choice[i]].toggle()
            self.showAI()
            time.sleep(PAUSE)
            self.choose_route()
            self.showAI()
            self.show_AI_message("Thinking ...")
            time.sleep(PAUSE)
            stop = self.AI_choose_stop(step)
            step += 1
            if stop:
                self.show_AI_message("I want to stop!")
                stop = True
                self.stop_round()
                self.showAI()
                self.show_AI_message("Next Player")

    def AI_score_voie_with_jump(self, voie, other_players):
        """
        Return the score of the voie
        
        Parameters
        ----------
        voie : int
        other_players : list of Joueur
        
        Return
        ----------
        int
        """
        score = 0
        for player in other_players:
            pawns = player._pawns
            try:
                if pawns[voie] == self._bonzes[voie]-1:
                    score = 3
                elif pawns[voie] == self._pawns[voie]-1:
                    score = 1
            except:
                pass
        return score
    
    def AI_score_voie_with_distance(self, voie):
        """
        Return the score of the voie
        
        Parameters
        ----------
        voie : int
        
        Return
        ----------
        int
        """
        
        if voie in self._bonzes:
            return 1/(HEIGHT[voie]-self._bonzes[voie])
        elif voie in self._pawns:
            return 1/(HEIGHT[voie]-self._pawns[voie])
        else:
            return 0

    def AI_compute_best_shot(self, scores):
        """
        Returns
        ---------
        int
        """
        
        sums = [scores[self._dices_pairs[0]-2] + scores[self._dices_pairs[3]-2],
                scores[self._dices_pairs[1]-2] + scores[self._dices_pairs[4]-2],
                scores[self._dices_pairs[2]-2] + scores[self._dices_pairs[5]-2]]
        return sums.index(max(sums))+1

    def AI_choose_stop(self, step_count):
        """
        Return
        ---------
        bool
        """
        
        for i in self._bonzes.keys():
            if self._bonzes[i] == HEIGHT[i]:
                return True  # If the AI has one bonze on top, it save it by stoping it's turn
        return random.randint(0, AI_MAX_STEPS) <= step_count
