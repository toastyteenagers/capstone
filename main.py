import sys
from PyQt6 import QtWidgets
from ui_startup import Ui_LoadScreen

app = QtWidgets.QApplication(sys.argv)

window = Ui_LoadScreen()
window.show()

app.exec()