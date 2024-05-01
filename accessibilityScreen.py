from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accessibility:
    backClicked = QtCore.pyqtSignal()    

    def __init__(self, parent=None):
        # Initialize UI components
        self.parent = parent
        self.setupUi(parent)

    def setupUi(self, Accessibility):
        Accessibility.setObjectName("Accessibility")
        Accessibility.resize(1920, 1080)
        Accessibility.setStyleSheet("background-color: black;")
        
        # Create and configure widgets here
        # ...

        # Example widget setup
        self.topRightLine = QtWidgets.QFrame(Accessibility)
        self.topRightLine.setGeometry(QtCore.QRect(1290, 30, 621, 21))
        self.topRightLine.setStyleSheet("background-color: gray;")
        self.topRightLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.topRightLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        # Continue setting up other widgets and signal connections
        # ...

        self.backButton = QtWidgets.QPushButton("Back", Accessibility)
        self.backButton.clicked.connect(self.onBackClicked)
        
        # Raise layers to adjust z-index if necessary
        self.topRightLine.raise_()
        # Continue for other components as needed

        # It's good practice to handle retranslations and meta object connections here
        self.retranslateUi(Accessibility)
        QtCore.QMetaObject.connectSlotsByName(Accessibility)
        
    def onBackClicked(self):
        self.backClicked.emit()
        if isinstance(self.parent, QtWidgets.QStackedWidget):
            self.parent.setCurrentIndex(2)
        # Assuming you have a method like self.ui_init_conf_main.incrementCount()
        # self.ui_init_conf_main.incrementCount()

    def retranslateUi(self, Accessibility):
        _translate = QtCore.QCoreApplication.translate
        Accessibility.setWindowTitle(_translate("Accessibility", "Form"))
        self.InitConfTitle.setText(_translate("Accessibility", "First Time Setup Sequence"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Accessibility = QtWidgets.QWidget()
    ui = Ui_Accessibility(Accessibility)
    Accessibility.showFullScreen()
    Accessibility.show()
    sys.exit(app.exec())

