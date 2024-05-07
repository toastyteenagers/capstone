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
font_size = 30


class LoadScreens(QWidget):
    def __init__(self, parent=None):
        super(LoadScreens,self).__init__(parent)
        
        self.createUI()
        
    def createUI(self):
        
        self.setGeometry(0,0,1920,1080)
        self.setWindowTitle("Screen Choice")
        
        self.addUserButton = QPushButton("ADD USER",self)
        self.addUserButton.setGeometry(120,300,480,480)
        self.addUserButton.clicked.connect(self.add_user)
        
        self.mainScreenButton = QPushButton("MAIN SCREEN",self)
        self.mainScreenButton.setGeometry(720,300,480,480)
        self.mainScreenButton.clicked.connect(self.main_screen)
        
        self.userInfoButton = QPushButton("USER INFORMATION",self)
        self.userInfoButton.setGeometry(1320,300,480,480)
        self.userInfoButton.clicked.connect(self.system_management)
        
        self.show()
        
    def add_user(self):
        subprocess.Popen([sys.executable, 'addUser.py'])
        sys.exit()
        
    def main_screen(self):
        subprocess.Popen([sys.executable, 'newGradientMain.py'])
        sys.exit()
        
    def system_management(self):
        #subprocess.Popen([sys.executable, 'adminControlScreen.py'])
        subprocess.Popen([sys.executable, 'newPassword.py'])
        sys.exit()
    
    
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
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = LoadScreens()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

#.move()
#.resize()
