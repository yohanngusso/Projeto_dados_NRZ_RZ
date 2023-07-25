import socket

# Obtém o nome do host
hostname = socket.gethostname()

# Obtém o endereço IP associado ao nome do host
ip_address = socket.gethostbyname(hostname)

# Imprime o endereço IP
print("Endereço IP do computador:", ip_address)
