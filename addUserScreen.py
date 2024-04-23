from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QProgressBar
from PyQt6.QtCore import QTimer, QRect, Qt
from PyQt6 import QtGui
import cv2
import face_recognition
import numpy as np


class Ui_addUserScreen(object):
    def __init__(self):
        self.timer = QTimer()
        self.videoCapture = cv2.VideoCapture(2)
        self.frameLabel = None
        self.progressValue = 0

    def setupUi(self, addUserScreen):
        addUserScreen.setObjectName("mainUserScreen")
        addUserScreen.resize(1920, 1080)
        addUserScreen.setStyleSheet("background: black")
        self.setupLabels(addUserScreen)
        self.setupProgressBar(addUserScreen)
        self.setupButtons(addUserScreen)
        self.setupTextEdit(addUserScreen)
        self.setupWebcam(addUserScreen)

    def setupLabels(self, addUserScreen):
        font = QtGui.QFont()
        font.setFamily("TI-92p Mini Sans")
        font.setPointSize(28)

        self.usernameLabel = QLabel(parent=addUserScreen)
        self.usernameLabel.setGeometry(QRect(100, 100, 200, 50))
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color: white;")
        self.usernameLabel.setText("User:")

        self.emotionLabel = QLabel(parent=addUserScreen)
        self.emotionLabel.setGeometry(QRect(640, 630, 641, 41))
        self.emotionLabel.setFont(font)
        self.emotionLabel.setStyleSheet("color: gray;")
        self.emotionLabel.setText("BPM:")

    def setupTextEdit(self, addUserScreen):
        self.textEdit_2 = QTextEdit(parent=addUserScreen)
        self.textEdit_2.setGeometry(QRect(310, 100, 300, 50))  # Positioned next to the "User:" label
        self.textEdit_2.setStyleSheet("background-color: white; color: black; font: 18pt 'TI-92p Mini Sans';")
        self.textEdit_2.setPlaceholderText("Enter user name here")

    def setupProgressBar(self, addUserScreen):
        self.progressBar = QProgressBar(addUserScreen)
        self.progressBar.setGeometry(QRect(640, 680, 641, 30))
        self.progressBar.setMaximum(100)
        self.progressBar.setVisible(False)

        self.visibilityTimer = QTimer()
        self.visibilityTimer.setSingleShot(True)
        self.visibilityTimer.timeout.connect(self.makeProgressBarVisible)
        self.visibilityTimer.start(10000)

    def makeProgressBarVisible(self):
        self.progressBar.setVisible(True)
        self.loadingTimer = QTimer()
        self.loadingTimer.timeout.connect(self.updateProgressBar)
        self.loadingTimer.start(1000)

    def updateProgressBar(self):
        self.progressValue += 10
        self.progressBar.setValue(self.progressValue)
        if self.progressValue >= 100:
            self.loadingTimer.stop()
            self.emotionLabel.setText("BPM: 79")

    def setupButtons(self, addUserScreen):
        self.pushButton = QPushButton(parent=addUserScreen)
        self.pushButton.setGeometry(QRect(100, 160, 200, 50))
        self.pushButton.setStyleSheet("""
            background-color: #fff;
            border: 1px solid #000;
            border-radius: 4px;
            color: #000;
            padding: 12px 40px;
            font-family: Arial;
            font-size: 14px;
            font-weight: 400;
            line-height: 20px;
        """)
        self.pushButton.setText("Train Face")

        # self.pushButton_2 = QPushButton(parent=addUserScreen)
        # self.pushButton_2.setGeometry(QRect(310, 160, 200, 50))
        # self.pushButton_2.setStyleSheet("background-color: white;")
        # self.pushButton_2.setText("Recognize Face")

    def setupWebcam(self, addUserScreen):
        screenWidth = 1920
        webcamWidth = 640
        webcamHeight = 480
        webcamStartX = (screenWidth - webcamWidth) / 2

        self.frameLabel = QLabel(parent=addUserScreen)
        self.frameLabel.setGeometry(QRect(webcamStartX, 20, webcamWidth, webcamHeight))
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 ms

    def update_frame(self):
        ret, frame = self.videoCapture.read()
        if ret:
            # Resize frame for face recognition to improve performance
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            # Convert the image from BGR color (which OpenCV uses) to RGB color
            rgb_small_frame = small_frame[:, :, ::-1]

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)

            # Display the results
            for top, right, bottom, left in face_locations:
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Convert to Qt format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytesPerLine = ch * w
            convertToQtFormat = QtGui.QImage(frame.data, w, h, bytesPerLine, QtGui.QImage.Format.Format_RGB888)
            p = convertToQtFormat.scaled(self.frameLabel.width(), self.frameLabel.height(),
                                         Qt.AspectRatioMode.KeepAspectRatio)
            self.frameLabel.setPixmap(QtGui.QPixmap.fromImage(p))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    addUserScreen = QWidget()
    ui = Ui_addUserScreen()
    ui.setupUi(addUserScreen)
    addUserScreen.show()
    sys.exit(app.exec())
