import sys
from PyQt6 import QtWidgets, QtCore
from startup import Ui_LoadScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoadScreen = QtWidgets.QWidget()
    ui = Ui_LoadScreen()
    ui.setupUi(LoadScreen)
    QtCore.QTimer.singleShot(1000, ui.playStartupSound)
    LoadScreen.show()
    sys.exit(app.exec())
    #test edit for git again