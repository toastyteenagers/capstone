# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'startupmQCaGg.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QTextBrowser,
    QWidget)
import resources_rc

class Ui_LoadScreen(object):
    def setupUi(self, LoadScreen):
        if not LoadScreen.objectName():
            LoadScreen.setObjectName(u"LoadScreen")
        LoadScreen.resize(1312, 831)
        LoadScreen.setStyleSheet(u"background-color: black;")
        self.logo = QTextBrowser(LoadScreen)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(270, 40, 631, 321))
        self.bc_bot = QFrame(LoadScreen)
        self.bc_bot.setObjectName(u"bc_bot")
        self.bc_bot.setGeometry(QRect(260, 350, 661, 31))
        self.bc_bot.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.bc_bot.setFrameShape(QFrame.HLine)
        self.bc_bot.setFrameShadow(QFrame.Sunken)
        self.bc_top = QFrame(LoadScreen)
        self.bc_top.setObjectName(u"bc_top")
        self.bc_top.setGeometry(QRect(240, 10, 671, 31))
        self.bc_top.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.bc_top.setFrameShape(QFrame.HLine)
        self.bc_top.setFrameShadow(QFrame.Sunken)
        self.bc_left = QFrame(LoadScreen)
        self.bc_left.setObjectName(u"bc_left")
        self.bc_left.setGeometry(QRect(240, 10, 31, 371))
        self.bc_left.setFrameShape(QFrame.VLine)
        self.bc_left.setFrameShadow(QFrame.Sunken)
        self.bc_right = QFrame(LoadScreen)
        self.bc_right.setObjectName(u"bc_right")
        self.bc_right.setGeometry(QRect(890, 10, 31, 371))
        self.bc_right.setFrameShape(QFrame.VLine)
        self.bc_right.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(LoadScreen)

        QMetaObject.connectSlotsByName(LoadScreen)
    # setupUi

    def retranslateUi(self, LoadScreen):
        LoadScreen.setWindowTitle(QCoreApplication.translate("LoadScreen", u"Form", None))
        self.logo.setHtml(QCoreApplication.translate("LoadScreen", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/images/images/project_backdown_ascii_art.jpg\" /></p></body></html>", None))
    # retranslateUi

