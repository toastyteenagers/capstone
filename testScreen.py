import sys
from PyQt6 import QtCore, QtGui, QtWidgets

class TestScreen(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TestScreen, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Test Screen")
        layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("This is a Test Screen", self)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # back button
        self.backButton = QtWidgets.QPushButton("Back", self)
        self.backButton.clicked.connect(self.on_back_clicked)
        layout.addWidget(self.backButton)

    def on_back_clicked(self):
        if isinstance(self.parent(), QtWidgets.QStackedWidget):
            self.parent().setCurrentIndex(2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TestScreen()
    window.show()
    sys.exit(app.exec())
