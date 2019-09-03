# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from otherWindow import Ui_MainWindow
from aboutWindow import Ui_MainWindow1

class Ui_Form(object):
    
    def openWindow (self):
        self.window = QtWidgets.QMainWindow ()
        self.ui = Ui_MainWindow ()
        self.ui.setupUi (self.window)
        self.window.show ()

    def openWindow1 (self):
        self.window = QtWidgets.QMainWindow ()
        self.ui = Ui_MainWindow1 ()
        self.ui.setup1(self.window)
        self.window.show ()

      
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(934, 649)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 931, 681))
        self.label.setStyleSheet("image: url(:/newPrefix/IBOX.jpeg);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(510, 530, 141, 31))
        self.pushButton.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 207, 93);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect (self.openWindow)

        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 530, 141, 31))
        self.pushButton_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(255, 207, 93);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect (self.openWindow1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton.setText(_translate("Form", "INICIAR"))
        self.pushButton_2.setText(_translate("Form", "SOBRE"))

             
import source


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
