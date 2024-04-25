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
from users import load_users, load_admins, delete_from_database


class adminManagement(QWidget):
    def __init__(self):
        super(adminManagement, self).__init__()

        self.users_tab = []
        self.layout = QVBoxLayout()
        self.createUI()

    def load(self):
        admins = load_admins()
        users = load_users()
        for i in admins:
            self.active_users.append(i)
        for j in users:
            self.active_users.append(j)

    def createUI(self):
        self.active_users = []
        self.load()

        self.setWindowTitle("System Management")
        self.setGeometry(0, 0, 1920, 1080)

        for user in self.active_users:
            self.listUsers(user)
        self.setLayout(self.layout)

    def listUsers(self, user):
        # User and Delete
        user_layout = QHBoxLayout()
        # User and Drop Down
        temp_user = user_info(user, self)
        deleteButton = QPushButton("Delete")
        deleteButton.clicked.connect(lambda: self.delete_user(user))

        user_layout.addWidget(temp_user)
        if user.get_level() == 0:
            user_layout.addWidget(deleteButton)

        self.layout.addLayout(user_layout)

    def delete_user(self, user):
        delete_from_database(user.get_name(), user.get_encodings())
        self.clear_whole_layout(self.layout)
        self.createUI()

    def clear_whole_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            if item.layout():
                self.clear_whole_layout(item.layout())


class user_info(QWidget):
    def __init__(self, user, parent):
        super().__init__(parent)
        self.user = user
        self.createUI()

    def createUI(self):
        # User Banner
        self.layout = QVBoxLayout()
        # User Info
        self.bannerLayout = QFormLayout()

        self.name = QLabel(self.user.get_name())
        self.toggleButton = QPushButton('Arrow Down')
        self.toggleButton.clicked.connect(self.toggle_info)
        self.bannerLayout.addRow(self.name, self.toggleButton)

        self.toggleWidget = QWidget()

        self.load_data()

        self.layout.addWidget(self.toggleWidget)

        self.layout.addLayout(self.bannerLayout)

        self.setLayout(self.layout)

    def toggle_info(self):
        if self.toggleWidget.isVisible():
            self.toggleWidget.setVisible(False)
            self.clear(self.infoLayout)
            self.clear_banner()
        else:
            self.toggleWidget.setVisible(True)
            self.load_data()

        # self.createUI()

    def clear_banner(self):
        item = self.bannerLayout.itemAt(2)
        widget = item.widget()
        if widget:
            widget.deleteLater()

    def clear(self, layout):
        for i in range(layout.count()):
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            elif item.layout():
                self.clear(item.layout())

    def load_data(self):
        self.infoLayout = QFormLayout(self.toggleWidget)

        self.level_text = QLabel("User Level: ")
        if self.user.get_level() == 1:
            self.level = QLabel("Admin")
        else:
            self.level = QLabel("Standard User")
        self.infoLayout.addRow(self.level_text, self.level)

        self.first_name_text = QLabel("First Name: ")
        self.first_name = QLabel(self.user.get_first_name())
        self.infoLayout.addRow(self.first_name_text, self.first_name)

        self.last_name_text = QLabel("Last Name: ")
        self.last_name = QLabel(self.user.get_last_name())
        self.infoLayout.addRow(self.last_name_text, self.last_name)

        self.doc_text = QLabel("User Created On: ")
        self.doc = QLabel(self.user.get_dateOfCreation())
        self.infoLayout.addRow(self.doc_text, self.doc)

        self.disability_text = QLabel("Disability Accomodations: ")
        self.disability = QLabel(self.user.get_disability())
        self.infoLayout.addRow(self.disability_text, self.disability)

        self.rhr_text = QLabel("Resting Heart Rate: ")
        self.rhr = QLabel(str(self.user.get_rhr()))
        self.infoLayout.addRow(self.rhr_text, self.rhr)

        self.uses_text = QLabel("User System History: ")
        self.use_layout = QVBoxLayout()
        self.use_layout.addWidget(self.uses_text)
        for use in self.user.get_use_history():
            use_text = QLabel('\t' + use[0] + '\t' + use[1])
            self.use_layout.addWidget(use_text)
        self.container = QWidget()
        self.container.setLayout(self.use_layout)
        self.infoLayout.addRow(self.container)

        self.container2 = QWidget()
        self.container2.setLayout(self.infoLayout)
        self.bannerLayout.addRow(self.container2)


def main():
    app = QApplication(sys.argv)
    window = adminManagement()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()