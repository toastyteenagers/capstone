from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import numpy as np
from users import load_users, load_admins, delete_from_database, search_passwords

class passwordScreen(QWidget):
    def __init__(self):
        super(passwordScreen, self).__init__()
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle("Password Check")
        self.createUI()

    def createUI(self):
        self.layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.top_layout.setAlignment(Qt.AlignBottom)
        self.bottom_layout = QVBoxLayout()
        self.bottom_layout.setAlignment(Qt.AlignTop)

        self.passTxt = QLabel("Please enter your password: ")
        self.passBox = QLineEdit(self)
        self.top_layout.addWidget(self.passTxt)
        self.top_layout.addWidget(self.passBox)

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.checkPassword)
        self.bottom_layout.addWidget(self.submitButton)

        self.layout.addLayout(self.top_layout)
        self.layout.addLayout(self.bottom_layout)

        self.setLayout(self.layout)

    def checkPassword(self):
        password = self.passBox.text()
        if search_passwords(password):
            print("Pass!")
        else:
            print("Fail!")

def main():
    app = QApplication(sys.argv)
    window = passwordScreen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()