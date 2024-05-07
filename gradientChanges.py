import sys
import cv2
import face_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import asyncio

import resources
import users


class Ui_gradientMainScreen(QWidget):

    def __init__(self, parent=None):
        super(Ui_gradientMainScreen, self).__init__(parent)

        self.name = None
        self.rhr = None
        self.status = "Waiting to Start..."
        self.clicked1 = False
        self.clicked2 = False

        QFontDatabase.addApplicationFont(
            '/Users/owenboxx/Documents/School/Capstone/database/TI-92p Mini Sans Normal.ttf')
        self.font = QFont("Ti-92p Mini Sans")
        self.font.setLetterSpacing(0, 90)

        self.createUI()
        self.start_camera()

    def createUI(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Main Screen")

        self.cameraLabel = QLabel(self)
        self.cameraLabel.setGeometry(QtCore.QRect(660, 120, 600, 450))
        self.cameraLabel.setObjectName("cameraLabel")
        self.cameraLabel.setStyleSheet("border: 8px solid white")

        self.nameLabel = QLabel("Name:", self)
        self.nameLabel.setGeometry(390, 580, 634, 80)
        self.nameLabel.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.nameLabel.setFont(self.font)

        self.nameTxt = QLabel(self.name, self)
        self.nameTxt.setGeometry(500, 580, 634, 80)
        self.nameTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.nameTxt.setFont(self.font)

        self.rhrLabel = QLabel("Heart Rate:", self)
        self.rhrLabel.setGeometry(390, 660, 634, 80)
        self.rhrLabel.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.rhrLabel.setFont(self.font)

        self.rhrTxt = QLabel(self.rhr, self)
        self.rhrTxt.setGeometry(600, 660, 634, 80)
        self.rhrTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.rhrTxt.setFont(self.font)

        self.statusLabel = QLabel("Status:", self)
        self.statusLabel.setGeometry(390, 740, 634, 80)
        self.statusLabel.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.statusLabel.setFont(self.font)

        self.statusTxt = QLabel("", self)
        self.statusTxt.setGeometry(530, 740, 634, 80)
        self.statusTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.statusTxt.setFont(self.font)

        self.clickFace = QLabel("Click Here\nto scan your\nface", self)
        self.clickFace.setAlignment(Qt.AlignCenter)
        self.clickFace.setGeometry(417, 145, 200, 100)
        self.clickFace.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
        self.clickFace.setFont(self.font)

        self.firstStep = QLabel("1", self)
        self.firstStep.setGeometry(495, 275, 150, 150)
        self.firstStep.setStyleSheet("QLabel{font-size: 80pt; color: white;}")
        self.firstStep.setFont(self.font)

        self.analyze = QPushButton(self)
        self.analyze.clicked.connect(self.recognize_from_camera)
        self.analyze.setGeometry(445, 270, 150, 150)
        self.analyze.setStyleSheet("background-color: white")
        self.analyze.setStyleSheet("background-color: transparent")

        self.clickrhr = QLabel("Click Here\nto scan your\nheart rate", self)
        self.clickrhr.setAlignment(Qt.AlignCenter)
        self.clickrhr.setGeometry(1295, 145, 200, 100)
        self.clickrhr.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
        self.clickrhr.setFont(self.font)

        self.secondStep = QLabel("2", self)
        self.secondStep.setGeometry(1373, 275, 150, 150)
        self.secondStep.setStyleSheet("QLabel{font-size: 80pt; color: white;}")
        self.secondStep.setFont(self.font)

        self.analyzeRhr = QPushButton(self)
        self.analyzeRhr.clicked.connect(self.testFunc)
        self.analyzeRhr.setGeometry(1325, 270, 150, 150)
        self.analyzeRhr.setStyleSheet("background-color: white")
        self.analyzeRhr.setStyleSheet("background-color: transparent")

        self.show()

    def updateFunctions(self):
        self.update_frame()
        if self.rhr is not None:
            self.rhrTxt.setText(str(self.rhr))
        if self.name is not None:
            self.nameTxt.setText(self.name)
        if self.status is not "Waiting to Start...":
            self.statusTxt.setText(self.status)

        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        # 10
        # painter.setPen(QPen(QColor(0,0,0,150), 10, Qt.SolidLine))
        painter.setPen(QPen(QColor(255, 255, 255, 150), 1, Qt.SolidLine))

        painter.drawLine(0, 540, 1920, 540)
        painter.drawLine(960, 0, 960, 1080)

        painter.setBrush(QColor(0, 0, 0, 100))
        painter.drawRoundedRect(380, 100, 1160, 880, 20, 20)

        # in button press
        button1 = QPainter(self)
        if self.clicked1:
            self.firstStep.setStyleSheet("QLabel{font-size: 80pt; color: gray;}")
            self.clickFace.setStyleSheet("QLabel{font-size: 25pt; color: gray;}")
            button1.setPen(QPen(QColor(255, 255, 255, 100), 7, Qt.SolidLine))
        else:
            self.firstStep.setStyleSheet("QLabel{font-size: 80pt; color: white;}")
            self.clickFace.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
            button1.setPen(QPen(QColor(255, 255, 255, 255), 7, Qt.SolidLine))
        button1.drawEllipse(445, 270, 150, 150)

        button2 = QPainter(self)
        if self.clicked2:
            # self.analyzeRhr.setEnabled(False)
            self.secondStep.setStyleSheet("QLabel{font-size: 80pt; color: gray;}")
            self.clickrhr.setStyleSheet("QLabel{font-size: 25pt; color: gray;}")
            button2.setPen(QPen(QColor(255, 255, 255, 100), 7, Qt.SolidLine))
        else:
            button2.setPen(QPen(QColor(255, 255, 255, 255), 7, Qt.SolidLine))
            # self.analyzeRhr.setEnabled(True)
            self.secondStep.setStyleSheet("QLabel{font-size: 80pt; color: white;}")
            self.clickrhr.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
        button2.drawEllipse(1325, 270, 150, 150)

    def testFunc(self):
        self.clicked2 = True

    def recognize_from_camera(self):
        self.clicked1 = True

        print(self.rhr, self.status)
        self.rhr = 80
        self.status = 'Processing'
        self.name = "Owen"

    def loop(self):
        self.clock = QTimer(self)
        self.clock.timeout.connect(self.updateFunctions)
        self.clock.start()

    def start_camera(self):
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        self.loop()

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)  # Flip the frame horizontally
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(800, 600, QtCore.Qt.KeepAspectRatio)
            self.cameraLabel.setPixmap(QPixmap.fromImage(p))

    def switch(self, index):
        if index == 0:
            app.setStyleSheet(stylesheet2)
        elif index == 1:
            app.setStyleSheet(stylesheet3)
        elif index == 2:
            app.setStyleSheet(stylesheet)


stylesheet = """
    Ui_gradientMainScreen {
        background-color: #182e8f;
        background-repeat: no-repeat;
        background-position: center;
    }
"""

stylesheet2 = """
    Ui_gradientMainScreen {
        background-color: #ff0000;
        background-repeat: no-repeat;
        background-position: center;
    }
"""

stylesheet3 = """
    Ui_gradientMainScreen {
        background-color: #00ff00;
        background-repeat: no-repeat;
        background-position: center;
    }
"""


def main():
    global app
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = Ui_gradientMainScreen()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
