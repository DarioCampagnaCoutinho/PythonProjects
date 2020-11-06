import socket

ip = '192.168.0.1'
porta = 80

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
resposta = meusocket.connect_ex((ip, porta))

if resposta == 0:
    print 'Porta Aberta'
else:
    print 'Porta Fechada'