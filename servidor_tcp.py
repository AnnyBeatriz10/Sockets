import socket
#thread
HOST = 'localhost'
PORT = 50000
lista_mensagens = []
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # INET = tipo IP , STREAM = TCP
serv.bind((HOST, PORT)) # estabelece a conexão com o cliente na porta 
serv.listen(2) # define o limite de conexões
con, cliente = serv.accept() # 'aceita' inputs

while True:

	print('Aguardando conexão')
	print('Conectado por: ', cliente) # na porta: ...

	while True:
		msg = con.recv(1024) # recebe atéé 1024 bytes

		if not msg: 
          break

    if msg == True:
			print(msg.decode('utf-8'))
       lista_mensagens.append(msg.decode('utf-8'))

con.close()
print('Finalizando conexão do cliente ', cliente)

#---------------------------------------------------------------------
# Bloco responsável por enviar as mensagens de volta para o cliente

		  if len(lista_mensagens) >= 5 : 
			  print(lista_mensagens)
		  	con.send(str(lista_mensagens).encode('utf-8')) # devolve a lista para o cliente
			  del lista_mensagens[0] # exclui o primeiro elemento informado
		
   




'''
OBS : armazenar mensagens do cliente em uma lista descartando o primeiro elemento quando completar 5
'''

'''
PASSO 2 : devolver a lista de mensagens para o cliente quando ele fechar a conexão
'''

