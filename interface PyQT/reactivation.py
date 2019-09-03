# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reactivation.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setup4(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 490)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 0, 141, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 0, 61, 21))
        self.label_4.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 420, 91, 31))
        self.label_6.setStyleSheet("font: 87 9pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 71, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.routinePeriodMinutes = QtWidgets.QLineEdit(self.centralwidget)
        self.routinePeriodMinutes.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.routinePeriodMinutes.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.routinePeriodMinutes.setText("")
        self.routinePeriodMinutes.setObjectName("routinePeriodMinutes")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 81, 16))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.isLeverRightActive = QtWidgets.QCheckBox(self.centralwidget)
        self.isLeverRightActive.setGeometry(QtCore.QRect(130, 250, 161, 20))
        self.isLeverRightActive.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";")
        self.isLeverRightActive.setObjectName("isLeverRightActive")
        self.isLeverLeftActive = QtWidgets.QCheckBox(self.centralwidget)
        self.isLeverLeftActive.setGeometry(QtCore.QRect(130, 290, 161, 20))
        self.isLeverLeftActive.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";")
        self.isLeverLeftActive.setObjectName("isLeverLeftActive")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 161, 21))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 9pt \"Arial Black\";")
        self.label_5.setObjectName("label_5")
        self.numberTouchesForReward = QtWidgets.QLineEdit(self.centralwidget)
        self.numberTouchesForReward.setGeometry(QtCore.QRect(200, 160, 113, 20))
        self.numberTouchesForReward.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.numberTouchesForReward.setText("")
        self.numberTouchesForReward.setObjectName("numberTouchesForReward")
        self.routineStartTime = QtWidgets.QPushButton(self.centralwidget)
        self.routineStartTime.setGeometry(QtCore.QRect(100, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.routineStartTime.setFont(font)
        self.routineStartTime.setStyleSheet("background-color: rgb(0, 227, 0);\n"
"font: 87 9pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);")
        self.routineStartTime.setObjectName("routineStartTime")
        self.routineStopTime = QtWidgets.QPushButton(self.centralwidget)
        self.routineStopTime.setGeometry(QtCore.QRect(280, 350, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.routineStopTime.setFont(font)
        self.routineStopTime.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.routineStopTime.setObjectName("routineStopTime")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 501, 21))
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
        self.label.setText(_translate("MainWindow", "REACTIVATION"))
        self.label_4.setText(_translate("MainWindow", "iBOX"))
        self.label_6.setText(_translate("MainWindow", "IIN-ELS"))
        self.label_2.setText(_translate("MainWindow", "TEMPO:"))
        self.label_3.setText(_translate("MainWindow", "ALAVANCAS:"))
        self.isLeverRightActive.setText(_translate("MainWindow", "DIREITA"))
        self.isLeverLeftActive.setText(_translate("MainWindow", "ESQUERDA"))
        self.label_5.setText(_translate("MainWindow", "RECOMPENSA/BARRA:"))
        self.routineStartTime.setText(_translate("MainWindow", "► RUN"))
        self.routineStopTime.setText(_translate("MainWindow", "■ STOP"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setup4(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
