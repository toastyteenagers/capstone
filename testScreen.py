from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import numpy as np

class TestScreen(QtWidgets.QWidget):
    backClicked = QtCore.pyqtSignal()  # Signal to emit when back is clicked

    def __init__(self, ui_init_conf_main=None, parent=None):
        super(TestScreen, self).__init__(parent)
        self.ui_init_conf_main = ui_init_conf_main  # Assign the passed instance directly
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Test Screen")
        layout = QtWidgets.QVBoxLayout(self)

        # Label to indicate it's a test screen
        self.label = QtWidgets.QLabel("This is a Test Screen", self)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Button to go back to the main initial config screen
        self.backButton = QtWidgets.QPushButton("Back", self)
        self.backButton.clicked.connect(self.onBackClicked)
        layout.addWidget(self.backButton)

    def onBackClicked(self):
        self.backClicked.emit()  # Emit the signal when back button is clicked
        if isinstance(self.parent(), QtWidgets.QStackedWidget):
            self.parent().setCurrentIndex(2)  # Correct index must be used here
        self.ui_init_conf_main.incrementCount()  # Correctly refer to the passed instance method


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TestScreen()
    window.show()
    sys.exit(app.exec_())