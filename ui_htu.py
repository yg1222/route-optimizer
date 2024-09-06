# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'how_to_use.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QTextBrowser,
    QWidget)
import opt_resource_rc

class Ui_htuWidget(object):
    def setupUi(self, htuWidget):
        if not htuWidget.objectName():
            htuWidget.setObjectName(u"htuWidget")
        htuWidget.resize(523, 643)
        icon = QIcon()
        icon.addFile(u":/images/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        htuWidget.setWindowIcon(icon)
        self.textBrowser = QTextBrowser(htuWidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 90, 471, 501))
        self.label = QLabel(htuWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 40, 201, 41))
        font = QFont()
        font.setFamilies([u"Noto Serif"])
        font.setPointSize(14)
        self.label.setFont(font)

        self.retranslateUi(htuWidget)

        QMetaObject.connectSlotsByName(htuWidget)
    # setupUi

    def retranslateUi(self, htuWidget):
        htuWidget.setWindowTitle(QCoreApplication.translate("htuWidget", u"Form", None))
        self.textBrowser.setHtml(QCoreApplication.translate("htuWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt;\">Paste your addresses in the &quot;Addresses&quot; text-box, the one to the top-right (you must include an origin addres"
                        "s as the first address). <br />Each address should start in a new line. <br />Format: &quot;123 Example Road, City, Province&quot;</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt;\">Click on the &quot;Optimize&quot; button while the &quot;Addresses&quot; text-box contains your addresses to calculate and display your addresses in an optimized order for better mileage and fuel efficiency.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Ben"
                        "gali,sans-serif, sans-serif'; font-size:12pt;\">Click the &quot;Open in Maps&quot; button to open a Google Maps page with an itinerary in the optimized order.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt;\">Click on the &quot;Copy Maps Link&quot; to copy a link that will generate a Google Maps page with an itinerary in the optimized order. This link can be shared with a driver or a colleague. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-size:8pt;\"><br /></span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Nas"
                        "kh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; text-decoration: underline; color:#202124;\">On an Android device:</span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:8pt; text-decoration: underline;\"> </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:8pt; background-color:transparent;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#202124;\">If </span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans"
                        " Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#000000;\">Google Maps app for Android </span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#202124;\">is installed and active, the URL launches Google Maps in the Maps app and performs the requested action.</span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif';\"> </span></li>\n"
"<li style=\" font-size:8pt; background-color:transparent;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#202124;\">If the Google Maps a"
                        "pp is not installed or is disabled, the URL launches Google Maps in a browser and performs the requested action.</span> </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; text-decoration: underline; color:#202124;\">On an iOS device:</span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:8pt; text-decoration: underline;\"> </span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:8pt; background-color:transparent;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#202124;\">If </span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#000000;\">Google Maps app for iOS </span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#202124;\">is installed, the URL launches Google Maps in the Maps app and performs the requested action.</span><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif';\"> </span></li>\n"
"<li style=\" font-size:8pt; background-color:tran"
                        "sparent;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#202124;\">If the Google Maps app is not installed, the URL launches Google Maps in a browser and performs the requested action.</span> </li></ul>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px; line-height:115%; background-color:transparent;\"><span style=\" font-family:'Roboto,Noto Sans,Noto Sans JP,Noto Sans KR,Noto Naskh Arabic,Noto Sans Thai,Noto Sans Hebrew,Noto Sans Bengali,sans-serif, sans-serif'; font-size:12pt; color:#202124;\">On any other device, the URL launches Google Maps in a browser and performs the requested action.</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("htuWidget", u"How to Use", None))
    # retranslateUi

