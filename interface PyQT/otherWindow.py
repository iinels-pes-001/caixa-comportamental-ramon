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
        self.label.setGeometry(QtCore.QRect(40, 50, 71, 16))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 50, 221, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 100, 221, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(120, 160, 110, 22))
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(330, 160, 118, 22))
        self.timeEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.timeEdit.setObjectName("timeEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 230, 211, 31))
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
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 300, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 227, 0);\n"
"font: 87 9pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect (self.openWindow3)



        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 100, 71, 16))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 41, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 160, 41, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 360, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 227, 0);\n"
"font: 87 9pt \"Arial Black\";\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect (self.openWindow4)
        
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
        self.pushButton_3.setText(_translate("MainWindow", "1. TRAINING"))
        self.label_10.setText(_translate("MainWindow", "ANIMAL"))
        self.label_2.setText(_translate("MainWindow", "DATA"))
        self.label_3.setText(_translate("MainWindow", "HORA"))
        self.pushButton_4.setText(_translate("MainWindow", "2. REACTIVATION"))
        self.label_4.setText(_translate("MainWindow", "iBOX"))
        self.label_6.setText(_translate("MainWindow", "II-NELS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
