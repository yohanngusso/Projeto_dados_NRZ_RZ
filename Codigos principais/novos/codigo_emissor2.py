import sys, socket
import plotly.graph_objects as go
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cryptography.fernet import Fernet


# Funções Nao utilizar no N
def encrypt(message, key):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(message.encode())
    return ciphertext.decode()

# Usa no N
def text_to_binary(message): 
    binary_message = ' '.join(format(ord(char), '08b') for char in message)
    return binary_message


def nrz_encoding(binary_message):
    signal = []
    for bit in binary_message:
        if bit == '0':
            signal.extend([1,1])  # Codifica '0' como sinal negativo
        elif bit == '1':
            signal.extend([-1,-1])  # Codifica '1' como sinal positivo
    return signal


def nrzI_encoding(binary_message):
    #valor auxiliar
    signal = [5]
    for bit in binary_message:
        if bit == '0' and signal [-1] == 1:
            signal.extend([1,1])  
        elif bit == '0' and signal [-1] == -1:
            signal.extend([-1,-1])  
        elif bit == '1' and signal [-1] == 1:
            signal.extend([-1,-1])  
        elif bit == '1' and signal [-1] == -1:
            signal.extend([1,1])  
        else:
            signal.remove(5)
            signal.extend([1,1])  

    return signal


def rz_encoding(binary_message):
    signal = []
    for bit in binary_message:
        if bit == '0':
            signal.extend([-1,-1,0,0])  # Codifica '0' como sinal zero
        elif bit == '1':
            signal.extend([1,1,0,0])  # Codifica '1' como sinal positivo seguido de sinal negativo
    return signal


def about(message):
    # Gerar uma nova chave válida para uso com o algoritmo Fernet
    key = Fernet.generate_key()
    # Criptografa a mensagem
    #mensagem_criptografada = encrypt(message, key)
    # Transforma para binário
    mensagem_binaria = text_to_binary(message)
    
    # Codifica em NRZ - L
    mensagem_codificada_nrz = nrz_encoding(mensagem_binaria)

    # Codifica em NRZ - I
    mensagem_codificada_nrzI = nrzI_encoding(mensagem_binaria)

    # Codifica em RZ
    mensagem_codificada_rz = rz_encoding(mensagem_binaria)


    return message, key, mensagem_binaria, mensagem_codificada_nrz, mensagem_codificada_rz, mensagem_codificada_nrzI


def plot_graphs(mensagem_codificada_nrz, mensagem_codificada_rz, mensagem_codificada_nrzI):
   

#________________________________________________ PARTE NRZ __________________________________________


    fig = go.Figure()

    #---------------------- Para ajustar o grafico NRZ 
    x_auxNRZ=[0]
    for i in range(len(mensagem_codificada_nrz)):
      
        if i == 0:
            x_auxNRZ.append(1)   

        if (x_auxNRZ[i-1]!=x_auxNRZ[i]) and i!=0:
            x_auxNRZ.append(x_auxNRZ[i])
        
        if x_auxNRZ[i-1]==x_auxNRZ[i]  and i!=0:
            x_auxNRZ.append((x_auxNRZ[i])+1)     
    #--------------------------------------------------

    # Criação do gráfico NRZ utilizando Plotly
    fig.add_trace(go.Scatter(x=x_auxNRZ, y=mensagem_codificada_nrz, mode='lines'))
    fig.update_layout(
        title="Codificação NRZ",
        xaxis_title="Tempo",
        yaxis_title="Nível de Sinal"
    )
    fig.show()

#________________________________________________ PARTE NRZ - I ________________________________________
   
    fig = go.Figure()

    #---------------------- Para ajustar o grafico NRZ - I
    x_auxNRZI=[0]
    for i in range(len(mensagem_codificada_nrz)):
      
        if i == 0:
            x_auxNRZI.append(1)   

        if (x_auxNRZI[i-1]!=x_auxNRZI[i]) and i!=0:
            x_auxNRZI.append(x_auxNRZI[i])
        
        if x_auxNRZI[i-1]==x_auxNRZI[i]  and i!=0:
            x_auxNRZI.append((x_auxNRZI[i])+1)     
    #-------------------------------------------------------

    # Criação do gráfico NRZ utilizando Plotly
    fig.add_trace(go.Scatter(x=x_auxNRZI, y=mensagem_codificada_nrzI, mode='lines'))
    fig.update_layout(
        title="Codificação NRZ-I",
        xaxis_title="Tempo",
        yaxis_title="Nível de Sinal"
    )
    fig.show()

#___________________________________________ PARTE RZ _________________________________________

    #----------------------- Para ajustar o grafico RZ 
    x_auxRZ=[0]
    for i in range(len(mensagem_codificada_rz)):
        if i == 0:
            x_auxRZ.append(1)   

        if (x_auxRZ[i-1]!=x_auxRZ[i]) and i!=0:
            x_auxRZ.append(x_auxRZ[i])
        
        if x_auxRZ[i-1]==x_auxRZ[i]  and i!=0:
            x_auxRZ.append((x_auxRZ[i])+1)     
    #--------------------------------------------------

    #Criação do gráfico RZ utilizando Plotly
    fig = go.Figure()
    #fig.add_trace(go.Scatter(x=list(range(len(mensagem_codificada_rz))), y=mensagem_codificada_rz, mode='lines'))
    fig.add_trace(go.Scatter(x=x_auxRZ, y=mensagem_codificada_rz, mode='lines'))
    fig.update_layout(
        title="Codificação RZ",
        xaxis_title="Tempo",
        yaxis_title="Nível de Sinal"
    )
    fig.show()



def ip_config_emissor(mensagem_codificada_nrz,mensagem_codificada_rz,mensagem_codificada_nrzI,host_ip,port):
    # Obtém o endereço IP do host receptor
    HOST = host_ip
    PORT = port  # Porta de comunicação
    # Cria o socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #AF_INET -> comunicação IPv4
    #SOCK_STREAM -> utilizando o protocolo TCP

    # Conecta ao receptor
    s.connect((HOST, PORT))

    # Envia a mensagem codificada nrz
    # encode é usado para converter uma string em uma sequencia de bytes, 
    # porém mensagem_codificada_nrz é uma lista 

    # Por isso vamos usar o método join() para concatenar as strings da lista em uma única string
    mensagem_codificada_nrz = [str(bit) for bit in mensagem_codificada_nrz]  # Converte os inteiros em strings
    mensagem_codificada_nrz = ''.join(mensagem_codificada_nrz)  # Converte a lista em uma string
    s.sendall(mensagem_codificada_nrz.encode()) # convert uma string em uma sequencia de bytes

    mensagem_codificada_nrzI = [str(bit) for bit in mensagem_codificada_nrzI]  # Converte os inteiros em strings
    mensagem_codificada_nrzI = ''.join(mensagem_codificada_nrzI)  # Converte a lista em uma string
    s.sendall(mensagem_codificada_nrzI.encode())


    mensagem_codificada_rz = [str(bit) for bit in mensagem_codificada_rz]  # Converte os inteiros em strings
    mensagem_codificada_rz = ''.join(mensagem_codificada_rz)  # Converte a lista em uma string
    # Envia a mensagem codificada rz
    s.sendall(mensagem_codificada_rz.encode())

    # Fecha o socket
    s.close()


class OutputWindow(QtWidgets.QMainWindow):
    def __init__(self, message, key, binary_message, nrz_signal, rz_signal,nrzi_signal):
        super(OutputWindow, self).__init__()
        self.setWindowTitle("Output Window")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.text_edit.setGeometry(QtCore.QRect(10, 10, 580, 380))
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QtGui.QFont("Courier", 10))
        self.text_edit.append("Mensagem original: {}".format(message))
        self.text_edit.append("\n")
        #self.text_edit.append("Mensagem criptografada: {}".format(mensagem_criptografada))
        #self.text_edit.append("\n")
        self.text_edit.append("Chave utilizada: {}".format(key))
        self.text_edit.append("\n")
        self.text_edit.append("Mensagem em binário: {}".format(binary_message))
        self.text_edit.append("\n")
        self.text_edit.append("Sinal codificado NRZ: {}".format(nrz_signal))
        self.text_edit.append("\n")
        self.text_edit.append("Sinal codificado NRZ: {}".format(nrzi_signal))
        self.text_edit.append("\n")
        self.text_edit.append("Sinal codificado RZ: {}".format(rz_signal))


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
        self.plot_button.clicked.connect(self.plot_button_clicked)
        self.load_button = QtWidgets.QPushButton(self.frame)
        self.load_button.setGeometry(QtCore.QRect(250, 20, 95, 23))
        self.load_button.setObjectName("load_button")
        self.load_button.clicked.connect(self.load_button_clicked)
        self.send_button = QtWidgets.QPushButton(self.frame)
        self.send_button.setGeometry(QtCore.QRect(510, 20, 75, 23))
        self.send_button.setObjectName("send_button")
        self.send_button.clicked.connect(self.send_button_clicked)
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

        self.output_window = None  # Variável de instância para a janela de saída

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

    def plot_button_clicked(self):
        message = self.message_line.text()
        if not message:
            QMessageBox.warning(MainWindow, "Atenção", "Digite uma mensagem antes de plotar.")
            return

        message, key, mensagem_binaria, mensagem_codificada_nrz,mensagem_codificada_rz,mensagem_codificada_nrzI = about(message)
        plot_graphs(mensagem_codificada_nrz,mensagem_codificada_rz,mensagem_codificada_nrzI)

    def load_button_clicked(self):
        message = self.message_line.text()
        if not message:
            QMessageBox.warning(MainWindow, "Atenção", "Digite uma mensagem antes de carregar.")
            return

        message,  key, binary_message, mensagem_codificada_nrz, mensagem_codificada_rz,mensagem_codificada_nrzI = about(message)

        self.output_window =  OutputWindow(message,  key, binary_message, mensagem_codificada_nrz, mensagem_codificada_rz,mensagem_codificada_nrzI)

        self.output_window.show()
    
    def send_button_clicked(self):
        host_ip = self.ip.text()

        message = self.message_line.text()
        if not message:
            QMessageBox.warning(MainWindow, "Atenção", "Digite uma mensagem antes de enviar.")
            return

        if not host_ip:
            QMessageBox.warning(MainWindow, "Atenção", "Digite o IP do host receptor antes de enviar.")
            return
        
        port = self.porta_line.text()
        if not port:
            QMessageBox.warning(MainWindow, "Atenção", "Digite a porta desejada antes de enviar.")
            return

        message,  key, binary_message, mensagem_codificada_nrz, mensagem_codificada_rz,mensagem_codificada_nrzI = about(message)
        ip_config_emissor(mensagem_codificada_nrz, mensagem_codificada_rz, host_ip, int(port),mensagem_codificada_nrzI)

        QMessageBox.information(MainWindow, "Sucesso", "Mensagem enviada com sucesso.")

        self.output_window = OutputWindow(message,  key, binary_message, mensagem_codificada_nrz, mensagem_codificada_rz,mensagem_codificada_nrzI)
        self.output_window.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())