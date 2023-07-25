import socket

def decrypt(message, key):
    # Implemente sua função de descriptografia aqui
    # Exemplo usando algoritmo de substituição simples
    decrypted_message = ""
    for char in message:
        decrypted_message += chr(ord(char) - key)
    return decrypted_message

def binary_to_text(binary):
    # Implemente sua função de conversão para texto aqui
    # Exemplo simples de conversão de binário para texto usando a tabela ASCII
    text_message = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text_message += chr(int(byte, 2))
    return text_message

def nrz_decoding(codificado):
    # Implemente sua função de decodificação NRZ aqui
    # Exemplo simples de decodificação NRZ (sem considerar sincronização, etc.)
    decoded_message = ""
    for bit in codificado:
        if bit == '-1':
            decoded_message += '0'
        else:
            decoded_message += '1'
    return decoded_message

# Configurações do receptor
HOST = '0.0.0.0'  # Endereço IP do receptor (deixe como '0.0.0.0' para aceitar conexões de qualquer IP)
PORT = 12345  # Porta de comunicação
KEY = 3  # Chave de criptografia

# Cria o socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço e porta
s.bind((HOST, PORT))

# Aguarda por conexões
s.listen(1)

# Aceita a conexão do emissor
conn, addr = s.accept()

# Recebe a mensagem codificada
mensagem_codificada = conn.recv(1024).decode()

# Decodifica em NRZ
binario = nrz_decoding(mensagem_codificada)

# Converte o binário para texto
mensagem_criptografada = binary_to_text(binario)

# Descriptografa a mensagem
mensagem_original = decrypt(mensagem_criptografada, KEY)

# Imprime a mensagem original
print("Mensagem recebida: ", mensagem_original)

# Fecha a conexão e o socket
conn.close()
s.close()
