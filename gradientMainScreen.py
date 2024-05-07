import sys
import cv2
import face_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
import asyncio
import threading
import subprocess
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
import RHR_Analysis
#import DoorControl
import users

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
            print(user.name)
            self.known_face_encodings.append(user.get_encodings())
            self.known_face_names.append(user.name)
        #RHR_Analysis.OpenFor5()
        


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-image: url(:/images/images/Blue_BG.png);")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
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
        self.progressBar.setMaximum(100)
        self.progressBar.setVisible(True)

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

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Setup camera
        self.capture = cv2.VideoCapture(2)
        self.timer = QTimer()
        #self.timer.timeout.connect(self.update_frame)
        self.timer.start()

        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update frame every 30ms
        self.wasStarted = True
        self.timer.start(30)

        # Timer to show text after three seconds
        self.textTimer = QTimer()
        self.textTimer.singleShot(5000, self.show_text)

        self.progressValue = 0

        # Setup status bar timer
        self.statusBarTimer = QTimer()
        self.statusBarTimer.timeout.connect(self.show_status_bar_message)
        self.statusBarTimer.start(10000)

        # Start asynchronous function to retrieve BPM value
        loop = asyncio.get_event_loop()
        self.bpm_task = loop.create_task(self.retrieve_bpm())

    async def retrieve_bpm(self):
        print("calling bpm")
        # Simulating asynchronous task to retrieve BPM value
        bpm_value = await RHR_Analysis.sample()  # Simulate some asynchronous operation
        # Update the BPM field with the retrieved value
        self.additionalTextLabel.setText(f"BPM: {bpm_value}")

    def show_status_bar_message(self):
        # Display status bar message for 10 seconds
        self.statusbar.showMessage("Status: Ready", 10000)
        
    def unflatten_face_encodings(flat_encodings, encoding_length=128):
        unflattened_encodings = []
        for i in range(0, len(flat_encodings), encoding_length):
            unflattened_encodings.append(np.array(flat_encodings[i:i+encoding_length]))
        return unflattened_encodings
        

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)  # Flip the frame horizontally
            h, w, ch = frame.shape
            face_locations = face_recognition.face_locations(frame)
            for (top, right, bottom, left) in face_locations:
                # Crop the face from the frame
                face_image = frame[top:bottom, left:right]

                # Encode the face
                face_encodings = face_recognition.face_encodings(face_image)
                
                # Unflatten the face encodings
                unflattened_encodings = []
                for encoding in face_encodings:
                    unflattened_encodings.append(np.reshape(encoding, (1, -1)))

                # Compare face encodings with known face encodings
                for face_encoding in unflattened_encodings:
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
                            # needs to show nice access granted and display rhr, as well as opening door.
                            DoorControl.OpenFor5()

        # Convert the frame to QImage format and display it in the cameraLabel
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(480, 360, QtCore.Qt.KeepAspectRatio)
        self.cameraLabel.setPixmap(QPixmap.fromImage(p))

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(480, 360, QtCore.Qt.KeepAspectRatio)
            self.cameraLabel.setPixmap(QPixmap.fromImage(p))

    def show_text(self):
        self.textLabel.setText("User: Roohan Amin")
        self.textLabel.setStyleSheet("color: white; font-size: 20px; background-color: rgba(0, 0, 0, 0.5)")
        self.progressBar.setVisible(True)  # Show the progress bar when the text appears

 userlist
    def update_progress(self, bpm=-1):
        self.progressValue = 0
        self.progressBar.setValue(0)
        self.finalTextLabel.setVisible(False)
        self.additionalTextLabel.setText("BPM: -")
        self.widget.parent().setStyleSheet("background-image: url(:/images/images/Blue_BG.png);")

        # Start incrementing progress every 100ms until reaching 100%
        self.progress_timer = QtCore.QTimer()
        self.progress_timer.timeout.connect(self.increment_progress)
        self.progress_timer.start(100)

    def increment_progress(self):
        self.progressValue += 1
        self.progressBar.setValue(self.progressValue)
        if self.progressValue >= 100:
            self.progress_timer.stop()
            self.finalTextLabel.setVisible(True)
            self.additionalTextLabel.setText("BPM: " + str(bpm_value))
            self.widget.parent().setStyleSheet("background-image: url(:/images/images/Green_BG.png);")


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
    gradientMainScreen = QtWidgets.QMainWindow()
    ui = Ui_gradientMainScreen()
    ui.setupUi(gradientMainScreen)
    gradientMainScreen.showFullScreen()
    sys.exit(app.exec())

