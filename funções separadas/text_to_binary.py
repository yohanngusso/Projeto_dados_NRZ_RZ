def text_to_binary(message):
    binary_message = ' '.join(format(ord(char), '08b') for char in message)
    return binary_message

message = "Oi"
binary_message = text_to_binary(message)

print("Mensagem original:", message)
print("\n")
print("Mensagem em binário:", binary_message)
print("\n")