from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
import sys
import cv2
import face_recognition
import numpy as np
from users import createUser

Camera_X = 640
Camera_Y = 480
Camera_W = 640
Camera_H = 640
font_size = 30


class AddUserScreen(QWidget):
    def __init__(self):
        super(AddUserScreen,self).__init__()

        self.name = ''
        self.rhr = 30
        self.encodings = []
        self.disability = 0
        self.level = 0


        self.font = QFont()
        self.font.setPointSize(font_size)

        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle("Add User Screen")

        self.layout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.inputLayout = QFormLayout()
        self.rightLayout = QFormLayout()
        #self.layout.setGeometry(0,0,1920,1080)
        QApplication.setFont(self.font, "QLabel")

        self.Worker1 = Worker1(self)
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

        self.FeedLabel = QLabel()
        self.FeedLabel.setGeometry(0,0,1920,1080)
        self.leftLayout.addWidget(self.FeedLabel)

        self.addUserButton = QPushButton("Add User")
        self.addUserButton.clicked.connect(self.add_user)
        self.leftLayout.addWidget(self.addUserButton)

        self.nameText = QLabel("Full Name: ")
        self.nameText.setGeometry(700,500,280,150)
        self.nameText.setFont(self.font)
        self.nameBox = QLineEdit(self)
        self.inputLayout.addRow(self.nameText, self.nameBox)

        self.addNameButton = QPushButton('Input:')
        self.addNameButton.clicked.connect(self.add_name)
        self.input_name = QLabel(self.name)
        self.rightLayout.addRow(self.addNameButton, self.input_name)

        self.rhrText = QLabel("Resting Heart Heart Rate: ")
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





        self.layout.addLayout(self.leftLayout)
        self.layout.addLayout(self.inputLayout)
        self.layout.addLayout(self.rightLayout)
        self.setLayout(self.layout)

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
            else:
                self.adminButton.setEnabled(False)

    def add_user(self):
        createUser(self.name, self.encodings, self.rhr, self.disability, self.level)
        #print(self.encodings)

class Worker1(QThread):
    def __init__(self, window):
        super(Worker1, self).__init__()
        self.window = window
        self.take_encoding = False
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        #can get rid of thread active
        self.ThreadActive = True
        Capture = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if self.take_encoding == True:
                face_locations = face_recognition.face_locations(frame)
                for (top, right, bottom, left) in face_locations:
                    face_image = frame[top:bottom, left:right]
                    face_encodings = face_recognition.face_encodings(frame,face_locations)
                    #print("Face Encodings: ", face_encodings)
                    flat_encodings = np.concatenate(face_encodings).tolist()
                    #print("flattened: ", flat_encodings)
                    self.window.encodings = flat_encodings
                    self.take_encoding = False
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image,1)
                ConvertToQtFormat = QImage(FlippedImage.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(Camera_W, Camera_H, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
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