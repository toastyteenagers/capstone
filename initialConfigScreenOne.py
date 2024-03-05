from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QStackedWidget


class Ui_InitConfScreenOne(object):
    def setupUi(self, InitConfScreenOne, stackedWidget):
        InitConfScreenOne.setObjectName("Form")
        InitConfScreenOne.resize(1920, 1080)
        InitConfScreenOne.setStyleSheet("background-color: black;")
        self.stackedWidget = stackedWidget
        self.line_5 = QtWidgets.QFrame(parent=InitConfScreenOne)
        self.line_5.setGeometry(QtCore.QRect(1400, 10, 511, 21))
        self.line_5.setStyleSheet("background-color: gray;")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_4 = QtWidgets.QFrame(parent=InitConfScreenOne)
        self.line_4.setGeometry(QtCore.QRect(10, 1020, 1901, 21))
        self.line_4.setStyleSheet("background-color: gray;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(parent=InitConfScreenOne)
        self.line_3.setGeometry(QtCore.QRect(1890, 10, 21, 1031))
        self.line_3.setStyleSheet("background-color: gray")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(parent=InitConfScreenOne)
        self.line_2.setGeometry(QtCore.QRect(10, 10, 21, 1031))
        self.line_2.setStyleSheet("background-color: gray")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(parent=InitConfScreenOne)
        self.line.setGeometry(QtCore.QRect(10, 10, 521, 21))
        self.line.setStyleSheet("background-color: gray;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.InitConfTitle = QtWidgets.QLabel(parent=InitConfScreenOne)
        self.InitConfTitle.setGeometry(QtCore.QRect(550, 10, 831, 51))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(36)
        self.InitConfTitle.setFont(font)
        self.InitConfTitle.setStyleSheet("color: gray;")
        self.InitConfTitle.setObjectName("InitConfTitle")
        self.WelcomeLOne = QtWidgets.QLabel(parent=InitConfScreenOne)
        self.WelcomeLOne.setGeometry(QtCore.QRect(530, 110, 861, 71))
        self.WelcomeLOne.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLOne.setObjectName("WelcomeLOne")
        self.WelcomeLTwo = QtWidgets.QLabel(parent=InitConfScreenOne)
        self.WelcomeLTwo.setGeometry(QtCore.QRect(550, 190, 831, 71))
        self.WelcomeLTwo.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLTwo.setObjectName("WelcomeLTwo")
        self.WelcomeLThree = QtWidgets.QLabel(parent=InitConfScreenOne)
        self.WelcomeLThree.setGeometry(QtCore.QRect(520, 270, 891, 71))
        self.WelcomeLThree.setStyleSheet("color: white;\n"
"font: 24pt, \"TI-92p Mini Sans\"")
        self.WelcomeLThree.setObjectName("WelcomeLThree")
        self.InitConfScreenOneButton = QtWidgets.QPushButton(parent=InitConfScreenOne)
        self.InitConfScreenOneButton.setGeometry(QtCore.QRect(900, 650, 151, 61))
        self.InitConfScreenOneButton.setStyleSheet("background: white;\n"
"font: 12pt \"TI-92p Mini Sans\";")
        self.InitConfScreenOneButton.setObjectName("InitConfScreenOneButton")
        self.line.raise_()
        self.line_5.raise_()
        self.line_4.raise_()
        self.line_3.raise_()
        self.line_2.raise_()
        self.InitConfTitle.raise_()
        self.WelcomeLOne.raise_()
        self.WelcomeLTwo.raise_()
        self.WelcomeLThree.raise_()
        self.InitConfScreenOneButton.raise_()
        self.InitConfScreenOneButton.clicked.connect(self.goToInitConfMain)
        self.retranslateUi(InitConfScreenOne)
        QtCore.QMetaObject.connectSlotsByName(InitConfScreenOne)

    def goToInitConfMain(self):
        currentIndex = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.InitConfTitle.setText(_translate("Form", "First Time Setup Sequence"))
        self.WelcomeLOne.setText(_translate("Form", "Welcome to the Project Backdown Initial Setup and Configuration Wizard."))
        self.WelcomeLTwo.setText(_translate("Form", "To start, please complete admin account setup. You will be required to"))
        self.WelcomeLThree.setText(_translate("Form", "input biometric data, user information, and your system configuration needs."))
        self.InitConfScreenOneButton.setText(_translate("Form", "OK"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec())
