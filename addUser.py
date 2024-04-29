from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
#from PyQt5.QtMultimedia import *
#from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
import sys
import cv2
import face_recognition
import numpy as np
import asyncio 
from users import createUser
import RHR_Analysis
Camera_X = 640
Camera_Y = 480
Camera_W = 640
Camera_H = 640
font_size = 30


class AddUserScreen(QWidget):
    backClicked = QtCore.pyqtSignal()
    def __init__(self, ui_init_conf_main, parent=None):
        super(AddUserScreen,self).__init__(parent)

        self.ui_init_conf_main = ui_init_conf_main

        self.name = ''
        self.rhr = 30
        self.encodings = []
        self.disability = 0
        self.level = 0
        self.password = ''

        #self.font = QFont()
        #self.font.setPointSize(font_size)

        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle("Add User Screen")

        self.layout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.inputLayout = QFormLayout()
        self.rightLayout = QFormLayout()
        #QApplication.setFont(self.font, "QLabel")

        self.Worker1 = Worker1(self)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

        self.FeedLabel = QLabel()
        self.FeedLabel.setGeometry(0,0,1920,1080)
        self.leftLayout.addWidget(self.FeedLabel)

        self.addUserButton = QPushButton("Add User")
        self.addUserButton.clicked.connect(self.add_user)
        self.leftLayout.addWidget(self.addUserButton)
        
        self.backButton = QPushButton("Back")
        self.backButton.clicked.connect(self.go_back)
        self.leftLayout.addWidget(self.backButton)

        self.nameText = QLabel("Full Name: ")
        self.nameText.setGeometry(700,500,280,150)
        #self.nameText.setFont(self.font)
        self.nameBox = QLineEdit(self)
        self.inputLayout.addRow(self.nameText, self.nameBox)

        self.addNameButton = QPushButton('Input:')
        self.addNameButton.clicked.connect(self.add_name)
        self.input_name = QLabel(self.name)
        self.rightLayout.addRow(self.addNameButton, self.input_name)

        self.rhrText = QLabel("Resting Heart Rate: ")
        self.heartRateButton = QPushButton('Start Input')
        self.heartRateButton.clicked.connect(self.add_rhr)
        self.inputLayout.addRow(self.rhrText, self.heartRateButton)

        self.faceText = QLabel("Activate Facial Recognition: ")
        self.faceEncodingsButton = QPushButton('Train')
        self.faceEncodingsButton.clicked.connect(self.add_encodings)
        self.inputLayout.addRow(self.faceText, self.faceEncodingsButton)

        self.disabilityBox = QCheckBox("Please check if you require disability accomodations:", self)
        self.disabilityButton = QPushButton("Submit")
        self.disabilityButton.setEnabled(False)
        self.disabilityBox.toggled.connect(lambda:self.checked(self.disabilityBox))
        self.disabilityButton.clicked.connect(self.add_disability)
        self.inputLayout.addRow(self.disabilityBox,self.disabilityButton)

        self.adminBox = QCheckBox("Admin User?", self)
        self.adminButton = QPushButton("Submit")
        self.adminButton.setEnabled(False)
        self.adminBox.toggled.connect(lambda:self.checked(self.adminBox))
        self.adminButton.clicked.connect(self.admin_level)
        self.inputLayout.addRow(self.adminBox, self.adminButton)
        
        self.passTxt = QLabel("Password: ")
        self.passBox = QLineEdit(self)
        self.passBox.setEnabled(False)
        self.inputLayout.addRow(self.passTxt, self.passBox)





        self.layout.addLayout(self.leftLayout)
        self.layout.addLayout(self.inputLayout)
        self.layout.addLayout(self.rightLayout)
        self.setLayout(self.layout)

    def go_back(self):
        self.Worker1.stop()
        self.backClicked.emit()
        if isinstance(self.parent(), QtWidgets.QStackedWidget):
            self.parent().setCurrentIndex(2)
        self.ui_init_conf_main.incrementCount()

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def add_name(self):
        self.name = self.nameBox.text()
        print(self.name)

    def admin_level(self):
        self.level = 1

    def add_encodings(self):
        print(self.Worker1.take_encoding)
        self.Worker1.take_encoding = True
        print(self.Worker1.take_encoding)

    def add_rhr(self):
        print('need to inplement rhr method')
        beatList = asyncio.run(RHR_Analysis.sample())
        rhr = asyncio.run(RHR_Analysis.analysis(beatList))
        print(rhr)
        self.rhr = rhr
        return rhr

    def add_disability(self):
        print('Need to add implementation of other disabilities')
        self.disability = 1

    def checked(self,c):
        if c.text() == "Please check if you require disability accomodations:":
            if(self.disabilityBox.isChecked()):
                self.disabilityButton.setEnabled(True)
            else:
                self.disabilityButton.setEnabled(False)
        elif c.text() == "Admin User?":
            if(self.adminBox.isChecked()):
                self.adminButton.setEnabled(True)
                self.passBox.setEnabled(True)
                self.level = 1
                self.password = self.passBox.text()
            else:
                self.adminButton.setEnabled(False)
                self.passBox.setEnabled(False)
                self.level = 0

    def add_user(self):
        #print(self.encodings)
        #createAdmin(name, encodings, rhr, disability, password='Admin', level=1, uses=[], doc=datetime.now()):
        if self.level == 1 and (len(self.password) > 0):
            createAdmin(self.name,self.encodings,self.rhr,self.disability, self.password, self.level)
            print("admin added")
        else:
            createUser(self.name, self.encodings, self.rhr, self.disability, self.level)
            print("user added")
        #print(self.encodings)

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
    window = AddUserScreen()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

#.move()
#.resize()
