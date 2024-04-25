from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import numpy as np
from users import load_users, load_admins, delete_from_database


class adminManagement(QWidget):
    def __init__(self):
        super(adminManagement, self).__init__()
        # background-color: #31394c

        self.users_tab = []
        self.window = QVBoxLayout()

        # self.setStyle()
        self.createUI()

    def gotoAddUser(self):
        print("go to add user screen")

    def load(self):
        admins = load_admins()
        users = load_users()
        for i in admins:
            self.active_users.append(i)
        for j in users:
            self.active_users.append(j)

    def createUI(self):
        self.active_users = []

        self.layout = QVBoxLayout()
        self.scroll = QScrollArea()
        self.group = QWidget()
        # self.group.setStyleSheet("background-color: #202633;")
        self.group_layout = QVBoxLayout()

        self.top_layout = QFormLayout()
        self.addUser = QLabel("Add a new User: ")
        self.addUserButton = QPushButton("Add User")
        self.addUserButton.clicked.connect(self.gotoAddUser)
        self.top_layout.addRow(self.addUser, self.addUserButton)
        self.layout.addLayout(self.top_layout)

        self.group.setLayout(self.group_layout)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.group)

        self.layout.addWidget(self.scroll)
        self.window.addLayout(self.layout)
        self.setLayout(self.window)

        self.load()

        self.setWindowTitle("System Management")
        self.setGeometry(0, 0, 1920, 1080)
        # self.setStyleSheet("background-color: #31394c")

        for user in self.active_users:
            self.listUsers(user)

    def listUsers(self, user):
        # User and Delete
        user_layout = QHBoxLayout()
        user_layout.setAlignment(Qt.AlignTop)
        # User and Drop Down
        temp_user = user_info(user, self)
        deleteButton = QPushButton("Delete")

        deleteButton.clicked.connect(lambda: self.delete_user(user))
        # deleteButton.setStyleSheet("background-color: #31394c;")
        user_layout.addWidget(temp_user)
        if user.get_level() == 0:
            user_layout.addWidget(deleteButton)

        self.group_layout.addLayout(user_layout)

    def delete_user(self, user):
        delete_from_database(user.get_name(), user.get_encodings())
        self.clear_whole_layout(self.window)
        self.createUI()
        self.setGeometry(0, 0, 1920, 1080)

    def clear_whole_layout(self, layout):
        if isinstance(layout, QScrollArea):
            widget = layout.widget()
            layout = widget.layout()
        if layout is None:
            return;
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
        self.start()

    def createUI(self):
        # User Banner
        self.layout = QVBoxLayout()
        # User Info
        self.bannerLayout = QFormLayout()

        self.name = QLabel(self.user.get_name())
        self.toggleButton = QPushButton('Arrow Down')
        self.toggleButton.clicked.connect(self.toggle_info)
        self.bannerLayout.addRow(self.name, self.toggleButton)
        self.bannerLayout.setFormAlignment(Qt.AlignTop)
        self.bannerLayout.setFormAlignment(Qt.AlignLeft)

        self.layout.addLayout(self.bannerLayout)

        self.toggleWidget = QWidget()
        self.toggleWidget.setStyleSheet("background-color: #31394c;")

        self.load_data()

        self.layout.addWidget(self.toggleWidget)

        self.setLayout(self.layout)

    def start(self):
        self.toggleWidget.setVisible(False)
        self.clear(self.infoLayout)
        self.clear_banner()

    def toggle_info(self):
        if self.toggleWidget.isVisible():
            self.toggleWidget.setVisible(False)
            self.clear(self.infoLayout)
            self.clear_banner()
        else:
            self.toggleWidget.setVisible(True)
            self.load_data()
            # self.createUI()

    def startClear(self):
        if self.toggleWidget.isVisible():
            self.toggleWidget.setVisible(False)
            self.clear(self.infoLayout)
            self.clear_banner()

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
        self.infoLayout.setFormAlignment(Qt.AlignTop)
        self.infoLayout.setFormAlignment(Qt.AlignLeft)

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
        self.container.setStyleSheet("background-color: #6a6a6a;")
        self.container.setLayout(self.use_layout)
        self.infoLayout.addRow(self.container)

        self.container2 = QWidget()
        self.container2.setStyleSheet("background-color: #6a6a6a;")
        self.container2.setLayout(self.infoLayout)
        self.bannerLayout.addRow(self.container2)


def main():
    app = QApplication(sys.argv)
    window = adminManagement()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()