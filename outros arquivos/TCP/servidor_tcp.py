import socket

MEU_IP = ''
# Endereço IP do servidor, '' = siginifica que ouvira em todas as interfaces 
# Podemos colar o IP especifico do PC CLIENTE AQUI

MINHA_PORTA = 8000
# Porta que o Servidor vai ouvir 
# Para saber se a porta está sendo usada utilize esse comandos:
#netstat -ano | findstr :8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET = INET (exemplo IPv4)sockets | socket.SOCK_STREAM = usaremos TCP
# aqui estamos dizendo que tipo de protocolo estamos utilizando 

# x = 1
testa_mensagem = ''
MEU_SERVIDOR = (MEU_IP, MINHA_PORTA)
tcp.bind(MEU_SERVIDOR)
# faz o bind do ip e a porta para que possa começar a ouvir 

tcp.listen(1)
# tcp vai ouvir e vai aguarda uma conexão antes de receber os dados

#uma vez que o cliente faz a conexão 
conexao, doclient = tcp.accept()
print("o cliente = ",doclient, "se conectou")
# pega o ip do cliente que conectou e printa

# While para verificar se realmente não chegou uma mensagem
# e não está printando uma suposta mensagem que nem chegou após a conexao 
while 1:
    Mensagem_Recebida = conexao.recv(1024)
    #Mensagem recebida do cliente
    if testa_mensagem != Mensagem_Recebida:
        #aqui verifica se exite mensagem nova
        print("Recebi = ",Mensagem_Recebida,", Do cliente", doclient)


conexao.close()
#fim do socket




