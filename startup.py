from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QPropertyAnimation
from PyQt6.QtWidgets import QGraphicsOpacityEffect
import resources_rc

class Ui_LoadScreen(object):
    def setupUi(self, LoadScreen):
        LoadScreen.setObjectName("LoadScreen")
        LoadScreen.resize(1317, 838)
        LoadScreen.setStyleSheet("background-color: black;")
        self.logo = QtWidgets.QTextBrowser(parent=LoadScreen)
        self.logo.setGeometry(QtCore.QRect(343, 40, 631, 321))
        self.logo.setMouseTracking(False)
        self.logo.setObjectName("logo")
        self.bc_bot = QtWidgets.QFrame(parent=LoadScreen)
        self.bc_bot.setGeometry(QtCore.QRect(340, 350, 661, 31))
        self.bc_bot.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bc_bot.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.bc_bot.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.bc_bot.setObjectName("bc_bot")
        self.bc_top = QtWidgets.QFrame(parent=LoadScreen)
        self.bc_top.setGeometry(QtCore.QRect(350, 10, 671, 31))
        self.bc_top.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.bc_top.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.bc_top.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.bc_top.setObjectName("bc_top")
        self.bc_left = QtWidgets.QFrame(parent=LoadScreen)
        self.bc_left.setGeometry(QtCore.QRect(330, 10, 31, 371))
        self.bc_left.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.bc_left.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.bc_left.setObjectName("bc_left")
        self.bc_right = QtWidgets.QFrame(parent=LoadScreen)
        self.bc_right.setGeometry(QtCore.QRect(970, 20, 31, 371))
        self.bc_right.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.bc_right.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.bc_right.setObjectName("bc_right")

        self.retranslateUi(LoadScreen)
        QtCore.QMetaObject.connectSlotsByName(LoadScreen)

    def playStartupSound(self):
        soundsPath = ("sounds", "startup_noise2.wav")
        filename = "/".join(soundsPath)

        # Create a class attribute to hold the QSoundEffect object
        self.startup_sound_effect = QSoundEffect()
        self.startup_sound_effect.setSource(QUrl.fromLocalFile(filename))

        # Adjust the volume
        self.startup_sound_effect.setVolume(0.25)

        # Adjust loop count to play the sound once
        self.startup_sound_effect.setLoopCount(1)

        self.startup_sound_effect.play()

    def retranslateUi(self, LoadScreen):
        _translate = QtCore.QCoreApplication.translate
        LoadScreen.setWindowTitle(_translate("LoadScreen", "Form"))
        self.logo.setHtml(_translate("LoadScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/images/project_backdown_ascii_art.jpg\" /></p></body></html>"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     LoadScreen = QtWidgets.QWidget()
#     ui = Ui_LoadScreen()
#     ui.setupUi(LoadScreen)
#     QtCore.QTimer.singleShot(1000, ui.playStartupSound)
#     LoadScreen.show()
#     sys.exit(app.exec())
#     #test edit for git again
