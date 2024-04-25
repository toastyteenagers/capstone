from PyQt6 import QtCore, QtGui, QtWidgets
import sys

from startup import Ui_LoadScreen
from initialConfigScreenOne import Ui_InitConfScreenOneBG
from mainInitialConfigScreen import Ui_InitConfMain
from testScreen import TestScreen

class MainApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.stack = QtWidgets.QStackedWidget()  # Stacked widget to manage screens

        # Loading screen setup
        self.loadScreen = QtWidgets.QWidget()
        self.uiLoadScreen = Ui_LoadScreen()
        self.uiLoadScreen.setupUi(self.loadScreen)
        self.uiLoadScreen.playStartupSound()
        self.stack.addWidget(self.loadScreen)

        # Initial configuration screen setup
        self.initConfScreenOne = QtWidgets.QWidget()
        self.uiInitConfScreenOne = Ui_InitConfScreenOneBG()
        self.uiInitConfScreenOne.setupUi(self.initConfScreenOne)
        self.stack.addWidget(self.initConfScreenOne)

        # Main initial configuration screen setup
        self.mainInitConfScreen = QtWidgets.QWidget()
        self.uiMainInitConfScreen = Ui_InitConfMain()
        self.uiMainInitConfScreen.setupUi(self.mainInitConfScreen)
        self.stack.addWidget(self.mainInitConfScreen)

        # Test screens setup
        self.testScreenAdmin = TestScreen(self.stack)
        self.stack.addWidget(self.testScreenAdmin)
        self.testScreenUser = TestScreen(self.stack)
        self.stack.addWidget(self.testScreenUser)
        self.testScreenAccessibility = TestScreen(self.stack)
        self.stack.addWidget(self.testScreenAccessibility)

        # Set layout only once
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.stack)
        self.stack.setCurrentWidget(self.loadScreen)

        # Timer for automatic transition from load screen to initial config screen
        self.transitionTimer = QtCore.QTimer(self)
        self.transitionTimer.setSingleShot(True)
        self.transitionTimer.timeout.connect(self.showInitConfScreen)
        self.transitionTimer.start(5000)  # 5 seconds to show load screen

        # Connect buttons to show test screens
        self.uiMainInitConfScreen.AdminControlsButton.clicked.connect(lambda: self.showTestScreen(3))
        self.uiMainInitConfScreen.AddUserButton.clicked.connect(lambda: self.showTestScreen(4))
        self.uiMainInitConfScreen.AccessibilityButton.clicked.connect(lambda: self.showTestScreen(5))

        # Connect the button in initial config screen one to trigger transition to the main initial config screen
        self.uiInitConfScreenOne.InitConfScreenOneButton.clicked.connect(self.showMainInitConfScreen)

    def showTestScreen(self, index):
        self.stack.setCurrentIndex(index)  # Use the index of the test screens

    def showInitConfScreen(self):
        self.stack.setCurrentWidget(self.initConfScreenOne)

    def showMainInitConfScreen(self):
        self.stack.setCurrentWidget(self.mainInitConfScreen)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainApp = MainApplication()
    mainApp.showFullScreen()
    sys.exit(app.exec())
