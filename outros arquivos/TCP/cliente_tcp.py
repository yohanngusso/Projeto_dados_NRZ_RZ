import socket

IP_SERVIDOR =  "192.168.1.6"
# Endereço IP do Servidor

PORTA_SERVIDOR = 8000
# Porta em que o servidor estara ouvindo 

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET = INET (exemplo IPv4)sockets | socket.SOCK_STREAM = usaremos TCP
# aqui estamos dizendo que tipo de protocolo estamos utilizando 

DESTINO = (IP_SERVIDOR, PORTA_SERVIDOR)
#destino(IP & PORTA do servidor que está enviando)

tcp.connect(DESTINO)
#INICIA A CONEXÃO TCP
# A ideia desse while é que não precisa fazer várias conexoes para enviar cada mensagem
# Fez a conexão uma vez pode enviar várias mensagens
while 1:
    Mensagem = input()
    # Mensagem recebera dados do teclado

    tcp.send(bytes(Mensagem,"utf8"))
    #enviar a mensagem para o destino da conexão(IP & PORTA)
    #bytes(Mensagem,"utf8") = converte tipo srt para byte
tcp.close()
#finalizar o socket 