from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import numpy as np

class HoverButton(QtWidgets.QPushButton):
    def __init__(self, default_text, hover_text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_text = default_text
        self.hover_text = hover_text
        self.setText(self.default_text)
        self.default_style = "color: white; font: 28pt 'TI-92p Mini Sans';"
        self.hover_style = self.default_style + "text-decoration: underline;"
        self.setStyleSheet(self.default_style)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.setText(self.hover_text)
        self.setStyleSheet(self.hover_style)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setText(self.default_text)
        self.setStyleSheet(self.default_style)
class Ui_InitConfMain(object):
    def __init__(self, parent=None, stackedWidget=None):
        self.parent = parent
        self.stackedWidget = stackedWidget
        self.counter = 0
        self.counterLabel = QtWidgets.QLabel("0/3", parent=self.parent)
        self.counterLabel.setGeometry(QtCore.QRect((1920-200)//1, ((1080-50)//1) - 60, 200, 52))
        self.counterLabel.setStyleSheet("color: white; font: 48pt 'TI-92p Mini Sans';")
        self.counterLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setupUi(parent)
    def setupUi(self, InitConfMain):
        InitConfMain.setObjectName("InitConfMain")
        InitConfMain.resize(1920, 1080)
        InitConfMain.setStyleSheet("background-color: black;")
        self.topRightLine = QtWidgets.QFrame(parent=InitConfMain)
        self.topRightLine.setGeometry(QtCore.QRect(1290, 30, 621, 21))
        self.topRightLine.setStyleSheet("background-color: gray;")
        self.topRightLine.setFrameShape(QFrame.HLine)
        self.topRightLine.setFrameShadow(QFrame.Sunken)
        self.topRightLine.setObjectName("topRightLine")
        self.bottomLine = QtWidgets.QFrame(parent=InitConfMain)
        self.bottomLine.setGeometry(QtCore.QRect(10, 1020, 1901, 21))
        self.bottomLine.setStyleSheet("background-color: gray;")
        self.bottomLine.setFrameShape(QFrame.HLine)
        self.bottomLine.setFrameShadow(QFrame.Sunken)
        self.bottomLine.setObjectName("bottomLine")
        self.rightLine = QtWidgets.QFrame(parent=InitConfMain)
        self.rightLine.setGeometry(QtCore.QRect(1890, 30, 21, 1011))
        self.rightLine.setStyleSheet("background-color: gray")
        self.rightLine.setFrameShape(QFrame.VLine)
        self.rightLine.setFrameShadow(QFrame.Sunken)
        self.rightLine.setObjectName("rightLine")
        self.leftLine = QtWidgets.QFrame(parent=InitConfMain)
        self.leftLine.setGeometry(QtCore.QRect(10, 30, 21, 1011))
        self.leftLine.setStyleSheet("background-color: gray")
        self.leftLine.setFrameShape(QFrame.VLine)
        self.leftLine.setFrameShadow(QFrame.Sunken)
        self.leftLine.setObjectName("leftLine")
        self.topLeftLine = QtWidgets.QFrame(parent=InitConfMain)
        self.topLeftLine.setGeometry(QtCore.QRect(10, 30, 621, 21))
        self.topLeftLine.setStyleSheet("background-color: gray;")
        self.topLeftLine.setFrameShape(QFrame.HLine)
        self.topLeftLine.setFrameShadow(QFrame.Sunken)
        self.topLeftLine.setObjectName("topLeftLine")
        self.InitConfTitle = QtWidgets.QLabel(parent=InitConfMain)
        self.InitConfTitle.setGeometry(QtCore.QRect(640, 10, 651, 51))
        font = QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(36)
        self.InitConfTitle.setFont(font)
        self.InitConfTitle.setStyleSheet("color: gray;")
        self.InitConfTitle.setObjectName("InitConfTitle")
        self.AdminControlsButton = HoverButton("- Admin Controls", "Admin Controls", parent=InitConfMain)
        self.AdminControlsButton.setGeometry(QtCore.QRect(90, 80, 321, 41))
        #self.AdminControlsButton.setStyleSheet("color: white;\n""font: 28pt \"TI-92p Mini Sans\";")
        #self.AdminControlsButton.setObjectName("AdminControlsButton")
        self.AddUserButton = HoverButton("- Add User", "Add User", parent=InitConfMain)
        self.AddUserButton.setGeometry(QtCore.QRect(90, 160, 201, 41))
        # self.AddUserButton.setStyleSheet("color: white;\n""font: 28pt \"TI-92p Mini Sans\";")
        # self.AddUserButton.setObjectName("AddUserButton")
        self.AccessibilityButton = HoverButton("- Accessibility", "Accessibility", parent=InitConfMain)
        self.AccessibilityButton.setGeometry(QtCore.QRect(90, 240, 261, 41))
        # test counter label
        self.counterLabel = QtWidgets.QLabel(parent=InitConfMain)
        self.counterLabel.setGeometry(QtCore.QRect((1920-200)//1, ((1080-50)//1) - 60, 200, 52))  # Centering the label
        self.counterLabel.setText("0/3")
        self.counterLabel.setStyleSheet("color: white; font: 48pt 'TI-92p Mini Sans';")
        self.counterLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.counterLabel.setObjectName("counterLabel")

        self.counter = 0

        # test hidden proceed button
        self.ProceedButton = QtWidgets.QPushButton(parent=InitConfMain)
        self.ProceedButton.setGeometry(QtCore.QRect((1920-200)//2, 1080-120, 200, 50))
        self.ProceedButton.setText("Proceed")
        self.ProceedButton.setStyleSheet("""background-color: #fff;
            border: 1px solid #000;
            border-radius: 4px;
            color: #000;
            padding: 12px 40px;
            font-family: Arial;
            font-size: 14px;
            font-weight: 400;
            line-height: 20px;""")
        self.ProceedButton.setObjectName("ProceedButton")
        self.ProceedButton.hide()
        # self.AccessibilityButton.setStyleSheet("color: white;\n""font: 28pt \"TI-92p Mini Sans\";")
        # self.AccessibilityButton.setObjectName("AccessibilityButton")
        self.topLeftLine.raise_()
        self.topRightLine.raise_()
        self.bottomLine.raise_()
        self.rightLine.raise_()
        self.leftLine.raise_()
        self.InitConfTitle.raise_()
        self.AdminControlsButton.raise_()
        self.AddUserButton.raise_()
        self.AccessibilityButton.raise_()

        self.retranslateUi(InitConfMain)
        QtCore.QMetaObject.connectSlotsByName(InitConfMain)

    def goToAdminControlsScreen(self):
        currentIndex = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def goToAddUserScreen(self):
        currentIndex = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def goToAccessibilityScreen(self):
        currentIndex = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def toggleProceedButton(self):
        if self.ProceedButton.isHidden():
            self.ProceedButton.show()
        else:
            self.ProceedButton.hide()

    def goToGradientMainScreen(self):
        currentIndex = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def incrementCount(self):
        if self.counter < 3:
            self.counter += 1
            self.counterLabel.setText(f'{self.counter}/3')

            if self.counter == 3:
                self.toggleProceedButton()

    def retranslateUi(self, InitConfMain):
        _translate = QtCore.QCoreApplication.translate
        InitConfMain.setWindowTitle(_translate("InitConfMain", "Form"))
        self.InitConfTitle.setText(_translate("InitConfMain", "First Time Setup Sequence"))
        self.AdminControlsButton.setText(_translate("InitConfMain", "- Admin Controls"))
        self.AddUserButton.setText(_translate("InitConfMain", "- Add User"))
        self.AccessibilityButton.setText(_translate("InitConfMain", "- Accessibility"))
        self.ProceedButton.setText(_translate("InitConfMain", "Proceed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InitConfMain = QtWidgets.QWidget()
    ui = Ui_InitConfMain()
    ui.setupUi(InitConfMain)
    InitConfMain.showFullScreen()
    InitConfMain.show()
    sys.exit(app.exec())