import sys
import socket
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
        self.grafic_button = QtWidgets.QPushButton(self.frame)
        self.grafic_button.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.grafic_button.setObjectName("grafic_button")
        self.carregar_button = QtWidgets.QPushButton(self.frame)
        self.carregar_button.setGeometry(QtCore.QRect(10, 80, 95, 23))
        self.carregar_button.setObjectName("carregar_button")
        self.gerarIP_button = QtWidgets.QPushButton(self.frame)
        self.gerarIP_button.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.gerarIP_button.setObjectName("gerarIP_button")
        self.gerarIP_button.clicked.connect(self.gerarIP)
        self.ip_line = QtWidgets.QLineEdit(self.frame)
        self.ip_line.setGeometry(QtCore.QRect(110, 20, 151, 20))
        self.ip_line.setObjectName("ip_line")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.gerarIP_button.clicked.connect(self.gerarIP)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grafic_button.setText(_translate("MainWindow", "Plotar"))
        self.carregar_button.setText(_translate("MainWindow", "Carregar dados"))
        self.gerarIP_button.setText(_translate("MainWindow", "Gerar IP"))

    def gerarIP(self):
        ip = socket.gethostbyname(socket.gethostname())
        self.ip_line.setText(ip)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
