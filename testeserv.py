#!/usr/bin/python3

import socket
import os

HOST = '127.0.0.1'
PORT = 50004

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # conexão do tipo TCP/IP
serv.bind((HOST,PORT)) # associa o host e a porta
serv.listen(3) # limite de conexões com clientes por vez
print('Aguardando conexão...')

import datetime

while True:
	
	lista = []

	conexão,endereço = serv.accept() # aceita requisições do cliente
	
	print('Conectado por:',endereço,'na porta:',PORT,'no dia:',time.strftime('%d %b %y'),'de:',time.strftime('%H:%M:%S'))
	
	dados = conexão.recv(1024)

	if not dados:
		break

try:

	while dados == True:

		msg_serv = ('O cliente {0} disse: {1}'.format(endereço, dados.decode('utf-8'))
		lista.append(msg_serv)
		conexão.send(msg_serv.encode('utf-8'))

	print('Finalizando conexão...',endereço,'na porta:',PORT,'no dia:',time.strftime('%d %b %y'),'de:',time.strftime('%H:%M:%S'))


	print('-------------------------------------------------------------')

	print('Exibindo histórico completo do cliente:',endereço'...')

	for i in range(0,len(lista)):
			
			print(lista[i])

	print('----------------------------------------------------')


	print('Histórico atualizado com as 5 últimas mensagens do cliente:',cliente)

	if lista > 5:

		del lista[0]

	print('----------------------------------------------------')

	



except Exception:

	print('Não é possível estabelecer a conexão requerida')

conexão.close()
		

		
		
	



