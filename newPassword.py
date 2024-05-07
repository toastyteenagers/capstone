from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import subprocess
import numpy as np
from users import load_users, load_admins, delete_from_database, search_passwords

class passwordScreen(QWidget):
    def __init__(self, parent=None):
        super(passwordScreen, self).__init__(parent)

        self.name = ""

        QFontDatabase.addApplicationFont('/Users/owenboxx/Documents/School/Capstone/database/TI-92p Mini Sans Normal.ttf')
        self.font = QFont("Ti-92p Mini Sans")
        self.font.setLetterSpacing(0,90)

        self.createUI()

    def loop(self):
        self.clock = QTimer(self)
        #self.clock.timeout.connect(self.check)
        #self.clock.start()

    def createUI(self):
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle("Password Check")

        self.titleText = QLabel("Enter your full name and password",self)
        self.titleText.setStyleSheet("QLabel{font-size: 70pt; color: white;}")
        self.titleText.setFont(self.font)
        self.titleText.setGeometry(245,180,1500,80)

        self.passwordPrompt = QLabel("Please enter your name and password below",self)
        self.passwordPrompt.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
        self.passwordPrompt.setFont(self.font)
        self.passwordPrompt.setGeometry(430,710,1500,80)

        self.nameText = QLabel("Full Name:",self)
        self.nameText.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.nameText.setFont(self.font)
        self.nameText.setGeometry(640,800,1500,80)
        self.nameBox = QLineEdit(self)
        self.nameBox.setGeometry(845,815,455,40)

        self.passwordTxt = QLabel("Enter Password:",self)
        self.passwordTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.passwordTxt.setFont(self.font)
        self.passwordTxt.setGeometry(640,880,1500,80)
        self.passwordBox = QLineEdit(self)
        self.passwordBox.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordBox.setGeometry(940,895,360,40)

        self.enterButton = QPushButton("Enter",self)
        self.enterButton.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.enterButton.setFont(self.font)
        self.enterButton.setGeometry(640,960,665,40)
        self.enterButton.clicked.connect(self.checkPassword)

        self.incorrectTxt = QLabel("The name or password is incorrect",self)
        self.incorrectTxt.setStyleSheet("QLabel{font-size: 30pt; color: red;}")
        self.incorrectTxt.setFont(self.font)
        self.incorrectTxt.setGeometry(655,1000,2000,40)
        self.incorrectTxt.setVisible(False)

    def checkPassword(self):
        password = self.passwordBox.text()
        name = self.nameBox.text()
        if search_passwords(password,name):
            subprocess.Popen([sys.executable, 'adminControlScreen.py'])
            sys.exit()
        else:
            self.incorrectTxt.setVisible(True)

    def paintEvent(self, e):

        icon = QPainter(self)
        icon.setPen(QPen(Qt.white, 5, Qt.SolidLine))
        icon.drawEllipse(780,280,360,360)
        icon.drawArc(860,460,200,320,150,2560)
        icon.drawEllipse(900,340,120,120)

        painter = QPainter(self)
        painter.setPen(QPen(QColor(0,0,0,100),10,Qt.SolidLine))
        painter.setBrush(QColor(255,255,255,20))
        painter.drawRoundedRect(384,690,1152,360,20,20)
        #painter.drawRect(640,800,640,200)

        #painter.drawElipse()

stylesheet = """
    passwordScreen {
        background-color: #41454f;
        background-repeat: no-repeat;
        background-position: center;
    }
"""


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = passwordScreen()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
