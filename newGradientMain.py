import sys
import cv2
import face_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from adminControlScreen import adminManagement
import asyncio
import threading
import subprocess
import resources
from RHR_Analysis2 import RHR_Analysis_LIB
RHR_Analysis = RHR_Analysis_LIB()
import users


class Ui_gradientMainScreen(QWidget):

    def __init__(self, RHR_Object, parent=None):
        super(Ui_gradientMainScreen, self).__init__(parent)

        self.name = None
        self.rhr = None
        self.status = "Waiting to Start..."
        self.clicked1 = False
        self.clicked2 = False
        self.recognizedUser = None
        #might need to be passed in
        #self.RHR_Analysis = RHR_Analysis_LIB()
        self.RHR_Analysis = RHR_Object

        QFontDatabase.addApplicationFont('TI-92p Mini Sans Normal.ttf')
        self.font = QFont("Ti-92p Mini Sans")
        self.font.setLetterSpacing(0, 90)

        self.createUI(self)
        self.start_camera()

    def add_hr(self):
        self.clicked2 = True
        self.makeBlue()
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
        if self.modeOfOperationBox.ItemIndex == 0:
            CbcMoo.encrypt(self.rhr)
        if self.modeOfOperationBox.ItemIndex == 1:
            CfbMoo.encrypt(self.rhr)
        if self.modeOfOperationBox.ItemIndex == 2:
            OfbMoo.encrypt(self.rhr)


    def startAuthBashScript(self):
        thread = threading.Thread(target=self.runAuthBashScript)
        thread.daemon = True
        thread.start()

    def runAuthBashScript(self):
        time.sleep(1)
        subprocess.run('~/capstone/sayAuth.sh')

    def startDuressBashScript(self):
        thread = threading.Thread(target=self.runDuressBashScript)
        thread.daemon = True
        thread.start()

    def runDuressBashScript(self):
        time.sleep(1)
        subprocess.run('~/capstone/sayDuress.sh')
    

    def checkOpen(self):
        print("username:")
        isUnderDuress = False
        if self.name == None:
            print("name is none")
        else:
            print(self.name)
        print("rhr:")
        if (self.rhr is None):
            print("rhr is none")
        else:
            print(self.rhr)
        if self.recognizedUser is not None and self.rhr is not None:
            isUnderDuress = self.RHR_Analysis.analyze(self.recognizedUser.get_rhr(), self.rhr)
            print("DURESS: "+str(isUnderDuress))
            if isUnderDuress:
                self.makeRed()
                self.startDuressBashScript()
                self.status = "DURESS DETECTED"
                self.rhr = None
                self.name = None
                self.recognizedUser = None
        if (self.rhr is not None and self.name is not None and not isUnderDuress):
            self.RHR_Analysis.OpenFor5()
            self.startAuthBashScript()
            print("AUTHORIZED")
            self.makeGreen()
            self.status = "Authorized"
            self.rhr = None
            self.name = None
            self.recognizedUser = None

    def createUI(self, gradientMainScreen):
    
        effect = QGraphicsOpacityEffect()
        effect.setOpacity(0)
        
        effectRhr = QGraphicsOpacityEffect()
        effectRhr.setOpacity(0)
    
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
        self.nameTxt.setGeometry(530, 580, 634, 80)
        self.nameTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.nameTxt.setFont(self.font)

        self.rhrLabel = QLabel("Heart Rate:", self)
        self.rhrLabel.setGeometry(390, 660, 634, 80)
        self.rhrLabel.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.rhrLabel.setFont(self.font)

        self.rhrTxt = QLabel(self.rhr, self)
        self.rhrTxt.setGeometry(640, 660, 634, 80)
        self.rhrTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.rhrTxt.setFont(self.font)

        self.statusLabel = QLabel("Status:", self)
        self.statusLabel.setGeometry(390, 740, 634, 80)
        self.statusLabel.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.statusLabel.setFont(self.font)

        self.statusTxt = QLabel("", self)
        self.statusTxt.setGeometry(570, 740, 634, 80)
        self.statusTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.statusTxt.setFont(self.font)

        self.clickFace = QLabel("Click Here\nto scan your\nface",self)
        self.clickFace.setAlignment(Qt.AlignCenter)
        self.clickFace.setGeometry(395,145,250,100)
        self.clickFace.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
        self.clickFace.setFont(self.font)
        
        self.firstStep = QLabel("1",self)
        self.firstStep.setGeometry(487,280,150,150)
        self.firstStep.setStyleSheet("QLabel{font-size: 75pt; color: white;}")
        self.firstStep.setFont(self.font)

        self.analyze = QPushButton(self)
        self.analyze.clicked.connect(self.recognize_from_camera)
        self.analyze.setGeometry(445, 270, 150, 150)
        self.analyze.setStyleSheet("background-color: white")
        #self.analyze.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.analyze.setGraphicsEffect(effect)

        self.clickrhr = QLabel("Click Here\nto scan your\nheart rate",self)
        self.clickrhr.setAlignment(Qt.AlignCenter)
        self.clickrhr.setGeometry(1275,145,250,100)
        self.clickrhr.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
        self.clickrhr.setFont(self.font)

        self.secondStep = QLabel("2",self)
        self.secondStep.setGeometry(1367,280,150,150)
        self.secondStep.setStyleSheet("QLabel{font-size: 75pt; color: white;}")
        self.secondStep.setFont(self.font)

        self.analyzeRhr = QPushButton(self)
        self.analyzeRhr.clicked.connect(self.add_hr)
        self.analyzeRhr.setGeometry(1325, 270, 150, 150)
        self.analyzeRhr.setStyleSheet("background-color: white")
        #self.analyzeRhr.setStyleSheet("background-color: rgba(255,255,255,0)")
        self.analyzeRhr.setGraphicsEffect(effectRhr)
        
        self.userManagement = QPushButton("BACK",self)
        self.userManagement.clicked.connect(self.go_to_userManagement)
        self.userManagement.setGeometry(1250,850,250,80)
        
        self.show()


    def go_to_userManagement(self):
        subprocess.Popen([sys.executable, 'run.py'])
        sys.exit()
        return
        
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
        
        button1 = QPainter(self)
        if self.clicked1:
            self.firstStep.setStyleSheet("QLabel{font-size: 80pt; color: gray;}")
            self.clickFace.setStyleSheet("QLabel{font-size: 25pt; color: gray;}")
            button1.setPen(QPen(QColor(255,255,255,100), 7, Qt.SolidLine))
        else:
            self.firstStep.setStyleSheet("QLabel{font-size: 80pt; color: white;}")
            self.clickFace.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
            button1.setPen(QPen(QColor(255,255,255,255), 7, Qt.SolidLine))
        button1.drawEllipse(445,270,150,150)
        
        button2 = QPainter(self)
        if self.clicked2:
            #self.analyzeRhr.setEnabled(False)
            self.secondStep.setStyleSheet("QLabel{font-size: 80pt; color: gray;}")
            self.clickrhr.setStyleSheet("QLabel{font-size: 25pt; color: gray;}")
            button2.setPen(QPen(QColor(255,255,255,100), 7, Qt.SolidLine))
        else:
            button2.setPen(QPen(QColor(255,255,255,255), 7, Qt.SolidLine))
            #self.analyzeRhr.setEnabled(True)
            self.secondStep.setStyleSheet("QLabel{font-size: 80pt; color: white;}")
            self.clickrhr.setStyleSheet("QLabel{font-size: 25pt; color: white;}")
        button2.drawEllipse(1325,270,150,150)
        

    def recognize_from_camera(self):
        self.clicked1 = True
        self.makeBlue()
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
        
        if self.modeOfOperationBox.ItemIndex == 0:
            CbcMoo.encrypt(self.face_locations)
            CbcMoo.encrypt(self.face_encodings)
        if self.modeOfOperationBox.ItemIndex == 1:
            CfbMoo.encrypt(self.face_locations)
            CfbMoo.encrypt(self.face_encodings)
        if self.modeOfOperationBox.ItemIndex == 2:
            OfbMoo.encrypt(self.face_locations)
            OfbMoo.encrypt(self.face_encodings)
            

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
                
                self.recognizedUser = userList[best_match_index]
                print("recognized users rhr: " + str(self.recognizedUser.get_rhr()))
                self.name = name
                self.nameTxt.setText(name)
                self.checkOpen()
                return name
            else:
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
    print(sys.platform)
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    RHR_Analysis = RHR_Analysis_LIB()
    window = Ui_gradientMainScreen(RHR_Analysis)
    window.showFullScreen()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
