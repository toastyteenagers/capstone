from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import numpy as np

class Ui_InitConfScreenOneBG(object):
    def setupUi(self, InitConfScreenOneBG):
        InitConfScreenOneBG.setObjectName("InitConfScreenOneBG")
        InitConfScreenOneBG.resize(1920, 1080)
        InitConfScreenOneBG.setStyleSheet("background-color: black;")

        self.topRightLine = QFrame(parent=InitConfScreenOneBG)
        self.topRightLine.setGeometry(QtCore.QRect(1290, 30, 621, 21))
        self.topRightLine.setStyleSheet("background-color: gray;")
        self.topRightLine.setFrameShape(QFrame.HLine)
        self.topRightLine.setFrameShadow(QFrame.Sunken)
        self.topRightLine.setObjectName("topRightLine")

        self.bottomLine = QFrame(parent=InitConfScreenOneBG)
        self.bottomLine.setGeometry(QtCore.QRect(10, 1020, 1901, 21))
        self.bottomLine.setStyleSheet("background-color: gray;")
        self.bottomLine.setFrameShape(QFrame.HLine)
        self.bottomLine.setFrameShadow(QFrame.Sunken)
        self.bottomLine.setObjectName("bottomLine")

        self.rightLine = QFrame(parent=InitConfScreenOneBG)
        self.rightLine.setGeometry(QtCore.QRect(1890, 30, 21, 1011))
        self.rightLine.setStyleSheet("background-color: gray")
        self.rightLine.setFrameShape(QFrame.VLine)
        self.rightLine.setFrameShadow(QFrame.Sunken)
        self.rightLine.setObjectName("rightLine")

        self.leftLine = QFrame(parent=InitConfScreenOneBG)
        self.leftLine.setGeometry(QtCore.QRect(10, 30, 21, 1011))
        self.leftLine.setStyleSheet("background-color: gray")
        self.leftLine.setFrameShape(QFrame.VLine)
        self.leftLine.setFrameShadow(QFrame.Sunken)
        self.leftLine.setObjectName("leftLine")

        self.topLeftLine = QFrame(parent=InitConfScreenOneBG)
        self.topLeftLine.setGeometry(QtCore.QRect(10, 30, 621, 21))
        self.topLeftLine.setStyleSheet("background-color: gray;")
        self.topLeftLine.setFrameShape(QFrame.HLine)
        self.topLeftLine.setFrameShadow(QFrame.Sunken)
        self.topLeftLine.setObjectName("topLeftLine")

        self.InitConfTitle = QLabel(parent=InitConfScreenOneBG)
        self.InitConfTitle.setGeometry(QtCore.QRect(640, 10, 651, 51))

        font = QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(36)

        self.InitConfTitle.setFont(font)
        self.InitConfTitle.setStyleSheet("color: gray;")
        self.InitConfTitle.setObjectName("InitConfTitle")

        self.WelcomeLOne = QLabel(parent=InitConfScreenOneBG)
        self.WelcomeLOne.setGeometry(QtCore.QRect(370, 110, 1101, 71))
        self.WelcomeLOne.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLOne.setObjectName("WelcomeLOne")
        self.WelcomeLTwo = QLabel(parent=InitConfScreenOneBG)
        self.WelcomeLTwo.setGeometry(QtCore.QRect(380, 190, 1071, 71))
        self.WelcomeLTwo.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLTwo.setObjectName("WelcomeLTwo")
        self.WelcomeLThree = QLabel(parent=InitConfScreenOneBG)
        self.WelcomeLThree.setGeometry(QtCore.QRect(360, 270, 1151, 71))
        self.WelcomeLThree.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLThree.setObjectName("WelcomeLThree")
        self.InitConfScreenOneButton = QPushButton(parent=InitConfScreenOneBG)
        self.InitConfScreenOneButton.setGeometry(QtCore.QRect(884, 650, 151, 61))
        self.InitConfScreenOneButton.setStyleSheet("          background-color: #fff;\n"
"        border: 1px solid #000;\n"
"        border-radius: 4px;\n"
"        color: #000;\n"
"        padding: 12px 40px;\n"
"        font-family: Arial;\n"
"        font-size: 14px;\n"
"        font-weight: 400;\n"
"        line-height: 20px;")
        self.InitConfScreenOneButton.setObjectName("InitConfScreenOneButton")
        self.topLeftLine.raise_()
        self.topRightLine.raise_()
        self.bottomLine.raise_()
        self.rightLine.raise_()
        self.leftLine.raise_()
        self.InitConfTitle.raise_()
        self.WelcomeLOne.raise_()
        self.WelcomeLTwo.raise_()
        self.WelcomeLThree.raise_()
        self.InitConfScreenOneButton.raise_()

        self.retranslateUi(InitConfScreenOneBG)
        QtCore.QMetaObject.connectSlotsByName(InitConfScreenOneBG)

    def retranslateUi(self, InitConfScreenOneBG):
        _translate = QtCore.QCoreApplication.translate
        InitConfScreenOneBG.setWindowTitle(_translate("InitConfScreenOneBG", "Form"))
        self.InitConfTitle.setText(_translate("InitConfScreenOneBG", "First Time Setup Sequence"))
        self.WelcomeLOne.setText(_translate("InitConfScreenOneBG", "Welcome to the Project Backdown Initial Setup and Configuration Wizard."))
        self.WelcomeLTwo.setText(_translate("InitConfScreenOneBG", "To start, please complete admin account setup. You will be required to"))
        self.WelcomeLThree.setText(_translate("InitConfScreenOneBG", "input biometric data, user information, and your system configuration needs."))
        self.InitConfScreenOneButton.setText(_translate("InitConfScreenOneBG", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InitConfScreenOneBG = QtWidgets.QMainWindow()
    ui = Ui_InitConfScreenOneBG()
    ui.setupUi(InitConfScreenOneBG)
    InitConfScreenOneBG.showFullScreen()
    InitConfScreenOneBG.show()
    sys.exit(app.exec_())