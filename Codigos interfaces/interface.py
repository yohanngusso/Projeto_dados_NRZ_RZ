import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit
import matplotlib.pyplot as plt
from cryptography.fernet import Fernet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Codificação de Linha")
        self.setGeometry(100, 100, 800, 600)

        # Label e LineEdit para a mensagem
        self.message_label = QLabel("Mensagem:")
        self.message_edit = QLineEdit()

        # Botões
        encrypt_button = QPushButton("Criptografar", self)
        encrypt_button.clicked.connect(self.encrypt_button_clicked)

        nrz_button = QPushButton("Codificar NRZ", self)
        nrz_button.clicked.connect(self.nrz_button_clicked)

        rz_button = QPushButton("Codificar RZ", self)
        rz_button.clicked.connect(self.rz_button_clicked)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_edit)
        layout.addWidget(encrypt_button)
        layout.addWidget(nrz_button)
        layout.addWidget(rz_button)

        # Widget central
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Chave de criptografia
        self.key = Fernet.generate_key()

        # Figuras para exibir os gráficos
        self.figure_nrz = plt.figure()
        self.figure_rz = plt.figure()

    def encrypt_button_clicked(self):
        message = self.message_edit.text()
        ciphertext = encrypt(message, self.key)

        print("Mensagem original:", message)
        print("Mensagem criptografada:", ciphertext)
        print("Chave utilizada:", self.key)

    def nrz_button_clicked(self):
        message = self.message_edit.text()
        binary_message = text_to_binary(message)
        signal = nrz_encoding(binary_message)

        print("Mensagem original:", message)
        print("Mensagem em binário:", binary_message)
        print("Sinal codificado NRZ:", signal)

        self.plot_graph(signal, self.figure_nrz, "Codificação NRZ")

    def rz_button_clicked(self):
        message = self.message_edit.text()
        binary_message = text_to_binary(message)
        signal = rz_encoding(binary_message)

        print("Mensagem original:", message)
        print("Mensagem em binário:", binary_message)
        print("Sinal codificado RZ:", signal)

        self.plot_graph(signal, self.figure_rz, "Codificação RZ")

    def plot_graph(self, signal, figure, title):
        ax = figure.add_subplot(111)
        ax.plot(signal)
        ax.set_title(title)
        ax.set_xlabel("Tempo")
        ax.set_ylabel("Nível de Sinal")

        plt.show()


def encrypt(message, key):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(message.encode())
    return ciphertext.decode()


def text_to_binary(message):
    binary_message = ' '.join(format(ord(char), '08b') for char in message)
    return binary_message


def nrz_encoding(binary_message):
    signal = []
    for bit in binary_message:
        if bit == '0':
            signal.extend([-1, -1])  # Codifica '0' como sinal negativo
        elif bit == '1':
            signal.extend([1, 1])  # Codifica '1' como sinal positivo

    return signal


def rz_encoding(binary_message):
    signal = []
    for bit in binary_message:
        if bit == '0':
            signal.extend([0] * 2)  # Codifica '0' como sinal zero
        elif bit == '1':
            signal.extend([1, -1])  # Codifica '1' como sinal positivo seguido de sinal negativo

    return signal


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
