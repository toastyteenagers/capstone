# Form implementation generated from reading ui file 'mainScreen.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1366, 869)
        Form.setStyleSheet("background: black")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(240, 560, 641, 41))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: gray;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setGeometry(QtCore.QRect(240, 630, 631, 41))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: gray;")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 520, 75, 24))
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 520, 111, 24))
        self.pushButton_2.setStyleSheet("background-color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=Form)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 450, 341, 61))
        self.textEdit_2.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font: 36pt \"TI-92p Mini Sans\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setGeometry(QtCore.QRect(700, 390, 641, 41))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: red;")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Recognized Face: Roohan"))
        self.label_4.setText(_translate("Form", "Detected Emotion: Fear"))
        self.pushButton.setText(_translate("Form", "Train Face"))
        self.pushButton_2.setText(_translate("Form", "Recognize Face"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'TI-92p Mini Sans\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("Form", "Duress Detected. Locked."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
