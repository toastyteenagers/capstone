from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
import sys
import resources
import numpy as np

class Ui_LoadScreen(object):
    def __init__(self):
        self.opacityEffect = None
        self.fadeInAnimation = None
        self.logo = None

    def setupUi(self, LoadScreen):
        LoadScreen.setObjectName("LoadScreen")
        LoadScreen.resize(1317, 838)
        LoadScreen.setStyleSheet("background-color: black;")
        self.logo = QtWidgets.QTextBrowser(parent=LoadScreen)
        self.logo.setGeometry(QRect(649, 20, 621, 341))
        self.logo.setMouseTracking(False)
        self.logo.setStyleSheet("border: none;")
        self.logo.setObjectName("logo")

        self.opacityEffect = QGraphicsOpacityEffect(self.logo)
        self.logo.setGraphicsEffect(self.opacityEffect)

        # Set up QPropertyAnimation for the opacity effect
        self.fadeInAnimation = QPropertyAnimation(self.opacityEffect, b"opacity")
        self.fadeInAnimation.setDuration(5000)  # Duration in milliseconds
        self.fadeInAnimation.setStartValue(0)  # Start fully transparent
        self.fadeInAnimation.setEndValue(1)  # End fully opaque
        self.fadeInAnimation.setEasingCurve(QEasingCurve.InOutQuad)  # Smooth transition
        self.fadeInAnimation.start()

        self.retranslateUi(LoadScreen)
        QMetaObject.connectSlotsByName(LoadScreen)

    def retranslateUi(self, LoadScreen):
        _translate = QCoreApplication.translate
        LoadScreen.setWindowTitle(_translate("LoadScreen", "Form"))
        self.logo.setHtml(_translate("LoadScreen",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "hr { height: 1px; border-width: 0; }\n"
                                     "li.unchecked::marker { content: \"\\2610\"; }\n"
                                     "li.checked::marker { content: \"\\2612\"; }\n"
                                     "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/images/project_backdown_logo_centered.jpg\" /></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadScreen = QtWidgets.QWidget()
    ui = Ui_LoadScreen()
    ui.setupUi(LoadScreen)
    LoadScreen.showFullScreen()
    LoadScreen.show()
    sys.exit(app.exec_())
