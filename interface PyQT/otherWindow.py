# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from training import Ui_MainWindow3
from reactivation import Ui_MainWindow4


class Ui_MainWindow(object):

    def openWindow3 (self):
        self.window = QtWidgets.QMainWindow ()
        self.ui = Ui_MainWindow3 ()
        self.ui.setup3 (self.window)
        self.window.show ()


    def openWindow4 (self):
        self.window = QtWidgets.QMainWindow ()
        self.ui = Ui_MainWindow4 ()
        self.ui.setup4 (self.window)
        self.window.show ()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(506, 495)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 60, 71, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.userName = QtWidgets.QLineEdit(self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(180, 60, 221, 20))
        self.userName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userName.setObjectName("userName")
        self.animalIdentificationNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.animalIdentificationNumber.setGeometry(QtCore.QRect(170, 130, 111, 21))
        self.animalIdentificationNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.animalIdentificationNumber.setObjectName("animalIdentificationNumber")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 190, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(170, 0, 255);\n"
"font: 87 16pt \"Arial Black\";")
        self.label_5.setObjectName("label_5")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(160, 260, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton3.setFont(font)
        self.pushButton3.setStyleSheet("background-color: rgb(0, 227, 0);\n"
"font: 87 9pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton3.setObjectName("pushButton3")

        self.pushButton3.clicked.connect (self.openWindow3)
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(80, 130, 71, 16))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_10.setObjectName("label_10")
        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(QtCore.QRect(160, 340, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton4.setFont(font)
        self.pushButton4.setStyleSheet("background-color: rgb(0, 227, 0);\n"
"font: 87 9pt \"Arial Black\";\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton4.setObjectName("pushButton4")

        self.pushButton4.clicked.connect (self.openWindow4)

        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 0, 61, 21))
        self.label_4.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 420, 91, 31))
        self.label_6.setStyleSheet("font: 87 9pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(220, 110, 21, 16))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(350, 110, 41, 16))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_12.setObjectName("label_12")
        self.animalName = QtWidgets.QLineEdit(self.centralwidget)
        self.animalName.setGeometry(QtCore.QRect(320, 130, 101, 21))
        self.animalName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.animalName.setObjectName("animalName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "USUÁRIO"))
        self.label_5.setText(_translate("MainWindow", "ESCOLHA ROTINA"))
        self.pushButton3.setText(_translate("MainWindow", "1. TRAINING"))
        self.label_10.setText(_translate("MainWindow", "ANIMAL"))
        self.pushButton4.setText(_translate("MainWindow", "2. REACTIVATION"))
        self.label_4.setText(_translate("MainWindow", "iBOX"))
        self.label_6.setText(_translate("MainWindow", "IIN-ELS"))
        self.label_11.setText(_translate("MainWindow", "Nº"))
        self.label_12.setText(_translate("MainWindow", "NOME"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
