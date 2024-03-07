from PyQt6 import QtCore, QtGui, QtWidgets


class HoverButton(QtWidgets.QPushButton):
    def __init__(self, default_text, hover_text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_text = default_text
        self.hover_text = hover_text
        # Set the default text initially
        self.setText(self.default_text)
        # Default style
        self.default_style = "color: white; font: 28pt 'TI-92p Mini Sans';"
        # Hover style with underline
        self.hover_style = self.default_style + " text-decoration: underline;"
        # Apply the default style initially
        self.setStyleSheet(self.default_style)

    def enterEvent(self, event):
        super().enterEvent(event)
        # Change the text and apply the hover style on hover
        self.setText(self.hover_text)
        self.setStyleSheet(self.hover_style)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        # Revert to the default text and style when not hovered
        self.setText(self.default_text)
        self.setStyleSheet(self.default_style)
class Ui_InitConfMain(object):
    def setupUi(self, InitConfMain, stackedWidget):
        InitConfMain.setObjectName("InitConfMain")
        InitConfMain.resize(1920, 1080)
        InitConfMain.setStyleSheet("background-color: black;")
        self.stackedWidget = stackedWidget
        self.line_5 = QtWidgets.QFrame(parent=InitConfMain)
        self.line_5.setGeometry(QtCore.QRect(1400, 10, 511, 21))
        self.line_5.setStyleSheet("background-color: gray;")
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_4 = QtWidgets.QFrame(parent=InitConfMain)
        self.line_4.setGeometry(QtCore.QRect(10, 1020, 1901, 21))
        self.line_4.setStyleSheet("background-color: gray;")
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QtWidgets.QFrame(parent=InitConfMain)
        self.line_3.setGeometry(QtCore.QRect(1890, 10, 21, 1031))
        self.line_3.setStyleSheet("background-color: gray")
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_2 = QtWidgets.QFrame(parent=InitConfMain)
        self.line_2.setGeometry(QtCore.QRect(10, 10, 21, 1031))
        self.line_2.setStyleSheet("background-color: gray")
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(parent=InitConfMain)
        self.line.setGeometry(QtCore.QRect(10, 10, 521, 21))
        self.line.setStyleSheet("background-color: gray;")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(parent=InitConfMain)
        self.label.setGeometry(QtCore.QRect(550, 10, 831, 51))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setStyleSheet("color: gray;")
        self.label.setObjectName("label")

        self.AdminControlsButton = HoverButton("- Admin Controls", "> Admin Controls", parent=InitConfMain)
        self.AdminControlsButton.setGeometry(QtCore.QRect(80, 80, 431, 41))
        self.AdminControlsButton.setObjectName("AdminControlsButton")

        self.AddUserButton = HoverButton("- Add User", "> Add User", parent=InitConfMain)
        self.AddUserButton.setGeometry(QtCore.QRect(80, 160, 281, 41))
        self.AddUserButton.setObjectName("AddUserButton")

        self.AccessiblilityButton = HoverButton("- Accessibility", "> Accessibility", parent=InitConfMain)
        self.AccessiblilityButton.setGeometry(QtCore.QRect(80, 240, 411, 41))
        self.AccessiblilityButton.setObjectName("AccessibilityButton")

        self.line.raise_()
        self.line_5.raise_()
        self.line_4.raise_()
        self.line_3.raise_()
        self.line_2.raise_()
        self.label.raise_()
        self.AdminControlsButton.raise_()

        self.AddUserButton.raise_()
        self.AddUserButton.clicked.connect(self.goToAddUserScreen)
        self.AccessiblilityButton.raise_()
        #self.InitConfScreenOneButton = QtWidgets.QPushButton(parent=InitConfMain)

        self.retranslateUi(InitConfMain)
        QtCore.QMetaObject.connectSlotsByName(InitConfMain)
        #self.button.clicked.connect(self.goToInitConfMain)

    def goToAddUserScreen(self):
        currentIndex = self.stackedWidget.currentIndex()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)

    def retranslateUi(self, InitConfMain):
        _translate = QtCore.QCoreApplication.translate
        InitConfMain.setWindowTitle(_translate("InitConfMain", "Form"))
        self.label.setText(_translate("InitConfMain", "First Time Setup Sequence"))
        self.AdminControlsButton.setText(_translate("InitConfMain", "- Admin Controls"))
        self.AddUserButton.setText(_translate("InitConfMain", "- Add User"))
        self.AccessiblilityButton.setText(_translate("InitConfMain", "- Accessibility"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     InitConfMain = QtWidgets.QWidget()
#     ui = Ui_InitConfMain()
#     ui.setupUi(InitConfMain)
#     InitConfMain.show()
#     sys.exit(app.exec())
