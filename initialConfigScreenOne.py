from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InitConfScreenOneBG(object):
    def setupUi(self, InitConfScreenOneBG):
        InitConfScreenOneBG.setObjectName("InitConfScreenOneBG")
        InitConfScreenOneBG.resize(1920, 1080)
        InitConfScreenOneBG.setStyleSheet("background-color: black;")
        self.topRightLine = QtWidgets.QFrame(parent=InitConfScreenOneBG)
        self.topRightLine.setGeometry(QtCore.QRect(1290, 30, 621, 21))
        self.topRightLine.setStyleSheet("background-color: gray;")
        self.topRightLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.topRightLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.topRightLine.setObjectName("topRightLine")
        self.bottomLine = QtWidgets.QFrame(parent=InitConfScreenOneBG)
        self.bottomLine.setGeometry(QtCore.QRect(10, 1020, 1901, 21))
        self.bottomLine.setStyleSheet("background-color: gray;")
        self.bottomLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.bottomLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.bottomLine.setObjectName("bottomLine")
        self.rightLine = QtWidgets.QFrame(parent=InitConfScreenOneBG)
        self.rightLine.setGeometry(QtCore.QRect(1890, 30, 21, 1011))
        self.rightLine.setStyleSheet("background-color: gray")
        self.rightLine.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.rightLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.rightLine.setObjectName("rightLine")
        self.leftLine = QtWidgets.QFrame(parent=InitConfScreenOneBG)
        self.leftLine.setGeometry(QtCore.QRect(10, 30, 21, 1011))
        self.leftLine.setStyleSheet("background-color: gray")
        self.leftLine.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.leftLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.leftLine.setObjectName("leftLine")
        self.topLeftLine = QtWidgets.QFrame(parent=InitConfScreenOneBG)
        self.topLeftLine.setGeometry(QtCore.QRect(10, 30, 621, 21))
        self.topLeftLine.setStyleSheet("background-color: gray;")
        self.topLeftLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.topLeftLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.topLeftLine.setObjectName("topLeftLine")
        self.InitConfTitle = QtWidgets.QLabel(parent=InitConfScreenOneBG)
        self.InitConfTitle.setGeometry(QtCore.QRect(640, 10, 651, 51))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(36)
        self.InitConfTitle.setFont(font)
        self.InitConfTitle.setStyleSheet("color: gray;")
        self.InitConfTitle.setObjectName("InitConfTitle")
        self.WelcomeLOne = QtWidgets.QLabel(parent=InitConfScreenOneBG)
        self.WelcomeLOne.setGeometry(QtCore.QRect(370, 110, 1101, 71))
        self.WelcomeLOne.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLOne.setObjectName("WelcomeLOne")
        self.WelcomeLTwo = QtWidgets.QLabel(parent=InitConfScreenOneBG)
        self.WelcomeLTwo.setGeometry(QtCore.QRect(380, 190, 1071, 71))
        self.WelcomeLTwo.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLTwo.setObjectName("WelcomeLTwo")
        self.WelcomeLThree = QtWidgets.QLabel(parent=InitConfScreenOneBG)
        self.WelcomeLThree.setGeometry(QtCore.QRect(360, 270, 1151, 71))
        self.WelcomeLThree.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLThree.setObjectName("WelcomeLThree")
        self.InitConfScreenOneButton = QtWidgets.QPushButton(parent=InitConfScreenOneBG)
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
    sys.exit(app.exec())
