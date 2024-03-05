# import sys
# from PyQt6 import QtWidgets, QtCore
# from startup import Ui_LoadScreen
# from initialConfigScreenOne import Ui_InitConfScreenOne
# from mainInitialConfigScreen import Ui_InitConfMain
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#
#     LoadScreen = QtWidgets.QWidget()
#     ui = Ui_LoadScreen()
#     ui.setupUi(LoadScreen)
#     LoadScreen.showFullScreen()
#     QtCore.QTimer.singleShot(1000, ui.playStartupSound)
#     LoadScreen.show()
#
#     stackedWidget = QtWidgets.QStackedWidget()
#     InitConfScreenOne = QtWidgets.QWidget()
#     ui_screen_one = Ui_InitConfScreenOne()
#     ui_screen_one.setupUi(InitConfScreenOne, stackedWidget)
#
#     InitConfMain = QtWidgets.QWidget()
#     ui_init_conf_main = Ui_InitConfMain()
#     ui_init_conf_main.setupUi(InitConfMain)
#
#     stackedWidget.addWidget(InitConfScreenOne)
#     stackedWidget.addWidget(InitConfMain)
#     stackedWidget.showFullScreen()
#
#     sys.exit(app.exec())

import sys
from PyQt6 import QtWidgets, QtCore
from startup import Ui_LoadScreen  # Assume this has the startup screen and sound
from initialConfigScreenOne import Ui_InitConfScreenOne
from mainInitialConfigScreen import Ui_InitConfMain


class MainApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.stackedWidget = QtWidgets.QStackedWidget()

        self.stackedWidget.setStyleSheet("border: none;")
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.stackedWidget)

        self.setupStartupScreen()
        self.setupInitialConfigScreen()
        self.setupMainInitialConfigScreen()

        self.showStartupScreen()

    def setupStartupScreen(self):
        self.startupScreen = QtWidgets.QWidget()
        self.ui_startup = Ui_LoadScreen()
        self.ui_startup.setupUi(self.startupScreen)
        self.stackedWidget.addWidget(self.startupScreen)

    def setupInitialConfigScreen(self):
        self.initConfScreenOne = QtWidgets.QWidget()
        self.ui_initConfScreenOne = Ui_InitConfScreenOne()
        self.ui_initConfScreenOne.setupUi(self.initConfScreenOne, self.stackedWidget)
        self.stackedWidget.addWidget(self.initConfScreenOne)
    def setupMainInitialConfigScreen(self):
        self.initConfMain = QtWidgets.QWidget()
        self.ui_initConfMain = Ui_InitConfMain()
        # Assuming Ui_InitConfMain doesn't need stackedWidget for setup
        self.ui_initConfMain.setupUi(self.initConfMain)
        self.stackedWidget.addWidget(self.initConfMain)
    def showStartupScreen(self):
        self.stackedWidget.setCurrentWidget(self.startupScreen)
        # Assume playStartupSound is a method in Ui_LoadScreen to play the sound
        QtCore.QTimer.singleShot(1000, self.ui_startup.playStartupSound)
        # Transition to the next screen after some delay
        QtCore.QTimer.singleShot(5000, self.showInitialConfigScreen)  # Adjust delay as needed

    def showInitialConfigScreen(self):
        self.stackedWidget.setCurrentWidget(self.initConfScreenOne)

    def showMainInitialConfigScreen(self):
        self.stackedWidget.setCurrentWidget(self.initConfMain)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainApp = MainApplication()
    mainApp.showFullScreen()
    sys.exit(app.exec())
