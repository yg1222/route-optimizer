# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optimizer.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QToolButton, QWidget)
import logo_rc

class Ui_optimizerForm(object):
    def setupUi(self, optimizerForm):
        if not optimizerForm.objectName():
            optimizerForm.setObjectName(u"optimizerForm")
        optimizerForm.resize(679, 724)
        optimizerForm.setAutoFillBackground(False)
        optimizerForm.setSizeGripEnabled(False)
        optimizerForm.setModal(False)
        self.btnOptimize = QPushButton(optimizerForm)
        self.btnOptimize.setObjectName(u"btnOptimize")
        self.btnOptimize.setGeometry(QRect(60, 380, 171, 51))
        font = QFont()
        font.setPointSize(11)
        self.btnOptimize.setFont(font)
        self.btnCopyLink = QPushButton(optimizerForm)
        self.btnCopyLink.setObjectName(u"btnCopyLink")
        self.btnCopyLink.setGeometry(QRect(60, 450, 171, 51))
        self.btnCopyLink.setFont(font)
        self.btnOpenMaps = QPushButton(optimizerForm)
        self.btnOpenMaps.setObjectName(u"btnOpenMaps")
        self.btnOpenMaps.setGeometry(QRect(60, 520, 171, 51))
        self.btnOpenMaps.setFont(font)
        self.txtInputAddresses = QTextEdit(optimizerForm)
        self.txtInputAddresses.setObjectName(u"txtInputAddresses")
        self.txtInputAddresses.setGeometry(QRect(320, 90, 291, 191))
        font1 = QFont()
        font1.setFamilies([u"Noto Serif"])
        font1.setPointSize(9)
        self.txtInputAddresses.setFont(font1)
        self.label = QLabel(optimizerForm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 50, 281, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Display"])
        font2.setPointSize(11)
        self.label.setFont(font2)
        self.txtOptimizedAddresses = QTextEdit(optimizerForm)
        self.txtOptimizedAddresses.setObjectName(u"txtOptimizedAddresses")
        self.txtOptimizedAddresses.setGeometry(QRect(320, 380, 291, 191))
        self.txtOptimizedAddresses.setFont(font1)
        self.label_2 = QLabel(optimizerForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 340, 241, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Variable Display"])
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.label_3 = QLabel(optimizerForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 610, 151, 51))
        self.label_3.setStyleSheet(u"image: url(:/logo/logo.png);")
        self.label_4 = QLabel(optimizerForm)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 110, 141, 41))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Variable Display Semil"])
        font4.setPointSize(18)
        font4.setBold(False)
        self.label_4.setFont(font4)
        self.btnLearnMore = QToolButton(optimizerForm)
        self.btnLearnMore.setObjectName(u"btnLearnMore")
        self.btnLearnMore.setGeometry(QRect(90, 160, 101, 41))
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(False)
        self.btnLearnMore.setFont(font5)

        self.retranslateUi(optimizerForm)

        QMetaObject.connectSlotsByName(optimizerForm)
    # setupUi

    def retranslateUi(self, optimizerForm):
        optimizerForm.setWindowTitle(QCoreApplication.translate("optimizerForm", u"Optimizer", None))
        self.btnOptimize.setText(QCoreApplication.translate("optimizerForm", u"Optimize", None))
        self.btnCopyLink.setText(QCoreApplication.translate("optimizerForm", u"Copy Maps Link", None))
        self.btnOpenMaps.setText(QCoreApplication.translate("optimizerForm", u"Open in Maps", None))
        self.label.setText(QCoreApplication.translate("optimizerForm", u"Paste your addresses in here; line by line", None))
        self.label_2.setText(QCoreApplication.translate("optimizerForm", u"Addresses in optimized order", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("optimizerForm", u"<html><head/><body><p>How to Use?</p></body></html>", None))
        self.btnLearnMore.setText(QCoreApplication.translate("optimizerForm", u"Learn More...", None))
    # retranslateUi

