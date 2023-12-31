# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interface_receptor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 277)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 691, 431))
        self.frame.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.plot_button = QtWidgets.QPushButton(self.frame)
        self.plot_button.setGeometry(QtCore.QRect(390, 60, 75, 23))
        self.plot_button.setObjectName("plot_button")
        self.load_button = QtWidgets.QPushButton(self.frame)
        self.load_button.setGeometry(QtCore.QRect(210, 60, 95, 23))
        self.load_button.setObjectName("load_button")
        self.gerarIP_button = QtWidgets.QPushButton(self.frame)
        self.gerarIP_button.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.gerarIP_button.setObjectName("gerarIP_button")
        self.ip_line = QtWidgets.QLineEdit(self.frame)
        self.ip_line.setGeometry(QtCore.QRect(90, 20, 151, 20))
        self.ip_line.setObjectName("ip_line")
        self.porta_line = QtWidgets.QLineEdit(self.frame)
        self.porta_line.setGeometry(QtCore.QRect(420, 20, 101, 20))
        self.porta_line.setObjectName("porta_line")
        self.porta_label = QtWidgets.QLabel(self.frame)
        self.porta_label.setGeometry(QtCore.QRect(250, 20, 161, 16))
        self.porta_label.setObjectName("porta_label")
        self.receber_button = QtWidgets.QPushButton(self.frame)
        self.receber_button.setGeometry(QtCore.QRect(10, 60, 95, 23))
        self.receber_button.setObjectName("receber_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plot_button.setText(_translate("MainWindow", "Plotar"))
        self.load_button.setText(_translate("MainWindow", "Carregar dados"))
        self.gerarIP_button.setText(_translate("MainWindow", "Gerar IP"))
        self.porta_label.setText(_translate("MainWindow", "Digite a Porta para comunicação:"))
        self.receber_button.setText(_translate("MainWindow", "Receber dados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
