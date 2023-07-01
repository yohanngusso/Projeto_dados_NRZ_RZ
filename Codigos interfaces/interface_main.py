from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 277)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 691, 431))
        self.frame.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.message_line = QtWidgets.QLineEdit(self.frame)
        self.message_line.setGeometry(QtCore.QRect(10, 20, 221, 20))
        self.message_line.setObjectName("message_line")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 141, 16))
        self.label_2.setObjectName("label_2")
        self.plot_button = QtWidgets.QPushButton(self.frame)
        self.plot_button.setGeometry(QtCore.QRect(380, 20, 75, 23))
        self.plot_button.setObjectName("plot_button")
        self.load_button = QtWidgets.QPushButton(self.frame)
        self.load_button.setGeometry(QtCore.QRect(250, 20, 95, 23))
        self.load_button.setObjectName("load_button")
        self.send_button = QtWidgets.QPushButton(self.frame)
        self.send_button.setGeometry(QtCore.QRect(510, 20, 75, 23))
        self.send_button.setObjectName("send_button")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 50, 141, 16))
        self.label.setObjectName("label")
        self.ip = QtWidgets.QLineEdit(self.frame)
        self.ip.setGeometry(QtCore.QRect(10, 70, 221, 20))
        self.ip.setObjectName("ip")
        self.porta_line = QtWidgets.QLineEdit(self.frame)
        self.porta_line.setGeometry(QtCore.QRect(10, 120, 221, 20))
        self.porta_line.setObjectName("porta_line")
        self.porta_label = QtWidgets.QLabel(self.frame)
        self.porta_label.setGeometry(QtCore.QRect(10, 100, 231, 16))
        self.porta_label.setObjectName("porta_label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Digite o texto aqui:"))
        self.plot_button.setText(_translate("MainWindow", "Plotar"))
        self.load_button.setText(_translate("MainWindow", "Carregar dados"))
        self.send_button.setText(_translate("MainWindow", "Enviar"))
        self.label.setText(_translate("MainWindow", "Digite o IP do host receptor:"))
        self.porta_label.setText(_translate("MainWindow", "Digite a Porta desejada para comunicação:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
