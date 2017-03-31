# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/designer/CantStopGUI.ui'
#
# Created by: PyQt4 UI code generator 4.12 and reviseted by the author
#


import icons_rc
from PyQt4 import QtCore, QtGui

__author__ = "Luciano Porretta"
__copyright__ = "Copyright 2017, Luciano Porretta"
__credits__ = ["Luciano Porretta "]
__license__ = "ULB Theaching License"
__version__ = "1.0"
__maintainer__ = "Luciano Porretta"
__email__ = "luciano.porretta@ulb.ac.be"
__status__ = "Beta"

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    
    
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Gui(object):
    # COLORS
    red = QtGui.QColor(255, 0, 0)
    green = QtGui.QColor(0, 255, 0)
    blue = QtGui.QColor(0, 0, 255)
    yellow = QtGui.QColor(255, 255, 0)
    white = QtGui.QColor(255, 255, 255)
    head = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline; color:#000000;\">"
    tail = "\'s Turn</span></p></body></html>"
    
    def __init__(self):
        self.setupWindow = None
        # QPimax Setup
        self._user_png = QtGui.QPixmap(_fromUtf8(":/icns/blueberry/PNG/32/user_friend.png"))
        self._cpu_png = QtGui.QPixmap(_fromUtf8(":/icns/blueberry/PNG/32/computer_monitor.png"))
        self._none_png = QtGui.QPixmap(_fromUtf8(":/icns/blueberry/PNG/32/delete_2.png"))
        # QPimax Main
        self._medal_png = QtGui.QPixmap(_fromUtf8(":/pion/pions/Sports-Medal-2-icon.png"))
        self._pion_png = QtGui.QPixmap(_fromUtf8(":/pion/pions/Science-Geometry-icon-2.png"))
        self._bonzo_png = QtGui.QPixmap(_fromUtf8(":/pion/pions/Sports-Meditation-Guru-icon.png"))
        self._rolling_png = QtGui.QPixmap(_fromUtf8(":/dice/dice/rolling.png"))
        self._stop_png = QtGui.QPixmap(_fromUtf8(":/base/base/stop-800px.png"))
        self._dice_png = {
            1: QtGui.QPixmap(_fromUtf8(":/dice/dice/1.png")),
            2: QtGui.QPixmap(_fromUtf8(":/dice/dice/2.png")),
            3: QtGui.QPixmap(_fromUtf8(":/dice/dice/3.png")),
            4: QtGui.QPixmap(_fromUtf8(":/dice/dice/4.png")),
            5: QtGui.QPixmap(_fromUtf8(":/dice/dice/5.png")),
            6: QtGui.QPixmap(_fromUtf8(":/dice/dice/6.png"))
        }
        # ICONS SETUP
        self.icon_user = QtGui.QIcon()
        self.icon_user.addPixmap(self._user_png, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_cpu = QtGui.QIcon()
        self.icon_cpu.addPixmap(self._cpu_png, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon_none = QtGui.QIcon()
        self.icon_none.addPixmap(self._none_png, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # ICONS MAIN
        self.pion_icon = QtGui.QIcon()
        self.pion_icon.addPixmap(self._pion_png, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bonzo_icon = QtGui.QIcon()
        self.bonzo_icon.addPixmap(self._bonzo_png, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.roll_icon = QtGui.QIcon()
        self.roll_icon.addPixmap(self._rolling_png, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_icon = QtGui.QIcon()
        self.stop_icon.addPixmap(self._stop_png, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # USEFUL DICTIONARY 4 SETUP
        self.frame = {}
        self.frame_title = {}
        self.radio_user = {}
        self.radio_cpu = {}
        self.radio_none = {}
        self.combo_difficulty = {}
        # USEFUL DICTIONARY MAIN
        self._route_len = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
        self.colors = {'Red': Gui.red, 'Green': Gui.green, 'Blue': Gui.blue, 'Yellow': Gui.yellow}
        self.bottom_label = {}
        self.top_label = {}
        self.route = {}
        self.dice = {}
        self.checkBox = {}
        self.error = QtGui.QWidget()
    
    # SETUP METHODS
    def _frame(self, n):
        """ SETUP FRAME
        Parameters
        ----------
        frame : QtGui.QFrame
        n : int
        """
        frame = QtGui.QFrame(self.MainFrame)
        frame.setFrameShape(QtGui.QFrame.StyledPanel)
        frame.setFrameShadow(QtGui.QFrame.Raised)
        frame_title = QtGui.QLabel(frame)
        if n == 1:
            frame.setObjectName(_fromUtf8("P1_frame"))
        if n == 2:
            frame.setObjectName(_fromUtf8("P2_frame"))
        if n == 3:
            frame.setObjectName(_fromUtf8("P3_frame"))
        if n == 4:
            frame.setObjectName(_fromUtf8("P4_frame"))
        return frame
    
    def _frame_title(self, frame, n):
        """ SETUP FRAME TITLE
        Parameters
        ----------
        frame : QtGui.QFrame
        n : int
        """
        frame_title = QtGui.QLabel(frame)
        frame_title.setGeometry(QtCore.QRect(0, 0, 350, 21))
        if n == 1:
            frame_title.setObjectName(_fromUtf8("P1_frame_title"))
        if n == 2:
            frame_title.setObjectName(_fromUtf8("P2_frame_title"))
        if n == 3:
            frame_title.setObjectName(_fromUtf8("P3_frame_title"))
        if n == 4:
            frame_title.setObjectName(_fromUtf8("P4_frame_title"))
        font = QtGui.QFont()
        font.setPointSize(18)
        frame_title.setFont(font)
        frame_title.setFrameShape(QtGui.QFrame.WinPanel)
        frame_title.setFrameShadow(QtGui.QFrame.Raised)
        return frame_title
    
    def _radio_user(self, layout, hlayout, n):
        """ SETUP RADIO BUTTONS 4 USER
        Parameters
        ----------
        layout : QtGui.QWidget
        hlayout : QtGui.QHBoxLayout
        n : int
        """
        radio = QtGui.QRadioButton(layout)
        radio.setIcon(self.icon_user)
        if n == 1:
            radio.setObjectName(_fromUtf8("P1_User_radio"))
            hlayout.addWidget(radio)
        if n == 2:
            radio.setObjectName(_fromUtf8("P2_User_radio"))
            hlayout.addWidget(radio)
        if n == 3:
            radio.setObjectName(_fromUtf8("P3_User_radio"))
            hlayout.addWidget(radio)
        if n == 4:
            radio.setObjectName(_fromUtf8("P4_User_radio"))
            hlayout.addWidget(radio)
        radio.setChecked(True)
        return radio
    
    def _radio_cpu(self, layout, hlayout, n):
        """ SETUP RADIO BUTTONS 4 CPU
        Parameters
        ----------
        layout : QtGui.QWidget
        hlayout : QtGui.QHBoxLayout
        n : int
        """
        radio = QtGui.QRadioButton(layout)
        radio.setIcon(self.icon_cpu)
        if n == 1:
            radio.setObjectName(_fromUtf8("P1_CPU_radio"))
            hlayout.addWidget(radio)
        if n == 2:
            radio.setObjectName(_fromUtf8("P2_CPU_radio"))
            hlayout.addWidget(radio)
        if n == 3:
            radio.setObjectName(_fromUtf8("P3_CPU_radio"))
            hlayout.addWidget(radio)
        if n == 4:
            radio.setObjectName(_fromUtf8("P4_CPU_radio"))
            hlayout.addWidget(radio)
        return radio
    
    def _radio_none(self, layout, hlayout, n):
        """ SETUP RADIO BUTTONS 4 NONE
        Parameters
        ----------
        layout : QtGui.QWidget
        hlayout : QtGui.QHBoxLayout
        n : int
        """
        radio = QtGui.QRadioButton(layout)
        radio.setIcon(self.icon_none)
        if n == 1:
            radio.setObjectName(_fromUtf8("P1_None_radio"))
            hlayout.addWidget(radio)
        if n == 2:
            radio.setObjectName(_fromUtf8("P2_None_radio"))
            hlayout.addWidget(radio)
        if n == 3:
            radio.setObjectName(_fromUtf8("P3_None_radio"))
            hlayout.addWidget(radio)
        if n == 4:
            radio.setObjectName(_fromUtf8("P4_None_radio"))
            hlayout.addWidget(radio)
        return radio
    
    # MAIN METHODS
    def _bottom_label(self, board, n):
        """This method setup a bottom label given a board and a number n
        Parameters
        ----------
        board : QtGui.QFrame
        n : int
        """
        label = QtGui.QLabel(board)
        if n == 2:
            label.setGeometry(QtCore.QRect(30, 330, 35, 21))
            label.setObjectName(_fromUtf8("bottom_label2"))
        if n == 3:
            label.setGeometry(QtCore.QRect(80, 360, 35, 21))
            label.setObjectName(_fromUtf8("bottom_label3"))
        if n == 4:
            label.setGeometry(QtCore.QRect(130, 390, 35, 21))
            label.setObjectName(_fromUtf8("bottom_label4"))
        if n == 5:
            label.setGeometry(QtCore.QRect(180, 420, 35, 21))
            label.setObjectName(_fromUtf8("bottom_label5"))
        if n == 6:
            label.setGeometry(QtCore.QRect(230, 450, 35, 21))
            label.setObjectName(_fromUtf8("bottom_label6"))
        if n == 7:
            label.setGeometry(QtCore.QRect(280, 480, 35, 21))
            label.setObjectName(_fromUtf8("bottom_label7"))
        if n == 8:
            label.setGeometry(QtCore.QRect(330, 450, 35, 20))
            label.setObjectName(_fromUtf8("bottom_label8"))
        if n == 9:
            label.setGeometry(QtCore.QRect(380, 420, 35, 20))
            label.setObjectName(_fromUtf8("bottom_label9"))
        if n == 10:
            label.setGeometry(QtCore.QRect(430, 400, 35, 20))
            label.setObjectName(_fromUtf8("bottm_label10"))
        if n == 11:
            label.setGeometry(QtCore.QRect(480, 370, 35, 20))
            label.setObjectName(_fromUtf8("bottom_label11"))
        if n == 12:
            label.setGeometry(QtCore.QRect(530, 340, 35, 20))
            label.setObjectName(_fromUtf8("bottom_label12"))
        
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setAutoFillBackground(False)
        label.setStyleSheet(_fromUtf8("background-image: url(:/back/backgrounds/grey5.jpg);"))
        label.setFrameShape(QtGui.QFrame.Panel)
        label.setFrameShadow(QtGui.QFrame.Raised)
        label.setLineWidth(1)
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label
    
    def _route(self, board, n):
        """This method setup a route given a board and a number n""
        Parameters
        ----------
        board : QtGui.QFrame
        n : int
        """
        route = QtGui.QTableWidget(board)
        if n == 2:
            route.setObjectName(_fromUtf8("route2"))
            route.setGeometry(QtCore.QRect(30, 240, 35, 91))
        if n == 3:
            route.setObjectName(_fromUtf8("route3"))
            route.setGeometry(QtCore.QRect(80, 210, 35, 151))
        if n == 4:
            route.setObjectName(_fromUtf8("route4"))
            route.setGeometry(QtCore.QRect(130, 180, 35, 211))
        if n == 5:
            route.setObjectName(_fromUtf8("route5"))
            route.setGeometry(QtCore.QRect(180, 150, 35, 271))
        if n == 6:
            route.setObjectName(_fromUtf8("route6"))
            route.setGeometry(QtCore.QRect(230, 120, 35, 331))
        if n == 7:
            route.setObjectName(_fromUtf8("route7"))
            route.setGeometry(QtCore.QRect(280, 90, 35, 391))
        if n == 8:
            route.setObjectName(_fromUtf8("route8"))
            route.setGeometry(QtCore.QRect(330, 120, 35, 331))
        if n == 9:
            route.setObjectName(_fromUtf8("route9"))
            route.setGeometry(QtCore.QRect(380, 150, 35, 271))
        if n == 10:
            route.setObjectName(_fromUtf8("route10"))
            route.setGeometry(QtCore.QRect(430, 190, 35, 211))
        if n == 11:
            route.setObjectName(_fromUtf8("route11"))
            route.setGeometry(QtCore.QRect(480, 220, 35, 151))
        if n == 12:
            route.setObjectName(_fromUtf8("route12"))
            route.setGeometry(QtCore.QRect(530, 250, 35, 91))
        
        route.setColumnCount(1)
        route.setRowCount(self._route_len[n])
        for i in range(self._route_len[n]):
            item = QtGui.QTableWidgetItem()
            route.setVerticalHeaderItem(i, item)
        
        route.setHorizontalHeaderItem(0, item)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(route.sizePolicy().hasHeightForWidth())
        route.setSizePolicy(sizePolicy)
        route.setStyleSheet(_fromUtf8("background-image: url(:/back/backgrounds/grey-linen-texture.jpg);"))
        route.setFrameShape(QtGui.QFrame.StyledPanel)
        route.setFrameShadow(QtGui.QFrame.Sunken)
        route.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        route.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        route.setAutoScroll(False)
        route.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        route.setTabKeyNavigation(False)
        route.setProperty("showDropIndicator", False)
        route.setDragDropOverwriteMode(False)
        route.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        route.setIconSize(QtCore.QSize(25, 25))
        route.setShowGrid(True)
        route.setEnabled(True)
        route.horizontalHeader().setVisible(False)
        route.horizontalHeader().setHighlightSections(False)
        route.verticalHeader().setVisible(False)
        route.verticalHeader().setHighlightSections(False)
        
        return route
    
    def _top_label(self, board, n):
        """This method setup a top label given a board and a number n
        Parameters
        ----------
        board : QtGui.QFrame
        n : int
        """
        label = QtGui.QLabel(board)
        if n == 2:
            label.setObjectName(_fromUtf8("top_label2"))
            label.setGeometry(QtCore.QRect(30, 190, 35, 35))
        if n == 3:
            label.setObjectName(_fromUtf8("top_label3"))
            label.setGeometry(QtCore.QRect(80, 160, 35, 35))
        if n == 4:
            label.setObjectName(_fromUtf8("top_label4"))
            label.setGeometry(QtCore.QRect(130, 130, 35, 35))
        if n == 5:
            label.setObjectName(_fromUtf8("top_label5"))
            label.setGeometry(QtCore.QRect(180, 100, 35, 35))
        if n == 6:
            label.setObjectName(_fromUtf8("top_label6"))
            label.setGeometry(QtCore.QRect(230, 70, 35, 35))
        if n == 7:
            label.setObjectName(_fromUtf8("top_label7"))
            label.setGeometry(QtCore.QRect(280, 40, 35, 35))
        if n == 8:
            label.setObjectName(_fromUtf8("top_label8"))
            label.setGeometry(QtCore.QRect(330, 70, 35, 35))
            # label.setPixmap(QtGui.QPixmap(_fromUtf8(":/pion/pions/Sports-Medal-2-icon.png")))
        if n == 9:
            label.setObjectName(_fromUtf8("top_label9"))
            label.setGeometry(QtCore.QRect(380, 100, 35, 35))
        if n == 10:
            label.setObjectName(_fromUtf8("top_label10"))
            label.setGeometry(QtCore.QRect(430, 140, 35, 35))
        if n == 11:
            label.setObjectName(_fromUtf8("top_label11"))
            label.setGeometry(QtCore.QRect(480, 170, 35, 35))
        if n == 12:
            label.setObjectName(_fromUtf8("top_label12"))
            label.setGeometry(QtCore.QRect(530, 200, 35, 35))
        
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        label.setFont(font)
        label.setAutoFillBackground(False)
        label.setStyleSheet(_fromUtf8("background-image: url(:/back/backgrounds/Carbonfiber.jpg);"))
        label.setFrameShape(QtGui.QFrame.Box)
        label.setFrameShadow(QtGui.QFrame.Sunken)
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label
    
    def _dice(self, n):
        """This method setup a dice given the his number
        Parameters
        ----------
        board : QtGui.QFrame
        n : int
        """
        dice = QtGui.QLabel(self.DiceFrame)
        if n == 1:
            dice.setObjectName(_fromUtf8("dice1"))
            dice.setGeometry(QtCore.QRect(10, 10, 40, 40))
            # dice.setPixmap(QtGui.QPixmap(_fromUtf8(":/dice/dice/4.png")))
        if n == 2:
            dice.setObjectName(_fromUtf8("dice2"))
            dice.setGeometry(QtCore.QRect(90, 10, 40, 40))
            # dice.setPixmap(QtGui.QPixmap(_fromUtf8(":/dice/dice/1.png")))
        if n == 3:
            dice.setObjectName(_fromUtf8("dice3"))
            dice.setGeometry(QtCore.QRect(50, 70, 40, 40))
            # dice.setPixmap(QtGui.QPixmap(_fromUtf8(":/dice/dice/3.png")))
        if n == 4:
            dice.setObjectName(_fromUtf8("dice4"))
            dice.setGeometry(QtCore.QRect(130, 70, 40, 40))
            # dice.setPixmap(QtGui.QPixmap(_fromUtf8(":/dice/dice/5.png")))
        
        dice.setText(_fromUtf8(""))
        dice.setScaledContents(True)
        return dice
    
    # PUBLIC METHODS (INTERFACE)
    def placeBonzo(self, column, row):
        """
         This method place a Bonzo on the route

         Parameters
         ----------
         column : int
         row : int
         player : int
         """
        item = QtGui.QTableWidgetItem()
        item.setIcon(self.bonzo_icon)
        brush = QtGui.QBrush(Gui.white)
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.route[column].setItem(self._route_len[column] - row - 1, 0, item)
    
    def removeBonzo(self, column, row):
        """
         This method remove a Bonzo on the route

         Parameters
         ----------
         column : int
         row : int
         """
        item = QtGui.QTableWidgetItem()
        self.route[column].setItem(self._route_len[column] - row - 1, 0, item)
    
    def removePion(self, column, row):
        """
         This method remove a Pion on the route

         Parameters
         ----------
         column : int
         row : int
         """
        item = QtGui.QTableWidgetItem()
        self.route[column].setItem(self._route_len[column] - row - 1, 0, item)
    
    def placePion(self, column, row, player):
        """
        This method place a Pion on the route

        Parameters
        ----------
        column : int
        row : int
        player : char
        """
        item = QtGui.QTableWidgetItem()
        item.setIcon(self.pion_icon)
        brush = QtGui.QBrush(self.colors[player])
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.route[column].setItem(self._route_len[column] - row - 1, 0, item)
    
    def lock_route(self, column):
        """
        This method lock a route

        Parameters
        ----------
        column : int
        """
        self.top_label[column].setPixmap(self._medal_png)
        self.top_label[column].setScaledContents(True)
        self.route[column].setEnabled(False)
        self.bottom_label[column].setEnabled(False)
    
    def updateDiceFrame(self, dices):
        """
        This method update the Dice Frame

        Parameters
        ----------
        dices : tuple
        """
        for i in range(1, 5):
            self.dice[i].setPixmap(self._dice_png[dices[i - 1]])
    
    def updateSelectFrame(self, dices, filter, blocked, max):
        """
        This method update the Select Frame

        Parameters
        ----------
        dices : tuple
        filter : dict
        blocked: list
        max : int
        """
        
        self.uncheckSelectFrame()  # UNCHECK BOXES
        for i in range(6):
            self.checkBox[i + 1].setText(_translate("Main", str(dices[i]), None))  # UPDATE CHECKBOX LABELS
            if len(filter) == max and dices[i] not in filter:  # IF THE ROUTE CANNOT BE SELECTED
                self.checkBox[i + 1].setEnabled(False)  # THE CHECKBOX IS DISABLED
            else:
                if dices[i] in blocked:
                    self.checkBox[i + 1].setEnabled(False)  # THE CHECKBOX IS DISABLED
                else:
                    self.checkBox[i + 1].setEnabled(True)  # THE CHECKBOX IS ENABLED
    
    def uncheckSelectFrame(self):
        """
         This method uncheck boxes in the Select Frame

         """
        
        for i in range(1, 7):
            self.checkBox[i].setChecked(False)
    
    def lockCommandFrame(self):
        """
         This method lock the Command Frame

         """
        self.RollButton.setDisabled(True)
        self.StopButton.setDisabled(True)
    
    def lockSelectFrame(self):
        """
         This method lock the Select Frame

         """
        self.GoButton.setDisabled(True)
        for i in range(1, 7):
            self.checkBox[i].setDisabled(True)
    
    def extract_radio(self):
        """
         This method extract radio values

         """
        count = 0
        active = []
        for i in range(1, 5):
            if self.radio_user[i].isChecked():
                active.append('Active')
                count += 1
            elif self.radio_cpu[i].isChecked():
                active.append('CPU')
                count += 1
            else:
                active.append(None)
        return count, active
    
    def extract_checkbox(self):
        """
         This method extract checkbox values
         """
        label = []
        active = []
        for i in range(1, 7):
            label.append(int(self.checkBox[i].text()))
            if self.checkBox[i].isChecked():
                active.append(True)
            else:
                active.append(False)
        return label, active
    
    def set_Command_Title(self, msg):
        """
         This method update the Command Title label

         Parameters
         ----------
         msg : str
         """
        
        self.CommandTitle.setText(_translate("Main", "{}{}{}".format(Gui.head, msg, Gui.tail), None))
    
    def set_AI_message(self, msg):
        """
         This method update the Ai Frame Message label

         Parameters
         ----------
         msg : str
         """
        
        self.Ai_label.setText(_translate("Main", "<html><b>AI messages:</b></hml> <i>{}</i>".format(msg), None))
    
    def set_Free_Bonzos(self, msg):
        """
         This method update the Command Title label

         Parameters
         ----------
         msg : str
         """
        self.bonzo_label.setText(_translate("Main", "{} {}".format("Free:", msg), None))
        
    def get_difficulty(self, count):
        """
        Returns
        ----------
        int
        """
        return self.combo_difficulty[count].currentIndex()
    
    # SETUP MAIN WINDOW
    def MainUi(self, Main):
        """ This method setup the User Interface"""
        # MAIN WIDGET
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(601, 675)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setAnimated(True)
        # CENTRAL WIDGET
        self.centralwidget = QtGui.QWidget(Main)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        # BOARD
        self.board = QtGui.QFrame(self.centralwidget)
        self.board.setGeometry(QtCore.QRect(0, -20, 741, 521))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.board.sizePolicy().hasHeightForWidth())
        self.board.setSizePolicy(sizePolicy)
        self.board.setFocusPolicy(QtCore.Qt.NoFocus)
        self.board.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.board.setAutoFillBackground(False)
        self.board.setStyleSheet(_fromUtf8("background-image: url(:/back/backgrounds/green1.jpg);"))
        self.board.setFrameShape(QtGui.QFrame.WinPanel)
        self.board.setFrameShadow(QtGui.QFrame.Plain)
        self.board.setObjectName(_fromUtf8("board"))
        
        # BOARD ELEMENTS
        # INIT BOTTOM LABELS
        for i in range(2, 13):
            self.bottom_label[i] = self._bottom_label(self.board, i)  # BOTTOM_LABEL
        # INIT ROUTES
        for i in range(2, 13):
            self.route[i] = self._route(self.board, i)  # ROUTE
        # INIT TOP LABELS
        for i in range(2, 13):
            self.top_label[i] = self._top_label(self.board, i)  # TOP LABEL
        # INIT DICE FRAME
        self.DiceFrame = QtGui.QFrame(self.centralwidget)
        self.DiceFrame.setGeometry(QtCore.QRect(10, 510, 191, 121))
        self.DiceFrame.setAutoFillBackground(True)
        self.DiceFrame.setFrameShape(QtGui.QFrame.WinPanel)
        self.DiceFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.DiceFrame.setObjectName(_fromUtf8("DiceFrame"))
        # INIT DICES
        for i in range(1, 5):
            self.dice[i] = self._dice(i)  # DICE
        
        # SETUP COMMAND FRAME
        self.CommandFrame = QtGui.QFrame(self.centralwidget)
        self.CommandFrame.setGeometry(QtCore.QRect(210, 510, 161, 121))
        self.CommandFrame.setAutoFillBackground(True)
        self.CommandFrame.setFrameShape(QtGui.QFrame.WinPanel)
        self.CommandFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.CommandFrame.setObjectName(_fromUtf8("CommandFrame"))
        
        # SETUP ROLL BUTTON
        self.RollButton = QtGui.QPushButton(self.CommandFrame)
        self.RollButton.setGeometry(QtCore.QRect(10, 40, 60, 60))
        # self.RollButton.clicked.connect(Jeu.)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.RollButton.setFont(font)
        self.RollButton.setAutoFillBackground(False)
        self.RollButton.setStyleSheet(_fromUtf8("background-image: url(:/back/backgrounds/LightGray.jpg);"))
        self.RollButton.setText(_fromUtf8(""))
        self.RollButton.setIcon(self.roll_icon)
        self.RollButton.setIconSize(QtCore.QSize(50, 50))
        self.RollButton.setObjectName(_fromUtf8("RollButton"))
        
        # SETUP STOP BUTTON
        self.StopButton = QtGui.QPushButton(self.CommandFrame)
        self.StopButton.setGeometry(QtCore.QRect(90, 40, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet(_fromUtf8("background-image: url(:/back/backgrounds/LightGray.jpg);"))
        self.StopButton.setText(_fromUtf8(""))
        self.StopButton.setIcon(self.stop_icon)
        self.StopButton.setIconSize(QtCore.QSize(55, 55))
        self.StopButton.setObjectName(_fromUtf8("StopButton"))
        
        # STEUP COMMAND TITLE
        self.CommandTitle = QtGui.QLabel(self.CommandFrame)
        self.CommandTitle.setGeometry(QtCore.QRect(0, 0, 151, 31))
        font = QtGui.QFont()
        font.setItalic(False)
        self.CommandTitle.setFont(font)
        self.CommandTitle.setFrameShape(QtGui.QFrame.NoFrame)
        self.CommandTitle.setFrameShadow(QtGui.QFrame.Sunken)
        self.CommandTitle.setLineWidth(2)
        self.CommandTitle.setObjectName(_fromUtf8("CommandTitle"))
        
        # SETUP SELECT FRAME
        self.SelectFrame = QtGui.QFrame(self.centralwidget)
        self.SelectFrame.setGeometry(QtCore.QRect(380, 510, 211, 121))
        self.SelectFrame.setAutoFillBackground(True)
        self.SelectFrame.setFrameShape(QtGui.QFrame.WinPanel)
        self.SelectFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.SelectFrame.setObjectName(_fromUtf8("SelectFrame"))
        self.SelectFrameTitle = QtGui.QLabel(self.SelectFrame)
        self.SelectFrameTitle.setGeometry(QtCore.QRect(50, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SelectFrameTitle.setFont(font)
        self.SelectFrameTitle.setObjectName(_fromUtf8("SelectFrameTitle"))
        self.layoutWidget = QtGui.QWidget(self.SelectFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 79, 20))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        
        # SETUP CHECKBOX 1 & 5
        self.horizontalLayout1 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout1.setMargin(0)
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.checkBox[1] = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox[1].setEnabled(True)
        self.checkBox[1].setObjectName(_fromUtf8("checkBox1"))
        # self.checkBox[1].stateChanged.connect(lambda: self._mutex_box(1))
        self.horizontalLayout1.addWidget(self.checkBox[1])
        self.checkBox[4] = QtGui.QCheckBox(self.layoutWidget)
        self.checkBox[4].setEnabled(True)
        self.checkBox[4].setObjectName(_fromUtf8("checkBox4"))
        # self.checkBox[4].stateChanged.connect(lambda: self._mutex_box(4))
        self.horizontalLayout1.addWidget(self.checkBox[4])
        self.layoutWidget1 = QtGui.QWidget(self.SelectFrame)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 78, 20))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        
        # SETUP CHECKBOX 2 & 4
        self.horizontalLayout2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout2.setMargin(0)
        self.horizontalLayout2.setObjectName(_fromUtf8("horizontalLayout2"))
        self.checkBox[2] = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox[2].setEnabled(True)
        self.checkBox[2].setObjectName(_fromUtf8("checkBox2"))
        # self.checkBox[2].stateChanged.connect(lambda: self._mutex_box(2))
        self.horizontalLayout2.addWidget(self.checkBox[2])
        self.checkBox[5] = QtGui.QCheckBox(self.layoutWidget1)
        self.checkBox[5].setEnabled(True)
        self.checkBox[5].setObjectName(_fromUtf8("checkBox5"))
        # self.checkBox[5].stateChanged.connect(lambda: self._mutex_box(5))
        self.horizontalLayout2.addWidget(self.checkBox[5])
        self.layoutWidget2 = QtGui.QWidget(self.SelectFrame)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 100, 79, 20))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        
        # SETUP CHECKBOX 3 & 6
        self.horizontalLayout3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout3.setMargin(0)
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self.checkBox[3] = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox[3].setEnabled(True)
        self.checkBox[3].setObjectName(_fromUtf8("checkBox3"))
        # self.checkBox[3].stateChanged.connect(lambda: self._mutex_box(3))
        self.horizontalLayout3.addWidget(self.checkBox[3])
        self.checkBox[6] = QtGui.QCheckBox(self.layoutWidget2)
        self.checkBox[6].setEnabled(True)
        self.checkBox[6].setObjectName(_fromUtf8("checkBox6"))
        # self.checkBox[6].stateChanged.connect(lambda: self._mutex_box(6))
        self.horizontalLayout3.addWidget(self.checkBox[6])
        self.layoutWidget3 = QtGui.QWidget(self.SelectFrame)
        self.layoutWidget3.setGeometry(QtCore.QRect(104, 44, 88, 69))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        
        # SETUP COMMAND LAYOUT
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.GoButton = QtGui.QPushButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        
        # GOBUTTON
        self.GoButton.setFont(font)
        self.GoButton.setStyleSheet(_fromUtf8("background-image: url(:/back/backgrounds/LightGray.jpg);"))
        self.GoButton.setIcon(self.bonzo_icon)
        self.GoButton.setIconSize(QtCore.QSize(32, 32))
        self.GoButton.setObjectName(_fromUtf8("GoButton"))
        self.verticalLayout.addWidget(self.GoButton)
        
        # BONZO LABEL
        self.bonzo_label = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bonzo_label.setFont(font)
        self.bonzo_label.setObjectName(_fromUtf8("bonzo_label"))
        self.verticalLayout.addWidget(self.bonzo_label)
        
        # AI FRAME
        self.AiFrame = QtGui.QFrame(self.centralwidget)
        self.AiFrame.setGeometry(QtCore.QRect(10, 640, 581, 31))
        self.AiFrame.setAutoFillBackground(True)
        self.AiFrame.setFrameShape(QtGui.QFrame.Box)
        self.AiFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.AiFrame.setObjectName(_fromUtf8("AiFrame"))
        self.Ai_label = QtGui.QLabel(self.AiFrame)
        self.Ai_label.setGeometry(QtCore.QRect(10, 4, 561, 20))
        self.Ai_label.setObjectName(_fromUtf8("label"))
        
        # RAISE
        self.CommandFrame.raise_()
        self.DiceFrame.raise_()
        self.board.raise_()
        self.SelectFrame.raise_()
        self.AiFrame.raise_()
        Main.setCentralWidget(self.centralwidget)
        self.retranslateMainUi(Main)
        # QtCore.QObject.connect(self.RollButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.updateDiceFrame((1,2,3,4)))
        # QtCore.QObject.connect(self.GoButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.board.update)
        # QtCore.QObject.connect(self.StopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.board.update)
        QtCore.QMetaObject.connectSlotsByName(Main)
    
    def retranslateMainUi(self, Main):
        """ This method translate all the text of the game in multiple languages """
        Main.setWindowTitle(_translate("Main", "Can\'t Stop", None))
        # SET BOTTOM LABEL VALUES
        for i in range(2, 13):
            self.bottom_label[i].setText(_translate("Main", str(i), None))
        # SET ROOT LABELS
        for i in range(2, 13):
            for y in range(self._route_len[i]):
                item = self.route[i].verticalHeaderItem(y)
                item.setText(_translate("Main", str(self._route_len[i] - y), None))
            item = self.route[i].horizontalHeaderItem(0)
            item.setText(_translate("Main", "1", None))
            __sortingEnabled = self.route[i].isSortingEnabled()
            self.route[i].setSortingEnabled(False)
            self.route[i].setSortingEnabled(__sortingEnabled)
        # SET TOP LABEL VALUES
        self.top_label[2].setText(_translate("Main", "C", None))
        self.top_label[3].setText(_translate("Main", "A", None))
        self.top_label[4].setText(_translate("Main", "N", None))
        self.top_label[5].setText(_translate("Main", "\'T", None))
        self.top_label[9].setText(_translate("Main", "S", None))
        self.top_label[10].setText(_translate("Main", "T", None))
        self.top_label[11].setText(_translate("Main", "O", None))
        self.top_label[12].setText(_translate("Main", "P", None))
        self.CommandTitle.setText(_translate("Main", "%s%s%s".format(Gui.head, 'Red', Gui.tail), None))
        self.SelectFrameTitle.setText(_translate("Main", "Choose route", None))
        for i in range(1, 7):
            self.checkBox[i].setText(_translate("Main", " ", None))
        
        self.GoButton.setText(_translate("Main", "GO!", None))
        self.bonzo_label.setText(_translate("Main", "Free: ", None))
    
    # SETUP SELECT WINDOW
    def SelectUi(self, SetupGame):
        SetupGame.setObjectName(_fromUtf8("SetupGame"))
        SetupGame.resize(428, 479)
        self.MainGridLayout = QtGui.QGridLayout(SetupGame)
        self.MainGridLayout.setObjectName(_fromUtf8("MainGridLayout"))
        self.MainFrame = QtGui.QFrame(SetupGame)
        self.MainFrame.setFrameShape(QtGui.QFrame.Box)
        self.MainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.MainFrame.setObjectName(_fromUtf8("MainFrame"))
        self.FrameGridLayout = QtGui.QGridLayout(self.MainFrame)
        self.FrameGridLayout.setObjectName(_fromUtf8("FrameGridLayout"))
        
        # SETUP FRAME 1
        self.frame[1] = self._frame(1)
        self.frame_title[1] = self._frame_title(self.frame[1], 1)
        self.layoutWidgetFrame1 = QtGui.QWidget(self.frame[1])
        self.layoutWidgetFrame1.setGeometry(QtCore.QRect(10, 30, 340, 20))
        self.layoutWidgetFrame1.setObjectName(_fromUtf8("layoutWidget_3"))
        self.P1_horizontalLayout = QtGui.QHBoxLayout(self.layoutWidgetFrame1)
        self.P1_horizontalLayout.setMargin(0)
        self.P1_horizontalLayout.setObjectName(_fromUtf8("P1_horizontalLayout"))
        self.radio_user[1] = self._radio_user(self.layoutWidgetFrame1, self.P1_horizontalLayout, 1)
        self.radio_cpu[1] = self._radio_cpu(self.layoutWidgetFrame1, self.P1_horizontalLayout, 1)
        self.combo_difficulty[1] = QtGui.QComboBox(self.layoutWidgetFrame1)
        self.combo_difficulty[1].addItem("Easy")
        self.combo_difficulty[1].addItem("Hard")
        self.P1_horizontalLayout.addWidget(self.combo_difficulty[1])
        self.radio_none[1] = self._radio_none(self.layoutWidgetFrame1, self.P1_horizontalLayout, 1)
        self.FrameGridLayout.addWidget(self.frame[1], 1, 0, 1, 1)
        
        # SETUP FRAME 2
        self.frame[2] = self._frame(2)
        self.frame_title[2] = self._frame_title(self.frame[2], 2)
        self.layoutWidgetFrame2 = QtGui.QWidget(self.frame[2])
        self.layoutWidgetFrame2.setGeometry(QtCore.QRect(10, 30, 340, 20))
        self.layoutWidgetFrame2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.P2_horizontalLayout = QtGui.QHBoxLayout(self.layoutWidgetFrame2)
        self.P2_horizontalLayout.setMargin(0)
        self.P2_horizontalLayout.setObjectName(_fromUtf8("P2_horizontalLayout"))
        self.radio_user[2] = self._radio_user(self.layoutWidgetFrame2, self.P2_horizontalLayout, 2)
        self.radio_cpu[2] = self._radio_cpu(self.layoutWidgetFrame2, self.P2_horizontalLayout, 2)
        self.combo_difficulty[2] = QtGui.QComboBox(self.layoutWidgetFrame2)
        self.combo_difficulty[2].addItem("Easy")
        self.combo_difficulty[2].addItem("Hard")
        self.P2_horizontalLayout.addWidget(self.combo_difficulty[2])
        self.radio_none[2] = self._radio_none(self.layoutWidgetFrame2, self.P2_horizontalLayout, 2)
        self.FrameGridLayout.addWidget(self.frame[2], 2, 0, 1, 1)
        self.MainGridLayout.addWidget(self.MainFrame, 0, 1, 1, 1)
        
        # SETUP FRAME 3
        self.frame[3] = self._frame(3)
        self.frame_title[3] = self._frame_title(self.frame[3], 3)
        self.layoutWidgetFrame3 = QtGui.QWidget(self.frame[3])
        self.layoutWidgetFrame3.setGeometry(QtCore.QRect(10, 30, 340, 20))
        self.layoutWidgetFrame3.setObjectName(_fromUtf8("layoutWidget1"))
        self.P3_horizontalLayout = QtGui.QHBoxLayout(self.layoutWidgetFrame3)
        self.P3_horizontalLayout.setMargin(0)
        self.P3_horizontalLayout.setObjectName(_fromUtf8("P3_horizontalLayout"))
        self.radio_user[3] = self._radio_user(self.layoutWidgetFrame3, self.P3_horizontalLayout, 3)
        self.radio_cpu[3] = self._radio_cpu(self.layoutWidgetFrame3, self.P3_horizontalLayout, 3)
        self.combo_difficulty[3] = QtGui.QComboBox(self.layoutWidgetFrame3)
        self.combo_difficulty[3].addItem("Easy")
        self.combo_difficulty[3].addItem("Hard")
        self.P3_horizontalLayout.addWidget(self.combo_difficulty[3])
        self.radio_none[3] = self._radio_none(self.layoutWidgetFrame3, self.P3_horizontalLayout, 3)
        self.FrameGridLayout.addWidget(self.frame[3], 3, 0, 1, 1)
        
        # SETUP FRAME 4
        self.frame[4] = self._frame(4)
        self.frame_title[4] = self._frame_title(self.frame[4], 4)
        self.layoutWidgetFrame4 = QtGui.QWidget(self.frame[4])
        self.layoutWidgetFrame4.setGeometry(QtCore.QRect(10, 30, 340, 20))
        self.layoutWidgetFrame4.setObjectName(_fromUtf8("layoutWidget"))
        self.P4_horizontalLayout = QtGui.QHBoxLayout(self.layoutWidgetFrame4)
        self.P4_horizontalLayout.setMargin(0)
        self.P4_horizontalLayout.setObjectName(_fromUtf8("P4_horizontalLayout"))
        self.radio_user[4] = self._radio_user(self.layoutWidgetFrame4, self.P4_horizontalLayout, 4)
        self.radio_cpu[4] = self._radio_cpu(self.layoutWidgetFrame4, self.P4_horizontalLayout, 4)
        self.combo_difficulty[4] = QtGui.QComboBox(self.layoutWidgetFrame4)
        self.combo_difficulty[4].addItem("Easy")
        self.combo_difficulty[4].addItem("Hard")
        self.P4_horizontalLayout.addWidget(self.combo_difficulty[4])
        self.radio_none[4] = self._radio_none(self.layoutWidgetFrame4, self.P4_horizontalLayout, 4)
        self.FrameGridLayout.addWidget(self.frame[4], 4, 0, 1, 1)
        
        # SETUP MAIN FRAME TITLE
        self.SetupTitle = QtGui.QLabel(self.MainFrame)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.SetupTitle.setFont(font)
        self.SetupTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.SetupTitle.setObjectName(_fromUtf8("SetupTitle"))
        # SETUP BUTTON
        self.ok_button = QtGui.QPushButton(self.MainFrame)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.FrameGridLayout.addWidget(self.ok_button, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.FrameGridLayout.addWidget(self.SetupTitle, 0, 0, 1, 1)
        
        self.retranslateSetupUi(SetupGame)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL(_fromUtf8("clicked()")), SetupGame.close)
        QtCore.QMetaObject.connectSlotsByName(SetupGame)
    
    def retranslateSetupUi(self, SetupGame):
        SetupGame.setWindowTitle(_translate("SetupGame", "Setup Game", None))
        self.frame_title[1].setText(_translate("SetupGame", "Player 1", None))
        self.radio_user[1].setText(_translate("SetupGame", "User", None))
        self.radio_cpu[1].setText(_translate("SetupGame", "CPU", None))
        self.radio_none[1].setText(_translate("SetupGame", "None", None))
        self.ok_button.setText(_translate("SetupGame", "OK", None))
        self.frame_title[4].setText(_translate("SetupGame", "Player 4", None))
        self.radio_user[4].setText(_translate("SetupGame", "User", None))
        self.radio_cpu[4].setText(_translate("SetupGame", "CPU", None))
        self.radio_none[4].setText(_translate("SetupGame", "None", None))
        self.SetupTitle.setText(_translate("SetupGame", "Select Players", None))
        self.frame_title[3].setText(_translate("SetupGame", "Player 3", None))
        self.radio_user[3].setText(_translate("SetupGame", "User", None))
        self.radio_cpu[3].setText(_translate("SetupGame", "CPU", None))
        self.radio_none[3].setText(_translate("SetupGame", "None", None))
        self.frame_title[2].setText(_translate("SetupGame", "Player 2", None))
        self.radio_user[2].setText(_translate("SetupGame", "User", None))
        self.radio_cpu[2].setText(_translate("SetupGame", "CPU", None))
        self.radio_none[2].setText(_translate("SetupGame", "None", None))
    
    def set_Error_Dialog(self, msg):
        self.error_msg.setText(_translate("Dialog", "{}".format(msg), None))