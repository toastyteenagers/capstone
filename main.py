import sys
from PyQt6 import QtWidgets, QtCore
from startup import Ui_LoadScreen
from initialConfigScreenOne import Ui_InitConfScreenOne
from mainInitialConfigScreen import Ui_InitConfMain
from addUserScreen import Ui_addUserScreen
# from userlist import Ui_UserList

class System(QtWidgets.QWidget):
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
        self.setupAddUserScreen()

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
        self.ui_initConfMain.setupUi(self.initConfMain, self.stackedWidget)
        self.stackedWidget.addWidget(self.initConfMain)
        self.stackedWidget.setCurrentWidget(self.startupScreen)
    def showStartupScreen(self):
        self.stackedWidget.setCurrentWidget(self.startupScreen)
        QtCore.QTimer.singleShot(1000, self.ui_startup.playStartupSound)
        QtCore.QTimer.singleShot(5000, self.showInitialConfigScreen)

    def showInitialConfigScreen(self): # ok button screen
        self.stackedWidget.setCurrentWidget(self.initConfScreenOne)

    def showMainInitialConfigScreen(self): # first time set up steps
        self.stackedWidget.setCurrentWidget(self.initConfMain)

    def setupAddUserScreen(self): # second step
        self.addUserScreen = QtWidgets.QWidget()
        self.ui_addUserScreen = Ui_addUserScreen()
        self.ui_addUserScreen.setupUi(self.addUserScreen)
        self.stackedWidget.addWidget(self.addUserScreen)

    # def setupUserListScreen(self):
    #     self.userListScreen = Ui_UserList()
    #     self.stackedWidget.addWidget(self.userListScreen)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    programRun = System()
    programRun.showFullScreen()
    sys.exit(app.exec())
