#!/usr/bin/python3
import socket

HOST = '0.0.0.0'
PORT = 50000
lista_mensagens = []


udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF.INET indifca a família do protocolo no caso ethernet

udp.bind((HOST, PORT)) 

try:

	while True:

		msg, cliente = udp.recvfrom(1024)
		lista_mensagens.append(msg.decode('utf-8'))

		if len(lista_mensagens) <= 5 : 
			del lista_mensagens[0]
			print(cliente, msg.decode('utf-8'),lista_mensagens)
			lista_mensagens.append(msg.decode('utf-8'))



except:

	while True:

		msg, cliente = udp.recvfrom(1024)
		lista_mensagens.append(msg)

		if len(lista_mensagens) <= 5 : 
			del lista_mensagens[0]
			lista_mensagens.append(msg)
			print(cliente, msg.decode('utf-8'),lista_mensagens)
	
udp.close()

'''
OBS: o intuito era continuar a operação até que o usuário parasse de mandar mensagens!
'''