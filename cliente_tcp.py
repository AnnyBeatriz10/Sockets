#!/usr/bin/python3
import socket
import os

HOST = 'localhost'
PORT = 50004
sum = 0

address = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address.connect((HOST, PORT))

print('Para sair digite SAIR')

msg = input('Digite uma mensagem: ')

while msg != SAIR:

	msg = input('Digite uma mensagem: ')
	msg = msg.encode('utf-8')
	address.send(msg)  # envia as mensagens para o servidor
	print(msg)
	msg = input('Digite uma mensagem: ')
	sum +=1
	print(sum) 
	if sum > 4: 
	     entrada = address.recv(1024)
	     entrada = entrada.decode('utf-8')
	     print('as 5 últimas mensagens são:',entrada)
a.close()


