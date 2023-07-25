from cryptography.fernet import Fernet

def encrypt(message, key):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(message.encode())
    return ciphertext.decode()

# Gerar uma nova chave válida para uso com o algoritmo Fernet
key = Fernet.generate_key()

# Mensagem a ser criptografada
message = "Olá"

# Criptografar a mensagem
encrypted_message = encrypt(message, key)

print("Mensagem original:", message)
print("\n")
print("Mensagem criptografada:", encrypted_message)
print("\n")
print("Chave utilizada:", key)
