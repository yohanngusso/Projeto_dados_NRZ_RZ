from cryptography.fernet import Fernet

def encrypt(message, key):
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(message.encode())
    return ciphertext.decode()

def decrypt(ciphertext, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(ciphertext.encode())
    return decrypted_message.decode()

# Gerar uma nova chave válida para uso com o algoritmo Fernet
key = Fernet.generate_key()

# Mensagem a ser criptografada
message = "Esta é uma mensagem confidencial."

# Criptografar a mensagem
encrypted_message = encrypt(message, key)

# Descriptografar a mensagem
decrypted_message = decrypt(encrypted_message, key)

print("Mensagem original:", message)
print("\n")
print("Mensagem criptografada:", encrypted_message)
print("\n")
print("Mensagem descriptografada:", decrypted_message)
print("\n")
print("Chave utilizada:", key)
print("\n")
