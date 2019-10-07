###################################################################################
##########################SOCKET SERVER############################################
###################################################################################
import socket

sock_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999

sock_server.bind((host, port))

print('''Servidor Adicao iniciado. Aguardando a Cliente.''')

while True:
    dados, addr = sock_server.recvfrom(1024)
    dados2, addr2 = sock_server.recvfrom(1024)
    dados3, addr3 = sock_server.recvfrom(1024)
    print('Estabelecida uma conexão: {}'.format(str(addr)))
    print("Mensagem Recebida: {} entre {} e {}".format(dados.decode('ascii'),dados2.decode('ascii'),dados3.decode('ascii') ))

    
    if (dados.decode('ascii')).lower() != 'exit':
        print('Resposta da soma para o cliente.')
        sock_server.sendto(str(int(dados2 )+ int(dados3)).encode('ascii'), addr)

    elif (dados.decode('ascii')).lower() == 'exit':
        print("Cliente Saiu do Sitema")
        exit()
 

sock_server.close()
