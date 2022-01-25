# BLOCO BÁSICO
import socket

HOST = 'localhost'
PORT = 50004
lista_msg = []
cont = 0

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((HOST, PORT))

print('Para sair use CTRL+X\n')

msg = input('Digite a mensagem: ')

while msg != '\x18':
	msg = msg.encode('utf-8')
	print(msg)
	tcp_socket.send(msg)
	msg = input('Digite a mensagem: ')

print('Para exibir a lista de mensagens use CTRL+Q\n')

#--------------------------------------------------------------------------------
# IMPLEMENTAÇÕES
# OBJETIVO: guardar as mensagens em uma lista(vetor) se a quantidade de msg for maior do que 5

if msg == ''.encode('utf-8'):

	lista_msg.appen(msg.decode('utf-8'))

	if len(lista_msg) > 5:

		for i in lista_msg:

			cont += 1
		print('sua mensagens:',i,'possuem',cont,'caracteres')

		
		
	


