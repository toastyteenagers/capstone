from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys
import numpy as np

from startup import Ui_LoadScreen
from initialConfigScreenOne import Ui_InitConfScreenOneBG
from mainInitialConfigScreen import Ui_InitConfMain
from gradientMainScreen import Ui_gradientMainScreen
from testScreen import TestScreen
from addUser import AddUserScreen

from RHR_Analysis2 import RHR_Analysis_LIB

class MainApplication(QWidget):
    def __init__(self, RHR_Object):
        super(MainApplication, self).__init__()
        self.RHR_Object = RHR_Object
        self.initUI()

    def initUI(self):
        self.stack = QtWidgets.QStackedWidget()

        self.loadScreen = QtWidgets.QWidget()
        self.uiLoadScreen = Ui_LoadScreen()
        self.uiLoadScreen.setupUi(self.loadScreen)
        # self.uiLoadScreen.playStartupSound()
        self.stack.addWidget(self.loadScreen)

        # initial config screen one setup (the one with 'ok' button)
        self.initConfScreenOne = QtWidgets.QWidget()
        self.uiInitConfScreenOne = Ui_InitConfScreenOneBG()
        self.uiInitConfScreenOne.setupUi(self.initConfScreenOne)
        self.stack.addWidget(self.initConfScreenOne)

        # main initial config screen setup (the one with 'admin controls', 'add user', 'accessibility')
        self.mainInitConfScreen = QtWidgets.QWidget()
        self.uiMainInitConfScreen = Ui_InitConfMain(parent=self.mainInitConfScreen)
        self.uiMainInitConfScreen.setupUi(self.mainInitConfScreen)
        self.stack.addWidget(self.mainInitConfScreen)

        # Test screens setup (will change drastically)
        self.testScreenAdmin = TestScreen(self.uiMainInitConfScreen, self.stack)
        self.stack.addWidget(self.testScreenAdmin)
        self.testScreenUser = AddUserScreen(self.uiMainInitConfScreen, self.RHR_Object, self.stack)
        self.stack.addWidget(self.testScreenUser)
        self.testScreenAccessibility = TestScreen(self.uiMainInitConfScreen, self.stack)
        self.stack.addWidget(self.testScreenAccessibility)

        # gradient main screen setup (that must come from pressing 'proceed')
        self.gradientMainScreen = QtWidgets.QMainWindow()
        self.uiGradientMainScreen = Ui_gradientMainScreen(self.RHR_Object)
        self.uiGradientMainScreen.setupUi(self.gradientMainScreen)
        self.stack.addWidget(self.gradientMainScreen)

        # Set layout only once
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.stack)
        self.stack.setCurrentWidget(self.loadScreen)

        # Timer for automatic transition from load screen to initial config screen
        self.transitionTimer = QTimer(self)
        self.transitionTimer.setSingleShot(True)
        self.transitionTimer.timeout.connect(self.showInitConfScreen)
        self.transitionTimer.start(5000)  # 5 seconds to show load screen

        # Connect buttons to show test screens
        self.uiMainInitConfScreen.AdminControlsButton.clicked.connect(lambda: self.showTestScreen(3))
        self.uiMainInitConfScreen.AddUserButton.clicked.connect(lambda: self.showTestScreen(4))
        self.uiMainInitConfScreen.AccessibilityButton.clicked.connect(lambda: self.showTestScreen(5))
        #self.uiMainInitConfScreen.ProceedButton.clicked.connect(self.showGradientMainScreen)
        #self.uiMainInitConfScreen.ProceedButton.clicked.connect(lambda: self.showGradientMainScreen(6))

        # Connect the button in initial config screen one to trigger transition to the main initial config screen
        self.uiInitConfScreenOne.InitConfScreenOneButton.clicked.connect(self.showMainInitConfScreen)
        self.uiMainInitConfScreen.ProceedButton.clicked.connect(self.showGradientMainScreen)

    def showTestScreen(self, index):
        self.stack.setCurrentIndex(index)  # Use the index of the test screens

    def showInitConfScreen(self):
        self.stack.setCurrentWidget(self.initConfScreenOne)

    def showMainInitConfScreen(self):
        self.stack.setCurrentWidget(self.mainInitConfScreen)

    def showGradientMainScreen(self):
        self.stack.setCurrentWidget(self.gradientMainScreen)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    RHR_Analysis = RHR_Analysis_LIB()
    mainApp = MainApplication(RHR_Analysis)
    mainApp.showFullScreen()
    sys.exit(app.exec())
