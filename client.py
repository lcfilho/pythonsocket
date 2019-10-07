###################################################################################
##########################SOCKET CLIENTE###########################################
###################################################################################
import socket

sock_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 9999

sock = ((host, port))

print('/'*60+'SOMA SERVER'+'/'*60)
print('''Digite c para começar e de Enter; o primeiro valor, Enter; o segundo, Enter:  
                Digite 'exit' e de Enter para sair.''')

msg = input('')
if msg == 'exit':
    sock_client.sendto(msg.encode('ascii'), sock)
    msg2 = 'exit'
    sock_client.sendto(msg2.encode('ascii'), sock)
    msg3 = 'exit'
    sock_client.sendto(msg3.encode('ascii'), sock)
    print("Saiu!")
    sock_client.close()

else:
    msg2 = input('->')
    msg3 = input('->')

while msg != 'exit':
    sock_client.sendto(msg.encode('ascii'), sock)
    sock_client.sendto(msg2.encode('ascii'), sock)
    sock_client.sendto(msg3.encode('ascii'), sock)
    print("Mensagem Enviada: qual o resultado da {} entre {} e {}?".format(msg, msg2,msg3))
    dados, end = sock_client.recvfrom(1024)

    print('Resposta: {}'.format(dados.decode('ascii')))
    msg = input('->')
    if msg == 'exit':
        sock_client.sendto(msg.encode('ascii'), sock)
        msg2 = 'exit'
        sock_client.sendto(msg2.encode('ascii'), sock)
        msg3 = 'exit'
        sock_client.sendto(msg3.encode('ascii'), sock)
        print(" Cliente Saiu!")
        sock_client.close()

    else:
        msg2 = input('->')
        msg3 = input('->')

sock_client.close()
