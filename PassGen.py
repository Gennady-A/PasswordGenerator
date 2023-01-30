# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PassGen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 300)
        MainWindow.setStyleSheet(u"color: rgb(161, 187, 210);\n"
"background-color: rgb(27, 48, 67);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(65, 68, 79);\n"
"box-shadow: 0px 0px 0px #000;\n"
"border:4px solid rgb(65, 68, 79);")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 2, 4, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"background-color: rgb(65, 68, 79);\n"
"box-shadow: 0px 0px 0px #000;\n"
"border:4px solid rgb(65, 68, 79);")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 4)

        self.Generate_But = QPushButton(self.centralwidget)
        self.Generate_But.setObjectName(u"Generate_But")
        font = QFont()
        font.setPointSize(14)
        font.setKerning(True)
        self.Generate_But.setFont(font)
        self.Generate_But.setStyleSheet(u"background-color: rgb(12, 39, 62);\n"
"color: rgb(12, 39, 62);\n"
"background-color: rgb(117, 166, 210);")

        self.gridLayout.addWidget(self.Generate_But, 0, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.PasswordLength_Lab = QLabel(self.centralwidget)
        self.PasswordLength_Lab.setObjectName(u"PasswordLength_Lab")

        self.horizontalLayout.addWidget(self.PasswordLength_Lab)

        self.PasswordLength_Sld = QSlider(self.centralwidget)
        self.PasswordLength_Sld.setObjectName(u"PasswordLength_Sld")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PasswordLength_Sld.sizePolicy().hasHeightForWidth())
        self.PasswordLength_Sld.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setStyleStrategy(QFont.PreferDefault)
        self.PasswordLength_Sld.setFont(font1)
        self.PasswordLength_Sld.setStyleSheet(u"")
        self.PasswordLength_Sld.setMinimum(1)
        self.PasswordLength_Sld.setMaximum(30)
        self.PasswordLength_Sld.setPageStep(1)
        self.PasswordLength_Sld.setSliderPosition(1)
        self.PasswordLength_Sld.setOrientation(Qt.Horizontal)
        self.PasswordLength_Sld.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout.addWidget(self.PasswordLength_Sld)

        self.PasswordLengthNumber_Lab = QLabel(self.centralwidget)
        self.PasswordLengthNumber_Lab.setObjectName(u"PasswordLengthNumber_Lab")

        self.horizontalLayout.addWidget(self.PasswordLengthNumber_Lab)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DecryptionTryPerSecond_Lab = QLabel(self.centralwidget)
        self.DecryptionTryPerSecond_Lab.setObjectName(u"DecryptionTryPerSecond_Lab")

        self.horizontalLayout_3.addWidget(self.DecryptionTryPerSecond_Lab)

        self.DecryptionTryPerSecond_Sld = QSlider(self.centralwidget)
        self.DecryptionTryPerSecond_Sld.setObjectName(u"DecryptionTryPerSecond_Sld")
        self.DecryptionTryPerSecond_Sld.setMinimum(1000000)
        self.DecryptionTryPerSecond_Sld.setMaximum(100000000)
        self.DecryptionTryPerSecond_Sld.setSingleStep(1000000)
        self.DecryptionTryPerSecond_Sld.setPageStep(1000000)
        self.DecryptionTryPerSecond_Sld.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.DecryptionTryPerSecond_Sld)

        self.DecryptionTryPerSecondNumber_Lab = QLabel(self.centralwidget)
        self.DecryptionTryPerSecondNumber_Lab.setObjectName(u"DecryptionTryPerSecondNumber_Lab")

        self.horizontalLayout_3.addWidget(self.DecryptionTryPerSecondNumber_Lab)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Number_Chb = QCheckBox(self.centralwidget)
        self.Number_Chb.setObjectName(u"Number_Chb")

        self.verticalLayout.addWidget(self.Number_Chb)

        self.Latin_Chb = QCheckBox(self.centralwidget)
        self.Latin_Chb.setObjectName(u"Latin_Chb")

        self.verticalLayout.addWidget(self.Latin_Chb)

        self.Cyrilic_Chb = QCheckBox(self.centralwidget)
        self.Cyrilic_Chb.setObjectName(u"Cyrilic_Chb")

        self.verticalLayout.addWidget(self.Cyrilic_Chb)

        self.SpecialSymbols_Chb = QCheckBox(self.centralwidget)
        self.SpecialSymbols_Chb.setObjectName(u"SpecialSymbols_Chb")

        self.verticalLayout.addWidget(self.SpecialSymbols_Chb)


        self.gridLayout.addLayout(self.verticalLayout, 2, 3, 2, 1)

        self.Password_Lab = QLabel(self.centralwidget)
        self.Password_Lab.setObjectName(u"Password_Lab")
        font2 = QFont()
        font2.setPointSize(14)
        self.Password_Lab.setFont(font2)

        self.gridLayout.addWidget(self.Password_Lab, 0, 0, 1, 2)

        self.DecryptionTimeAnswer_Lab = QLabel(self.centralwidget)
        self.DecryptionTimeAnswer_Lab.setObjectName(u"DecryptionTimeAnswer_Lab")

        self.gridLayout.addWidget(self.DecryptionTimeAnswer_Lab, 5, 1, 1, 3)

        self.DecryptionTime_Lab = QLabel(self.centralwidget)
        self.DecryptionTime_Lab.setObjectName(u"DecryptionTime_Lab")

        self.gridLayout.addWidget(self.DecryptionTime_Lab, 5, 0, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"background-color: rgb(65, 68, 79);\n"
"box-shadow: 0px 0px 0px #000;\n"
"border:4px solid rgb(65, 68, 79);")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Generate_But.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0413\u0415\u041d\u0415\u0420\u0418\u0420\u041e\u0412\u0410\u0422\u042c", None))
        self.PasswordLength_Lab.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043f\u0430\u0440\u043e\u043b\u044f: ", None))
        self.PasswordLengthNumber_Lab.setText(QCoreApplication.translate("MainWindow", u" 1 ", None))
        self.DecryptionTryPerSecond_Lab.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u043b\u043e\u043c(\u043f\u043e\u043f\u044b\u0442\u043a\u0438 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0443): ", None))
        self.DecryptionTryPerSecondNumber_Lab.setText(QCoreApplication.translate("MainWindow", u" 1000000 ", None))
        self.Number_Chb.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0438\u0444\u0440\u044b", None))
        self.Latin_Chb.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0442\u0438\u043d\u0438\u0446\u0430", None))
        self.Cyrilic_Chb.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0438\u0440\u0438\u043b\u0438\u0446\u0430", None))
        self.SpecialSymbols_Chb.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0435\u0446. \u0441\u0438\u043c\u0432\u043e\u043b\u044b", None))
        self.Password_Lab.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a\u043e\u0439-\u0442\u043e \u043f\u0430\u0440\u043e\u043b\u044c...", None))
        self.DecryptionTimeAnswer_Lab.setText(QCoreApplication.translate("MainWindow", u"0\u0441", None))
        self.DecryptionTime_Lab.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043d\u0430 \u043f\u043e\u0434\u0431\u043e\u0440: ", None))
    # retranslateUi

