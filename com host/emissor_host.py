import socket
from cryptography.fernet import Fernet


def encrypt(message, key):
    key = key.encode()  # Convertendo a chave para bytes
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(message.encode())
    return ciphertext.decode()

def text_to_binary(text):
    # Implemente sua função de conversão para binário aqui
    pass

def nrz_encoding(binary):
    # Implemente sua função de codificação NRZ aqui
    pass

# Configurações do emissor
HOST = 'IP_DO_RECEPTOR'  # Endereço IP do emissor
PORT = 12345  # Porta de comunicação
KEY = 3  # Chave de criptografia

# Mensagem a ser enviada
mensagem = "Oi"

# Criptografa a mensagem
mensagem_criptografada = encrypt(mensagem, KEY)

# Converte a mensagem criptografada em binário
binario = text_to_binary(mensagem_criptografada)

# Codifica em NRZ
mensagem_codificada = nrz_encoding(binario)

# Cria o socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao receptor
s.connect((HOST, PORT))

# Envia a mensagem codificada
s.sendall(mensagem_codificada.encode())

# Fecha o socket
s.close()
