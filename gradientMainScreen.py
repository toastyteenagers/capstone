import sys
import cv2
import face_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
import asyncio

import resources
#import RHR_Analysis
#import DoorControl
import users

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        userList = users.load_users()
        self.known_face_encodings = []
        self.known_face_names = []  # Update with known user names
        for user in userList:
            print(user.name)
            self.known_face_encodings.append(face_recognition.face_encodings(user))
            self.known_face_names.append(user.name)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url(:/images/images/Blue BG.png);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 20, 991, 901))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")

        self.cameraLabel = QtWidgets.QLabel(self.widget)
        self.cameraLabel.setGeometry(QtCore.QRect(250, 10, 480, 360))
        self.cameraLabel.setObjectName("cameraLabel")

        self.textLabel = QtWidgets.QLabel(self.widget)
        self.textLabel.setGeometry(QtCore.QRect(250, 400, 480, 50))
        self.textLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel.setObjectName("textLabel")

        self.additionalTextLabel = QtWidgets.QLabel(self.widget)
        self.additionalTextLabel.setGeometry(QtCore.QRect(250, 460, 480, 50))
        self.additionalTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.additionalTextLabel.setText("BPM:")
        self.additionalTextLabel.setObjectName("additionalTextLabel")

        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(250, 520, 480, 30))
        self.progressBar.setMaximum(100)
        self.progressBar.setVisible(False)

        self.finalTextLabel = QtWidgets.QLabel(self.widget)
        self.finalTextLabel.setGeometry(QtCore.QRect(250, 560, 480, 50))
        self.finalTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.finalTextLabel.setText("Access Granted")
        self.finalTextLabel.setVisible(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Setup camera
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start()

        # Timer to manage progress bar
        self.progressBarTimer = QTimer()
        self.progressBarTimer.timeout.connect(self.update_progress)
        self.progressBarTimer.start(100)

        self.progressValue = 0

        # Setup status bar timer
        self.statusBarTimer = QTimer()
        self.statusBarTimer.timeout.connect(self.show_status_bar_message)
        self.statusBarTimer.start(10000)

        # Start asynchronous function to retrieve BPM value
        loop = asyncio.get_event_loop()
        loop.create_task(self.retrieve_bpm())

    async def retrieve_bpm(self):
        # Simulating asynchronous task to retrieve BPM value
        #bpm_value = await RHR_Analysis.sample()  # Simulate some asynchronous operation
        bpm_value = -1
        # Update the BPM field with the retrieved value
        self.additionalTextLabel.setText(f"BPM: {bpm_value}")

    def show_status_bar_message(self):
        # Display status bar message for 10 seconds
        self.statusbar.showMessage("Status: Ready", 10000)

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # Find all face locations in the frame
            face_locations = face_recognition.face_locations(frame)

            # Iterate through each face found in the frame
            for (top, right, bottom, left) in face_locations:
                # Draw a rectangle around each face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Check if known face encodings are available
                if self.known_face_encodings:
                    # Crop the face from the frame
                    face_image = frame[top:bottom, left:right]

                    # Encode the face
                    face_encodings = face_recognition.face_encodings(face_image)

                    # Compare face encodings with known face encodings
                    for face_encoding in face_encodings:
                        # Compare the current face encoding with known face encodings
                        matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)

                        # Check if any match is found
                        if True in matches:
                            # Find the index of the first match
                            first_match_index = matches.index(True)

                            # Get the corresponding known face name
                            name = self.known_face_names[first_match_index]

                            # Display the name of the recognized user on the frame
                            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                                        (255, 255, 255), 1)
                            if (RHR_Analysis.analyze(users.search_database(face_encoding))):
                                self.textLabel.setText("Access Granted")
                                #needs to show nice access granted and display rhr, as well as opening door.
                                DoorControl.OpenFor5()

            # Convert the frame to QImage format and display it in the cameraLabel
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(480, 360, QtCore.Qt.KeepAspectRatio)
            self.cameraLabel.setPixmap(QPixmap.fromImage(p))

    def show_text(self, name):
        self.textLabel.setText("User: "+name)
        self.textLabel.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0, 0, 0, 0.5)")
        self.progressBar.setVisible(True)  # Show the progress bar when the text appears

    def update_progress(self, bpm=-1):
        if self.progressBar.isVisible():
            if self.progressValue >= 100:
                self.progressBarTimer.stop()
                self.finalTextLabel.setVisible(True)
                self.additionalTextLabel.setText("BPM: "+bpm)
                # Change background image of the MainWindow
                self.widget.parent().setStyleSheet("background-image: url(:/images/images/Green BG.png);")
            else:
                self.progressValue += 1
                self.progressBar.setValue(self.progressValue)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition Viewer"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())