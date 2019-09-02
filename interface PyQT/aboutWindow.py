# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 493)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 71, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 110, 341, 271))
        self.textEdit.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
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
        self.label.setText(_translate("MainWindow", "SOBRE"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:9pt; color:#00ff00;\">O </span><span style=\" font-family:\'-apple-system\'; font-size:9pt; font-weight:600; color:#00ff00;\">iBOX</span><span style=\" font-family:\'-apple-system\'; font-size:9pt; color:#00ff00;\"> é uma aplicação Python a ser executada em um modelo Raspberry (computador de placa única do tamanho reduzido) para automação de uma caixa comportamental posível de ser configurada remotamente.<br /><br /><br />Desenvolvedores:<br />Alex Aquino <br />Bruno Spinelli <br />Erika </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:9pt; color:#00ff00;\">Flávia Freire</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:9pt; color:#00ff00;\">Johseph Paballo<br />Larissa Pinto<br />Pablo Queiroz<br />Rodrigo Amaral<br />Tâmara Nunes<br />Tássia Nunes<br /></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'-apple-system\'; font-size:9pt; color:#00ff00;\"><br />Para saber mais, acesse:<br /></span><a href=\"https://github.com/iinels-pes-001/icx\"><span style=\" font-size:8pt; text-decoration: underline; color:#00ff00;\">GitHub - iBOX</span></a></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "iBOX"))
        self.label_6.setText(_translate("MainWindow", "II-NELS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
