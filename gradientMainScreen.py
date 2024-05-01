import sys
import cv2
import face_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
import asyncio

import resources
#from RHR_Analysis2 import RHR_Analysis_LIB
#RHR_Analysis = RHR_Analysis_LIB()
#import DoorControl
import users

class Ui_gradientMainScreen(object):
    
    def __init__(self, RHR_Object, parent=None):
        #super(Ui_gradientMainScreen,self).__init__(parent)
        #self.ui_init_conf_main = ui_init_conf_main
        self.RHR_Analysis = RHR_Object
        self.recognizedUser = None
        self.username = None
        self.rhr = None
        self.status = "Processing"
    def checkOpen(self):
            print("checking if open: ")
            print("username:")
            if self.username == None:
                print("username is none")
            else:
                print(self.username)
            print("rhr:")
            if (self.rhr is None):
                print("rhr is none")
            else:
                print(self.rhr)
            if (self.rhr is not None and self.username is not None) :
                self.RHR_Analysis.OpenFor5()
                print("AUTHORIZED")
                self.status = "Authorized"
                self.statusValue.setText(self.status)
                self.rhr = None
                self.username = None
                self.recognizedUser = None
    
    def setupUi(self, gradientMainScreen):
        userList = users.load_users()
        self.known_face_encodings = []
        self.known_face_names = []  # Update with known user names
        for user in userList:
            self.known_face_encodings.append(user.get_encodings())
            self.known_face_names.append(user.name)
        
        #gradientMainScreen.setObjectName("gradientMainScreen")
        gradientMainScreen.resize(1920, 1080)
        gradientMainScreen.setStyleSheet("background-image: url(:/images/images/Blue_BG.png);")

        self.centralwidget = QtWidgets.QWidget(gradientMainScreen)
        self.centralwidget.setObjectName("centralwidget")

        # Setting up settings button
        self.SettingsButton = QPushButton("Admin Controls", self.centralwidget)
        self.SettingsButton.setGeometry(QtCore.QRect(280, 10, 151, 61))
        #self.SettingsButton.setStyleSheet("background-color: #fff; border: 1px solid #000; border-radius: 4px; color: #000; padding: 12px 40px; font-family: Arial; font-size: 14px; font-weight: 400; line-height: 20px;")
        #self.SettingsButton.clicked.connect(self.)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(480, 20, 991, 901))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")

        self.cameraLabel = QtWidgets.QLabel(self.widget)
        self.cameraLabel.setGeometry(QtCore.QRect(250, 10, 480, 360))
        self.cameraLabel.setObjectName("cameraLabel")

        gradientMainScreen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(gradientMainScreen)
        self.statusbar.setObjectName("statusbar")
        gradientMainScreen.setStatusBar(self.statusbar)
        
        #self.retranslateUi(gradientMainScreen)
        #QtCore.QMetaObject.connectSlotsByName(gradientMainScreen)
        self.startB = QPushButton("Start", self.centralwidget)
        self.startB.clicked.connect(self.startButton)
        self.wasStarted = False
        self.startB.setGeometry(QtCore.QRect(280, 81, 151, 61))
        
        self.nameTxt = QLabel("User: ", self.centralwidget)
        self.nameTxt.setGeometry(QtCore.QRect(250, 600, 151,61))
        self.userNameTxt = QLabel(self.username, self.centralwidget)
        self.userNameTxt.setGeometry(QtCore.QRect(300, 600, 151, 61))
        
        self.rhrB = QPushButton("Analyze HR", self.centralwidget)
        self.rhrB.clicked.connect(self.add_hr)
        self.rhrB.setGeometry(QtCore.QRect(280,220, 151,61))
        
        #Heart Rate text
        self.bpmTxt = QLabel("Heart Rate: ", self.centralwidget)
        self.bpmTxt.setGeometry(QtCore.QRect(280,290,151,61))
        self.rhrTxt = QLabel(self.rhr, self.centralwidget)
        self.rhrTxt.setGeometry(QtCore.QRect(280,360,151,61))
        
        self.statusTxt = QLabel("Status: ", self.centralwidget)
        self.statusTxt.setGeometry(QtCore.QRect(280,430,151,61))
        self.statusValue = QLabel(self.status, self.centralwidget)
        self.statusValue.setGeometry(QtCore.QRect(280,500,151,61))
        
        
        self.analyze=QPushButton("Analyze Face",self.centralwidget)
        self.analyze.clicked.connect(self.recognize_from_camera)
        self.analyze.setGeometry(QtCore.QRect(280, 150, 151, 61))
        
     
              
    def add_hr(self):
        if self.rhr is None or self.username is None:
            self.status="Processing"
            self.statusValue.setText(self.status)
        
        beatList = self.RHR_Analysis.sample()
        rhr = self.RHR_Analysis.analysis(beatList)
        #beatList = asyncio.run(self.RHR_Analysis.sample())
        #rhr = asyncio.run(self.RHR_Analysis.analysis(beatList))
        print(rhr)
        self.rhr = rhr
        self.rhrTxt.setText(str(rhr))
        self.checkOpen()
        if self.recognizedUser is not None:
            print("Recognized User: "+self.recognizedUser.get_first_name())
            print("recognized user's RHR:'"+str(self.recognizedUser.get_rhr()))
            print("Duress? : "+str(self.RHR_Analysis.analyze(self.recognizedUser.get_rhr(), rhr)))
        return rhr
        
    def get_camera_frame(self):
        # Initialize the camera capture
        cap = self.capture
        if not cap.isOpened():
            print("Error: Camera could not be accessed.")
            return None

        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            return None
        return frame 
        
    def recognize_from_camera(self):
        if self.rhr is None or self.username is None:
            self.status="Processing"
            self.statusValue.setText(self.status)
            
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
                name=self.known_face_names[best_match_index]
                print(name)
                #self.recognizedUser = users.search_database(face_encoding_to_check)
                self.username = name
                self.userNameTxt.setText(name)
                self.checkOpen()
                return name 
            else:
                self.userNameTxt.setText("Not Recognized")
                print("user not found")

        return None

   
        
    
            
    def startButton(self):
        if self.wasStarted:
            return
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update frame every 30ms
        self.wasStarted = True

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)  # Flip the frame horizontally
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(480, 360, QtCore.Qt.KeepAspectRatio)
            self.cameraLabel.setPixmap(QPixmap.fromImage(p))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gradientMainScreen = QtWidgets.QMainWindow()
    ui = Ui_gradientMainScreen()
    ui.setupUi(gradientMainScreen)
    gradientMainScreen.showFullScreen()
    sys.exit(app.exec())

