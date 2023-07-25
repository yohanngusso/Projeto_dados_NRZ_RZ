from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt(message, key):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(message.encode())
    return ciphertext

def decrypt(ciphertext, key):
    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(ciphertext)
    return plaintext.decode()

# Gera uma chave
key = generate_key()

# Mensagem de teste
message = "Essa é uma mensagem de teste."

# Criptografa a mensagem
ciphertext = encrypt(message, key)
print("Mensagem criptografada:", ciphertext)

# Descriptografa a mensagem
decrypted_message = decrypt(ciphertext, key)
print("Mensagem descriptografada:", decrypted_message)
