from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
import sys
import cv2
import face_recognition
import numpy as np
import subprocess
import asyncio 
from users import createUser, createAdmin
from RHR_Analysis2 import RHR_Analysis_LIB
RHR_Analysis = RHR_Analysis_LIB()
Camera_X = 0
Camera_Y = 0
Camera_W = 800
Camera_H = 450
font_size = 30


class AddUserScreen(QWidget):
    backClicked = QtCore.pyqtSignal()
    def __init__(self, RHR_Object, parent=None):
        super(AddUserScreen,self).__init__(parent)

        self.checks = [0,0,0,0,0]
        self.level = None
        self.name = ""
        self.rhr = None
        self.disability = None
        self.encodings = []
        self.password = None
        self.RHR_Analysis = RHR_Object

        #self.test = QFont()
        #print(self.test.letterSpacingType())

        QFontDatabase.addApplicationFont('/capstone/TI-92p Mini Sans Normal.ttf')
        self.font = QFont("Ti-92p Mini Sans")
        self.font.setLetterSpacing(0,90)

        self.createUI()
        self.loop()

    def loop(self):
        self.clock = QTimer(self)
        self.clock.timeout.connect(self.check)
        self.clock.start()

    def createUI(self):
        
        #self.layout = QHBoxLayout(self)

        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle("Add User Screen")
        #self.setStyleSheet("background-color: #41454f")

        self.Worker1 = Worker1(self)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

        self.FeedLabel = QLabel(self)
        self.FeedLabel.setGeometry(0,0,Camera_W,Camera_H)
        #center at 640,360
        self.FeedLabel.move(215,135)
        self.FeedLabel.setStyleSheet("border: 8px solid white")

        self.addUserButton = QPushButton("Add User",self)
        self.addUserButton.setGeometry(215,655,Camera_W, 100)
        self.addUserButton.clicked.connect(self.add_user)
        self.addUserButton.setEnabled(False)

        self.titleTxt = QLabel("Add New User",self)
        self.titleTxt.setGeometry(298,35,634,80)
        self.titleTxt.setStyleSheet("QLabel{font-size: 70pt; color: white;}")
        self.titleTxt.setFont(self.font)

        #1170, 180
        self.nameText = QLabel("Full Name: ", self)
        self.nameText.setGeometry(1114,120,242,50)
        self.nameText.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
        self.nameText.setFont(self.font)
        self.nameBox = QLineEdit(self)
        self.nameBox.setGeometry(1411,125,300,45)
        
        self.rhrTxt = QLabel("Heart Rate: ", self)
        self.rhrTxt.setGeometry(1114, 200, 269,50)
        self.rhrTxt.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
        self.rhrTxt.setFont(self.font)
        self.rhrButton = QPushButton("Start Input!", self)
        self.rhrButton.setGeometry(1411,200, 300,50)
        self.rhrButton.clicked.connect(self.add_rhr)

        self.faceTxt = QLabel("Scan Face: ", self)
        self.faceTxt.setGeometry(1114, 280, 269,50)
        self.faceTxt.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
        self.faceTxt.setFont(self.font)
        self.faceButton = QPushButton("Start Scan!", self)
        self.faceButton.setGeometry(1411,280,300,50)
        self.faceButton.clicked.connect(self.add_encodings)

        self.disabilityTxt = QLabel("Disability Accommodation", self)
        self.disabilityTxt.setGeometry(1114, 360, 597,50)
        self.disabilityTxt.setStyleSheet("QLabel{font-size: 36pt; color: white;}")
        self.disabilityTxt.setFont(self.font)
        self.disabilityBox = QComboBox(self)
        self.disabilityBox.setGeometry(1114, 420, 597, 50)
        self.disabilityBox.addItems(['Select An Option','None','Facial Detection', 'Heart Rate', 'Facial Detection and Heart Rate'])

        self.adminTxt = QLabel("Admin:",self)
        self.adminTxt.setGeometry(1114, 500, 161,50)
        self.adminTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.adminTxt.setFont(self.font)
        self.adminBox = QCheckBox(self)
        self.adminBox.setGeometry(1264, 500, 200,50)
        #self.adminBox.setStyleSheet("QCheckBox{font-size: 40pt; color: white; width:50px; height:50px;}")
        self.adminBox.toggled.connect(self.adminCheck)
        #Fix size of checkbox
        #self.adminBox.setStyleSheet("QCheckBox::inidcator {width: 50px; height: 50px;}")

        self.userTxt = QLabel("User:",self)
        self.userTxt.setGeometry(1444, 500, 161,50)
        self.userTxt.setStyleSheet("QLabel{font-size: 30pt; color: white;}")
        self.userTxt.setFont(self.font)
        self.userBox = QCheckBox(self)
        self.userBox.setGeometry(1574, 500, 200,50)
        self.userBox.toggled.connect(self.userCheck)
        
        
        self.passwordTxt = QLabel("Enter Password: ", self)
        self.passwordTxt.setGeometry(1114, 580, 369,50)
        self.passwordTxt.setStyleSheet("QLabel{font-size: 40pt; color: grey;}")
        self.passwordTxt.setFont(self.font)
        self.passwordBox = QLineEdit(self)
        self.passwordBox.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordBox.setGeometry(1114, 635, 597,50)
        self.passwordBox.setEnabled(False)


        #Check Texts
        self.checkName = QLabel("NAME",self)
        self.checkName.setGeometry(220,855,150,150)
        self.checkName.setStyleSheet("QLabel{font-size: 15pt; color: grey;}")
        self.checkName.setFont(self.font)

        self.checkRhr = QLabel("RHR",self)
        self.checkRhr.setGeometry(558,855,150,150)
        self.checkRhr.setStyleSheet("QLabel{font-size: 20pt; color: grey;}")
        self.checkRhr.setFont(self.font)

        self.checkFace = QLabel("FACE",self)
        self.checkFace.setGeometry(870,855,150,150)
        self.checkFace.setStyleSheet("QLabel{font-size: 20pt; color: grey;}")
        self.checkFace.setFont(self.font)

        self.checkDis = QLabel("ACC",self)
        self.checkDis.setGeometry(1190,855,150,150)
        self.checkDis.setStyleSheet("QLabel{font-size: 20pt; color: grey;}")
        self.checkDis.setFont(self.font)

        self.checkLevel = QLabel("LEVEL",self)
        self.checkLevel.setGeometry(1495,855,150,150)
        self.checkLevel.setStyleSheet("QLabel{font-size: 15pt; color: grey;}")
        self.checkLevel.setFont(self.font)

        self.show()
        #self.layout.addWidget(self.FeedLabel)

    def adminCheck(self):
        if self.adminBox.isChecked():
            self.userBox.setCheckState(False)
            self.level = 1
        else:
            self.checks[4] = 0
            self.level = 0

    def add_user(self):
        print(self.name, self.level, self.disability, self.rhr, self.password)
        if self.level == 1 and (len(self.password) > 0):
            createAdmin(self.name,self.encodings,self.rhr,self.disability, self.password, self.level)
            print("admin added")
        else:
            createUser(self.name, self.encodings, self.rhr, self.disability, self.level)
            print("user added")
        subprocess.Popen([sys.executable, 'run.py'])
        sys.exit()

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def add_encodings(self):
        self.Worker1.take_encoding = True

    #def add_rhr(self):
    #    beatList = self.RHR_Analysis.sample()
    #    rhr = self.RHR_Analysis(beatList)
    #    self.rhr = rhr
    #    return rhr

    #def add_disability(self):
        #self.disability = 

    def userCheck(self):
        if self.userBox.isChecked():
            self.checks[4] = 1
            self.adminBox.setCheckState(False)
            self.level = 0
        else:
            self.checks[4] = 0

    def check(self):
        if 0 not in self.checks:
            self.addUserButton.setEnabled(True)
        else:
            self.addUserButton.setEnabled(False)

        if self.disabilityBox.currentIndex() > 0:
            self.disability = self.disabilityBox.currentIndex()
            self.checks[3] = 1
        else:
            self.disability = None
            self.checks[3] = 0

        if len(self.nameBox.text()) > 0:
            self.name = self.nameBox.text()
            self.checks[0] = 1
        else:
            self.checks[0] = 0

        if self.level == 1:
            self.passwordTxt.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
            self.passwordBox.setEnabled(True)
            if len(self.passwordBox.text()) > 0:
                self.checks[4] = 1
                self.password = self.passwordBox.text()
            else:
                self.password = None
                self.checks[4] = 0
        else:
            self.password = None
            self.passwordTxt.setStyleSheet("QLabel{font-size: 40pt; color: grey;}")
            self.passwordBox.setEnabled(False)
        
        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        Qt.gray
        painter.setPen(QPen(QColor(0,0,0,100), 10, Qt.SolidLine))
        painter.drawRect(210,130,810,460)

        circle1 = QPainter(self)
        if self.checks[0] == 1:
            self.checkName.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
            circle1.setPen(QPen(Qt.green, 7, Qt.SolidLine))
        else:
            self.checkName.setStyleSheet("QLabel{font-size: 40pt; color: grey;}")
            circle1.setPen(QPen(Qt.gray, 7, Qt.SolidLine))
        circle1.drawEllipse(199,850,180,180)

        circle2 = QPainter(self)
        if self.checks[1] == 1:
            self.checkRhr.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
            circle2.setPen(QPen(Qt.green, 7, Qt.SolidLine))
        else:
            self.checkRhr.setStyleSheet("QLabel{font-size: 40pt; color: grey;}")
            circle2.setPen(QPen(Qt.gray, 7, Qt.SolidLine))
        circle2.drawEllipse(519,850,180,180)

        circle3 = QPainter(self)
        if self.checks[2] == 1:
            self.checkFace.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
            circle3.setPen(QPen(Qt.green, 7, Qt.SolidLine))
        else:
            self.checkFace.setStyleSheet("QLabel{font-size: 40pt; color: grey;}")
            circle3.setPen(QPen(Qt.gray, 7, Qt.SolidLine))
        circle3.drawEllipse(839,850,180,180)

        circle4 = QPainter(self)
        if self.checks[3] == 1:
            self.checkDis.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
            circle4.setPen(QPen(Qt.green, 7, Qt.SolidLine))
        else:
            self.checkDis.setStyleSheet("QLabel{font-size: 40pt; color: grey;}")
            circle4.setPen(QPen(Qt.gray, 7, Qt.SolidLine))
        circle4.drawEllipse(1159,850,180,180)

        circle5 = QPainter(self)
        if self.checks[4] == 1:
            self.checkLevel.setStyleSheet("QLabel{font-size: 40pt; color: white;}")
            circle5.setPen(QPen(Qt.green, 7, Qt.SolidLine))
        else:
            self.checkLevel.setStyleSheet("QLabel{font-size: 40pt; color: grey;}")
            circle5.setPen(QPen(Qt.gray, 7, Qt.SolidLine))
        circle5.drawEllipse(1479,850,180,180)

    def add_rhr(self):
        self.checks[1] = 1
        #beatList = asyncio.run(RHR_Analysis.sample())
        beatList = self.RHR_Analysis.sample()
        #rhr = asyncio.run(RHR_Analysis.analysis(beatList))
        rhr = self.RHR_Analysis.analysis(beatList)
        #rhr = self.RHR_Analysis.analysis(beatList)
        self.rhr = rhr
        return rhr

    def add_encodings(self):
        self.checks[2] = 1
        print(self.Worker1.take_encoding)
        self.Worker1.take_encoding = True
        print(self.Worker1.take_encoding)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

stylesheet = """
    AddUserScreen {
        background-color: #41454f;
        background-repeat: no-repeat;
        background-position: center;
    }
"""


class Worker1(QThread):
    def __init__(self, window):
        super(Worker1, self).__init__()
        self.window = window
        self.take_encoding = False
        self.Capture = None
    ImageUpdate = pyqtSignal(QImage)
    
    def run(self):
        self.ThreadActive = True
        self.Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = self.Capture.read()
            if self.take_encoding:
                face_locations = face_recognition.face_locations(frame)
                face_encodings = face_recognition.face_encodings(frame, face_locations)
                for face_location, face_encoding in zip(face_locations, face_encodings):
                    #print("face encoding: "+str(face_encoding))
                    top, right, bottom, left = face_location
                    face_image = frame[top:bottom, left:right]
                    flat_encoding = face_encoding.tolist()
                    #print("face encoding list: "+str(flat_encoding))
                    self.window.encodings = flat_encoding
                self.take_encoding = False
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(Camera_W, Camera_H, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
        
    def stop(self):
        self.ThreadActive = False
        if self.Capture is not None:
            self.Capture.release()
        self.quit()


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    RHR_Analysis = RHR_Analysis_LIB()
    window = AddUserScreen(RHR_Analysis)
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

#.move()
#.resize()
