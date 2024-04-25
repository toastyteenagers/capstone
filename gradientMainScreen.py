import sys
import cv2
import face_recognition
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap, QImage
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url(:/images/images/Blue BG.png);")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 20, 991, 901))
        self.widget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.widget.setObjectName("widget")

        # QLabel for displaying the video frames
        self.cameraLabel = QtWidgets.QLabel(self.widget)
        self.cameraLabel.setGeometry(QtCore.QRect(250, 10, 480, 360))
        self.cameraLabel.setObjectName("cameraLabel")

        # First QLabel for displaying text
        self.textLabel = QtWidgets.QLabel(self.widget)
        self.textLabel.setGeometry(QtCore.QRect(250, 400, 480, 50))
        self.textLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.textLabel.setObjectName("textLabel")

        # Second QLabel for displaying additional text
        self.additionalTextLabel = QtWidgets.QLabel(self.widget)
        self.additionalTextLabel.setGeometry(QtCore.QRect(250, 460, 480, 50))
        self.additionalTextLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.additionalTextLabel.setText("BPM:")
        self.additionalTextLabel.setObjectName("additionalTextLabel")

        # QProgressBar for displaying progress
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setGeometry(QtCore.QRect(250, 520, 480, 30))
        self.progressBar.setMaximum(100)  # Set the maximum value of progress bar
        self.progressBar.setVisible(False)  # Initially hidden

        # Third QLabel for displaying final text
        self.finalTextLabel = QtWidgets.QLabel(self.widget)
        self.finalTextLabel.setGeometry(QtCore.QRect(250, 560, 480, 50))
        self.finalTextLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.finalTextLabel.setText("Access Granted") #DURESS DETECTED. ACCESS DENIED. or "Access Granted
        self.finalTextLabel.setVisible(False)  # Initially hidden

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Setup camera
        self.capture = cv2.VideoCapture(2)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        # Timer to show text after three seconds
        self.textTimer = QTimer()
        self.textTimer.singleShot(5000, self.show_text)

        # Timer to manage progress bar
        self.progressBarTimer = QTimer()
        self.progressBarTimer.timeout.connect(self.update_progress)
        self.progressBarTimer.start(100)

        self.progressValue = 0

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            face_locations = face_recognition.face_locations(frame)
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            p = convert_to_Qt_format.scaled(480, 360, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            self.cameraLabel.setPixmap(QPixmap.fromImage(p))

    def show_text(self):
        self.textLabel.setText("User: Roohan Amin")
        self.textLabel.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0, 0, 0, 0.5)")
        self.progressBar.setVisible(True)  # Show the progress bar when the text appears

    def update_progress(self):
        if self.progressBar.isVisible():
            if self.progressValue >= 100:
                self.progressBarTimer.stop()
                self.finalTextLabel.setVisible(True)
                self.additionalTextLabel.setText("BPM: 75")
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

# import sys
# import os
# import cv2
# import face_recognition
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import QTimer
# from PyQt5.QtGui import QPixmap, QImage
# import resources  # Assuming 'resources' is a valid resource file
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1920, 1080)
#         MainWindow.setStyleSheet("background-image: url(:/images/images/Blue BG.png);")
#
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#
#         self.widget = QtWidgets.QWidget(self.centralwidget)
#         self.widget.setGeometry(QtCore.QRect(480, 20, 991, 901))
#         self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.widget.setObjectName("widget")
#
#         # QLabel for displaying the video frames
#         self.cameraLabel = QtWidgets.QLabel(self.widget)
#         self.cameraLabel.setGeometry(QtCore.QRect(250, 10, 480, 360))
#         self.cameraLabel.setObjectName("cameraLabel")
#
#         # First QLabel for displaying text
#         self.textLabel = QtWidgets.QLabel(self.widget)
#         self.textLabel.setGeometry(QtCore.QRect(250, 400, 480, 50))
#         self.textLabel.setAlignment(QtCore.Qt.AlignCenter)
#         self.textLabel.setObjectName("textLabel")
#
#         # Second QLabel for displaying additional text
#         self.additionalTextLabel = QtWidgets.QLabel(self.widget)
#         self.additionalTextLabel.setGeometry(QtCore.QRect(250, 460, 480, 50))
#         self.additionalTextLabel.setAlignment(QtCore.Qt.AlignCenter)
#         self.additionalTextLabel.setText("BPM:")
#         self.additionalTextLabel.setObjectName("additionalTextLabel")
#
#         # QProgressBar for displaying progress
#         self.progressBar = QtWidgets.QProgressBar(self.widget)
#         self.progressBar.setGeometry(QtCore.QRect(250, 520, 480, 30))
#         self.progressBar.setMaximum(100)  # Set the maximum value of progress bar
#         self.progressBar.setVisible(False)  # Initially hidden
#
#         # Third QLabel for displaying final text
#         self.finalTextLabel = QtWidgets.QLabel(self.widget)
#         self.finalTextLabel.setGeometry(QtCore.QRect(250, 560, 480, 50))
#         self.finalTextLabel.setAlignment(QtCore.Qt.AlignCenter)
#         self.finalTextLabel.setText("Access Granted") # Or "DURESS DETECTED. ACCESS DENIED."
#         self.finalTextLabel.setVisible(False)  # Initially hidden
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)
#
#         # Setup camera
#         self.capture = cv2.VideoCapture(2)
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)
#
#         # Timer to show text after three seconds
#         self.textTimer = QTimer()
#         self.textTimer.singleShot(5000, self.show_text)
#
#         # Timer to manage progress bar
#         self.progressBarTimer = QTimer()
#         self.progressBarTimer.timeout.connect(self.update_progress)
#         self.progressBarTimer.start(100)
#
#         self.progressValue = 0
#
#     def update_frame(self):
#         ret, frame = self.capture.read()
#         if ret:
#             face_locations = face_recognition.face_locations(frame)
#             for (top, right, bottom, left) in face_locations:
#                 cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#             rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             h, w, ch = rgb_image.shape
#             bytes_per_line = ch * w
#             convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#             p = convert_to_Qt_format.scaled(480, 360, QtCore.Qt.KeepAspectRatio)
#             self.cameraLabel.setPixmap(QPixmap.fromImage(p))
#
#     def show_text(self):
#         self.textLabel.setText("User: Roohan Amin")
#         self.textLabel.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0, 0, 0, 0.5)")
#         self.progressBar.setVisible(True)  # Show the progress bar when the text appears
#
#     def update_progress(self):
#         if self.progressBar.isVisible():
#             if self.progressValue >= 100:
#                 self.progressBarTimer.stop()
#                 self.finalTextLabel.setVisible(True)
#                 self.additionalTextLabel.setText("BPM: 75")
#                 # Change background image of the MainWindow
#                 self.widget.parent().setStyleSheet("background-image: url(:/images/images/Green BG.png);")
#             else:
#                 self.progressValue += 1
#                 self.progressBar.setValue(self.progressValue)
#
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition Viewer"))
#
# if __name__ == "__main__":
#     os.environ["QT_QPA_PLATFORM"] = "xcb"
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())
