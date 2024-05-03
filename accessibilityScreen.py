from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Accessibility(object):
    def setupUi(self, Accessibility):
        Accessibility.setObjectName("Accessibility")
        Accessibility.resize(1920, 1080)
        Accessibility.setStyleSheet("background-color: black;")
        self.topRightLine = QtWidgets.QFrame(Accessibility)
        self.topRightLine.setGeometry(QtCore.QRect(1290, 30, 621, 21))
        self.topRightLine.setStyleSheet("background-color: gray;")
        self.topRightLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topRightLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topRightLine.setObjectName("topRightLine")
        self.bottomLine = QtWidgets.QFrame(Accessibility)
        self.bottomLine.setGeometry(QtCore.QRect(10, 1020, 1901, 21))
        self.bottomLine.setStyleSheet("background-color: gray;")
        self.bottomLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottomLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottomLine.setObjectName("bottomLine")
        self.rightLine = QtWidgets.QFrame(Accessibility)
        self.rightLine.setGeometry(QtCore.QRect(1890, 30, 21, 1011))
        self.rightLine.setStyleSheet("background-color: gray")
        self.rightLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.rightLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.rightLine.setObjectName("rightLine")
        self.leftLine = QtWidgets.QFrame(Accessibility)
        self.leftLine.setGeometry(QtCore.QRect(10, 30, 21, 1011))
        self.leftLine.setStyleSheet("background-color: gray")
        self.leftLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.leftLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.leftLine.setObjectName("leftLine")
        self.topLeftLine = QtWidgets.QFrame(Accessibility)
        self.topLeftLine.setGeometry(QtCore.QRect(10, 30, 621, 21))
        self.topLeftLine.setStyleSheet("background-color: gray;")
        self.topLeftLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topLeftLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLeftLine.setObjectName("topLeftLine")
        self.InitConfTitle = QtWidgets.QLabel(Accessibility)
        self.InitConfTitle.setGeometry(QtCore.QRect(640, 10, 651, 51))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(36)
        self.InitConfTitle.setFont(font)
        self.InitConfTitle.setStyleSheet("color: gray;")
        self.InitConfTitle.setObjectName("InitConfTitle")
        self.checkBox = QtWidgets.QCheckBox(Accessibility)
        self.checkBox.setGeometry(QtCore.QRect(80, 110, 661, 61))
        self.checkBox.setStyleSheet("color: white;\n"
"font:  18pt \'TI-92p Mini Sans\';\n"
"background-color: gray;")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Accessibility)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 210, 661, 61))
        self.checkBox_2.setStyleSheet("color: white;\n"
"font:  18pt \'TI-92p Mini Sans\';\n"
"background-color: gray;")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Accessibility)
        self.checkBox_3.setGeometry(QtCore.QRect(80, 310, 661, 61))
        self.checkBox_3.setStyleSheet("color: white;\n"
"font:  18pt \'TI-92p Mini Sans\';\n"
"background-color: gray;")
        self.checkBox_3.setObjectName("checkBox_3")
        self.InitConfScreenOneButton = QtWidgets.QPushButton(Accessibility)
        self.InitConfScreenOneButton.setGeometry(QtCore.QRect(900, 650, 151, 61))
        self.InitConfScreenOneButton.setStyleSheet("background: white;\n"
"font: 12pt \"TI-92p Mini Sans\";")
        self.InitConfScreenOneButton.setObjectName("InitConfScreenOneButton")
        self.topLeftLine.raise_()
        self.topRightLine.raise_()
        self.bottomLine.raise_()
        self.rightLine.raise_()
        self.leftLine.raise_()
        self.InitConfTitle.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.InitConfScreenOneButton.raise_()

        self.retranslateUi(Accessibility)
        QtCore.QMetaObject.connectSlotsByName(Accessibility)

    def retranslateUi(self, Accessibility):
        _translate = QtCore.QCoreApplication.translate
        Accessibility.setWindowTitle(_translate("Accessibility", "Form"))
        self.InitConfTitle.setText(_translate("Accessibility", "First Time Setup Sequence"))
        self.checkBox.setText(_translate("Accessibility", "Enable Screen Reader"))
        self.checkBox_2.setText(_translate("Accessibility", "High Contrast Mode"))
        self.checkBox_3.setText(_translate("Accessibility", "Heart Rate Deviation Adjustment"))
        self.InitConfScreenOneButton.setText(_translate("Accessibility", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accessibility = QtWidgets.QWidget()
    ui = Ui_Accessibility()
    ui.setupUi(Accessibility)
    Accessibility.show()
    sys.exit(app.exec_())
