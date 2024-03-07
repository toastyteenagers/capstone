import sys
from PyQt6.QtWidgets import *
from PyQt6.QtMultimedia import QCamera, QMediaCaptureSession
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import QUrl
from PyQt6 import QtCore, QtGui, QtWidgets
import pickle
import csv
from UserFields import UserFields
import random

class UI_UserList(QWidget):
    def __init__(self):
        super().__init__()
        self.active_users = []

        self.createUI()
        self.loadUserData()
        self.listNames()

    def createUI(self):
        self.setWindowTitle('User List')
        self.resize(1920,1080)
        self.grid = QGridLayout()
        self.setLayout(self.grid)

    def listNames(self):
        self.clearLayout()
        self.text = []
        self.names = []
        for i in self.active_users:
            self.text.append((' ----- Name:\t' + i.get_name() + '\t\t ----- Average Heart Rate:\t' + str(i.get_rhr()) + '\t ----- Access: ' + str(i.get_access())))
            self.names.append(i.get_name())

        #Delete later, randomly generate users to show deletion
        gButton = QPushButton('Generate Users')
        gButton.clicked.connect(self.generateUsers)
        self.grid.addWidget(gButton, 0, 0)

        row = 1
        for j,name in zip(self.text, self.names):
            temp_name = QLabel(j)
            temp_button = QPushButton('Delete')
            temp_button.clicked.connect(lambda _, name=name: self.deleteUser(name))
            self.grid.addWidget(temp_name, row, 0)
            self.grid.addWidget(temp_button, row, 1)
            row += 1

    def printUserData(self):
        users = []

        with open('Users.csv', mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Encodings', 'rhr', 'disability'])
            for user in self.active_users:
                writer.writerow([user.get_name(), user.get_vector(), user.get_rhr(), user.get_disability()])
                users.append(user.get_name())

    def loadUserData(self):
        filepath = "newUsers.pkl"
        try:
            with open(filepath, "rb") as pickle_file:
                self.active_users = pickle.load(pickle_file)
                print("User Data loaded")
                self.printUserData()
        except FileNotFoundError:
            print("User Data not found")
            print("Generating new Users for Demo. Try Again.")
            self.generateUsers()
            self.loadUserData()

    def clearLayout(self):
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

    def deleteUser(self, name):
        temp = None
        found = False
        for user in self.active_users:
            if user.get_name() == name:
                temp = user
                found = True
                break

        if found:
            self.active_users.remove(temp)
            print('Deleted: ' + temp.get_name())
            self.save_User()
            self.printUserData()
            self.listNames()
        else:
            print('User ot found')

    def save_User(self):
        filepath = "newUsers.pkl"

        with open(filepath, "wb") as pickle_file:
            pickle.dump(self.active_users, pickle_file)
            print("Successfully saved active user")

    def createUser(self, name, face_encodings, rhr, disability):
        user = UserFields(name, face_encodings, rhr, disability)
        self.active_users.append(user)
        return user

    def generateUsers(self):
        names = ['Owen', 'Hayden', 'Roohan', 'Alex']
        for i in range(4):
            encodings = [1,2,3,4,5]
            rhr = random.randrange(0,100,1)
            disability = random.randrange(0,1,1)
            self.createUser(names[i], encodings, rhr, disability)

        self.save_User()
        self.printUserData()
        self.listNames()


app = QApplication(sys.argv)
window = UI_UserList()
window.show()
app.exec()