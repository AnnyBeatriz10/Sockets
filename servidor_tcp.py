import socket
#thread
HOST = 'localhost'
PORT = 50000
lista_mensagens = []
a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a.bind((HOST, PORT))
a.listen(2)
con, cliente = a.accept()
while True:

	print('Aguardando conexão')
	print('Conectado por: ', cliente)

	while True:
		msg = con.recv(1024)
		if not msg: break
#                if msg.decode('utf-8')):
			
		lista_mensagens.append(msg.decode('utf-8'))
		print(lista_mensagens)
		if len(lista_mensagens) >= 5 : 
			print(lista_mensagens)
			con.send(str(lista_mensagens).encode('utf-8'))
			del lista_mensagens[0]
		
   
print('Finalizando conexão do cliente ', cliente)
con.close()

'''
OBS : armazenar mensagens do cliente em uma lista descartando o primeiro elemento quando completar 5
'''

'''
PASSO 2 : devolver a lista de mensagens para o cliente
'''

