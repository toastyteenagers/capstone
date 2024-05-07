import sys
import cv2
import face_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import asyncio
import threading
import subprocess
import resources
#from RHR_Analysis2 import RHR_Analysis_LIB
#RHR_Analysis = RHR_Analysis_LIB()
#import DoorControl
import users


class Ui_gradientMainScreen(QWidget):

    def __init__(self, parent=None):
        super(Ui_gradientMainScreen, self).__init__(parent)

        self.name = None
        self.rhr = None
        self.status = "Waiting to Start..."
        self.recognizedUser = None
        self.RHR_Analysis = RHR_Object

        QFontDatabase.addApplicationFont(
            '/Users/owenboxx/Documents/School/Capstone/database/TI-92p Mini Sans Normal.ttf')
        self.font = QFont("Ti-92p Mini Sans")
        self.font.setLetterSpacing(0, 90)

        self.createUI()
        self.start_camera()

    def add_hr(self):
        if self.rhr is None or self.name is None:
            self.status = "Processing"

        beatList = self.RHR_Analysis.sample()
        rhr = self.RHR_Analysis.analysis(beatList)
        print(rhr)
        self.rhr = rhr
        self.checkOpen()
        if self.recognizedUser is not None:
            print("Recognized User: " + self.recognizedUser.get_first_name())
            print("recognized user's RHR:'" + str(self.recognizedUser.get_rhr()))
            print("Duress? : " + str(self.RHR_Analysis.analyze(self.recognizedUser.get_rhr(), rhr)))
        return rhr

    def checkOpen(self):
        print("checking if open: ")
        print("username:")
        if self.name == None:
            print("name is none")
        else:
            print(self.name)
        print("rhr:")
        if (self.rhr is None):
            print("rhr is none")
        else:
            print(self.rhr)
        if (self.rhr is not None and self.name is not None):
            self.RHR_Analysis.OpenFor5()
            print("AUTHORIZED")
            self.status = "Authorized"
            self.rhr = None
            self.name = None
            self.recognizedUser = None

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

        self.analyze = QPushButton(self)
        self.analyze.clicked.connect(self.recognize_from_camera)
        self.analyze.setGeometry(445, 270, 150, 150)
        self.analyze.setStyleSheet("background-color: white")
        # self.analyze.setStyleSheet("background-color: transparent")

        self.analyzeRhr = QPushButton(self)
        self.analyzeRhr.clicked.connect(self.recognize_from_camera)
        self.analyzeRhr.setGeometry(1325, 270, 150, 150)
        self.analyzeRhr.setStyleSheet("background-color: white")
        # self.analyze.setStyleSheet("background-color: transparent")

        self.show()

    def updateFunctions(self):
        self.update_frame()
        if self.rhr is not None:
            self.rhrTxt.setText(str(self.rhr))
        else:
            self.rhrTxt.setText("")
        if self.name is not None:
            self.nameTxt.setText(self.name)
        else:
            self.nameTxt.setText("")
        if self.status is not "Waiting to Start...":
            self.statusTxt.setText(self.status)
        else:
            self.statusTxt.setText("")

    def paintEvent(self, e):
        painter = QPainter(self)
        # 10
        # painter.setPen(QPen(QColor(0,0,0,150), 10, Qt.SolidLine))
        painter.setPen(QPen(QColor(255, 255, 255, 150), 1, Qt.SolidLine))

        painter.drawLine(0, 540, 1920, 540)
        painter.drawLine(960, 0, 960, 1080)

        painter.setBrush(QColor(0, 0, 0, 100))
        painter.drawRoundedRect(380, 100, 1160, 880, 20, 20)

    def recognize_from_camera(self):
        if self.rhr is None or self.name is None:
            self.status = "Processing"

        userList = users.load_users()
        self.known_face_encodings = []
        self.known_face_names = []  # Update with known user names
        for user in userList:
            self.known_face_encodings.append(user.get_encodings())
            self.known_face_names.append(user.name)
        # Get a frame from the camera
        frame = self.get_camera_frame()

        # Convert from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Assuming that each frame has one face for simplicity
        if face_encodings:
            # Use the first found face encoding
            face_encoding_to_check = face_encodings[0]

            # Check each known face encoding against the one detected
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding_to_check)
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding_to_check)

            best_match_index = None
            if matches:
                best_match_index = face_distances.argmin()

            if best_match_index is not None and matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                print(name)
                # self.recognizedUser = users.search_database(face_encoding_to_check)
                self.name = name
                self.nameTxt.setText(name)
                self.checkOpen()
                return name
            else:
                self.nameTxt.setText("Not Recognized")
                print("user not found")

        return None

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

    def get_camera_frame(self):
        cap = self.capture
        if not cap.isOpened():
            print("Error: Camera could not be accessed.")
            return None
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            return None
        return frame

    def makeGreen(self):
        app.setStyleSheet(stylesheet3)

    def makeBlue(self):
        app.setStyleSheet(stylesheet)

    def makeRed(self):
        app.setStyleSheet(stylesheet2)


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
