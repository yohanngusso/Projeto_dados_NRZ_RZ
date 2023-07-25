import sys
import socket
import plotly.graph_objects as go
import netifaces
import base64
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cryptography.fernet import Fernet


def decrypt(ciphertext, key):
    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(ciphertext.encode())
    return plaintext.decode()


def binary_to_text(binary_message):
    binary_message = binary_message.replace(" ", "")  # Remove os espaços em branco
    chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    message = ''.join(chr(int(char, 2)) for char in chars)
    return message


def nrz_decoding(signal):
    binary_message = ""
    for i in range(0, len(signal), 2):
        if signal[i] == -1 and signal[i+1] == -1:  # Sinal negativo codifica '0'
            binary_message += "0"
        elif signal[i] == 1 and signal[i+1] == 1:  # Sinal positivo codifica '1'
            binary_message += "1"
    return binary_message


def rz_decoding(signal):
    binary_message = ""
    for i in range(0, len(signal), 2):
        if signal[i] == 0 and signal[i+1] == 0:  # Sinal zero codifica '0'
            binary_message += "0"
        elif signal[i] == 1 and signal[i+1] == -1:  # Sinal positivo seguido de negativo codifica '1'
            binary_message += "1"
    return binary_message


def about(nrzcoded_message, rzcoded_message, key):
    # Decodifica NRZ
    binary_message_nrz = nrz_decoding(nrzcoded_message)
    # Decodifica RZ
    binary_message_rz = rz_decoding(rzcoded_message)
    # Converte binário para texto
    decrypted_message = binary_to_text(binary_message_rz)
    # Gera a chave a partir da chave fornecida codificada em base64
    key = base64.urlsafe_b64decode(key)

    decrypted_message = decrypt(decrypted_message, key)

    return decrypted_message


def plot_graphs(mensagem_codificada_nrz, mensagem_codificada_rz):
    # Criação do gráfico NRZ utilizando Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(mensagem_codificada_nrz))), y=mensagem_codificada_nrz, mode='lines'))

    fig.update_layout(
        title="Codificação NRZ",
        xaxis_title="Tempo",
        yaxis_title="Nível de Sinal"
    )
    fig.show()

    # Criação do gráfico RZ utilizando Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(mensagem_codificada_rz))), y=mensagem_codificada_rz, mode='lines'))

    fig.update_layout(
        title="Codificação RZ",
        xaxis_title="Tempo",
        yaxis_title="Nível de Sinal"
    )
    fig.show()


# classe para uma nova janela
class OutputWindow(QtWidgets.QDialog):
    def __init__(self, mensagem_codificada_nrz, mensagem_codificada_rz):
        super(OutputWindow, self).__init__()

        self.setWindowTitle("Output Window")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QtWidgets.QVBoxLayout()

        self.nrzcoded_label = QtWidgets.QLabel("Mensagem codificada NRZ: " + mensagem_codificada_nrz)
        self.rzcoded_label = QtWidgets.QLabel("Mensagem codificada RZ: " + mensagem_codificada_rz)

        self.layout.addWidget(self.nrzcoded_label)
        self.layout.addWidget(self.rzcoded_label)

        self.setLayout(self.layout)


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
        self.grafic_button.setGeometry(QtCore.QRect(390, 60, 75, 23))
        self.grafic_button.setObjectName("grafic_button")
        self.carregar_button = QtWidgets.QPushButton(self.frame)
        self.carregar_button.setGeometry(QtCore.QRect(210, 60, 95, 23))
        self.carregar_button.setObjectName("carregar_button")
        self.gerarIP_button = QtWidgets.QPushButton(self.frame)
        self.gerarIP_button.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.gerarIP_button.setObjectName("gerarIP_button")
        self.gerarIP_button.clicked.connect(self.gerarIP_button_clicked)
        self.ip_line = QtWidgets.QLineEdit(self.frame)
        self.ip_line.setGeometry(QtCore.QRect(90, 20, 151, 20))
        self.ip_line.setObjectName("ip_line")
        self.porta_line = QtWidgets.QLineEdit(self.frame)
        self.porta_line.setGeometry(QtCore.QRect(460, 20, 101, 20))
        self.porta_line.setObjectName("porta_line")
        self.porta_label = QtWidgets.QLabel(self.frame)
        self.porta_label.setGeometry(QtCore.QRect(250, 20, 201, 16))
        self.porta_label.setObjectName("porta_label")
        self.receber_button = QtWidgets.QPushButton(self.frame)
        self.receber_button.setGeometry(QtCore.QRect(10, 60, 95, 23))
        self.receber_button.setObjectName("receber_button")
        self.receber_button.clicked.connect(self.receber_button_clicked)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.grafic_button.setText(_translate("MainWindow", "Plotar"))
        self.carregar_button.setText(_translate("MainWindow", "Carregar dados"))
        self.gerarIP_button.setText(_translate("MainWindow", "Gerar IP"))
        self.porta_label.setText(_translate("MainWindow", "Digite a Porta para comunicação:"))
        self.receber_button.setText(_translate("MainWindow", "Receber dados"))

    def gerarIP_button_clicked(self):
        interfaces = netifaces.interfaces()
        ipv4 = None
        for interface in interfaces:
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                ipv4 = addresses[netifaces.AF_INET][0]['addr']
                break

        if ipv4 is not None:
            self.ip_line.setText(ipv4)
        else:
            self.ip_line.setText("Endereço IPv4 não encontrado")

    def receber_button_clicked(self):
        HOST = '0.0.0.0'  # Endereço IP do receptor (deixe como '0.0.0.0' para aceitar conexões de qualquer IP)
        PORT = int(self.porta_line.text())  # Porta de comunicação
    
        if not PORT:
            QMessageBox.warning(MainWindow, "Atenção", "Digite uma mensagem antes de carregar.")
            return

        # Cria o socket TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Liga o socket ao endereço IP e porta
        s.bind((HOST, PORT))

        # Aguarda a conexão do emissor
        s.listen()

        print("Aguardando conexão do emissor...")
        conn, addr = s.accept()
        print("Conexão estabelecida com o emissor:", addr)

        # Recebe a mensagem codificada NRZ
        data_nrz = conn.recv(1024)
        mensagem_codificada_nrz = data_nrz.decode()

        # Recebe a mensagem codificada RZ
        data_rz = conn.recv(1024)
        mensagem_codificada_rz = data_rz.decode()

        # Chama a função 'about' para decodificar e descriptografar as mensagens
        key, ok = QtWidgets.QInputDialog.getText(MainWindow, "Digite a Chave", "Chave:", QtWidgets.QLineEdit.Normal)
        if ok and key:
            # Utilize a chave digitada pelo usuário aqui
            print("Chave digitada:", key)

        key = about(mensagem_codificada_nrz, mensagem_codificada_rz, key)


        # Cria a janela de saída
        self.output_window = OutputWindow(
            mensagem_codificada_nrz,
            mensagem_codificada_rz
        )
        self.output_window.exec_()

        # Fecha a conexão
        conn.close()
        s.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
