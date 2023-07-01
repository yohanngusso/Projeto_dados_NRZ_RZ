import plotly.graph_objects as go
from cryptography.fernet import Fernet

# Funções
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

def about(message):
    # Criptografa a mensagem
    mensagem_criptografada = encrypt(message, key)
    print("Mensagem original:", message)
    print("\n")
    print("Mensagem criptografada:", mensagem_criptografada)
    print("\n")
    print("Chave utilizada:", key)
    print("\n")
    # Converte a mensagem criptografada em binário
    binary_message = text_to_binary(mensagem_criptografada)
    print("Mensagem em binário:", binary_message)
    print("\n")
    # Codifica em NRZ
    mensagem_codificada_nrz = nrz_encoding(binary_message)
    print("Sinal codificado NRZ:", mensagem_codificada_nrz)
    # Codifica em RZ
    mensagem_codificada_rz = rz_encoding(binary_message)
    print("Sinal codificado RZ:", mensagem_codificada_rz)
    
    return mensagem_codificada_nrz

def graphic(mensagem_codificada):
    # Criação do gráfico NRZ utilizando Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(mensagem_codificada))), y=mensagem_codificada, mode='lines'))

    fig.update_layout(
        title="Codificação NRZ",
        xaxis_title="Tempo",
        yaxis_title="Nível de Sinal"
    )
    fig.show()
    # Criação do gráfico RZ utilizando Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(mensagem_codificada))), y=mensagem_codificada, mode='lines'))

    fig.update_layout(
        title="Codificação RZ",
        xaxis_title="Tempo",
        yaxis_title="Nível de Sinal"
    )
    fig.show()

# Código principal

# Gerar uma nova chave válida para uso com o algoritmo Fernet
key = Fernet.generate_key()

# Mensagem a ser enviada
message = "Oi"

informacoes = about(message)
graphic(informacoes)

