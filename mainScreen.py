from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtMultimedia import QCamera, QMediaCaptureSession
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_mainUserScreen(object):
    def __init__(self):
        self.viewfinder = None
        self.camera = None
        self.captureSession = QMediaCaptureSession()

    def setupUi(self, mainUserScreen):
        mainUserScreen.setObjectName("mainUserScreen")
        mainUserScreen.resize(1920, 1080)
        mainUserScreen.setStyleSheet("background: black")
        self.usernameLabel = QtWidgets.QLabel(parent=mainUserScreen)
        self.usernameLabel.setGeometry(QtCore.QRect(240, 560, 641, 41))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(28)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color: gray;")
        self.usernameLabel.setObjectName("usernameLabel")
        self.emotionLabel = QtWidgets.QLabel(parent=mainUserScreen)
        self.emotionLabel.setGeometry(QtCore.QRect(240, 630, 631, 41))
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(28)
        self.emotionLabel.setFont(font)
        self.emotionLabel.setStyleSheet("color: gray;")
        self.emotionLabel.setObjectName("emotionLabel")
        self.pushButton = QtWidgets.QPushButton(parent=mainUserScreen)
        self.pushButton.setGeometry(QtCore.QRect(250, 520, 75, 24))
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=mainUserScreen)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 520, 111, 24))
        self.pushButton_2.setStyleSheet("background-color: white;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=mainUserScreen)
        self.textEdit_2.setGeometry(QtCore.QRect(250, 440, 361, 71))
        self.textEdit_2.setStyleSheet("background-color: white;\n"
"color: black;\n"
"font: 36pt \"TI-92p Mini Sans\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.setupWebcam(mainUserScreen)

        self.retranslateUi(mainUserScreen)
        QtCore.QMetaObject.connectSlotsByName(mainUserScreen)
    def setupWebcam(self, parent):
        self.camera = QCamera()

        self.viewfinder = QVideoWidget(parent)
        self.viewfinder.setGeometry(QtCore.QRect(900, 20, 640, 480))  # Adjust as necessary

        self.captureSession.setCamera(self.camera)  # Set the camera for the session
        self.captureSession.setVideoOutput(self.viewfinder)  # Set the viewfinder as the video output

        self.viewfinder.show()

        self.camera.start()

    def retranslateUi(self, mainUserScreen):
        _translate = QtCore.QCoreApplication.translate
        mainUserScreen.setWindowTitle(_translate("mainUserScreen", "Form"))
        self.usernameLabel.setText(_translate("mainUserScreen", "User:"))
        self.emotionLabel.setText(_translate("mainUserScreen", "Detected Emotion: "))
        self.pushButton.setText(_translate("mainUserScreen", "Train Face"))
        self.pushButton_2.setText(_translate("mainUserScreen", "Recognize Face"))
        self.textEdit_2.setHtml(_translate("mainUserScreen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'TI-92p Mini Sans\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainUserScreen = QWidget()
    ui = Ui_mainUserScreen()
    ui.setupUi(mainUserScreen)
    mainUserScreen.show()
    sys.exit(app.exec())
