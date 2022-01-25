import socket

HOST = 'localhost'
PORT = 50000
sum = 0
conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conexão.connect((HOST, PORT))
print('Para sair digite SAIR')

try:

  while True:

	  msg = input('Digite a mensagem: ')

    if msg == sair.upper():
      print('Finalizando conexão')
      break

	  msg = msg.encode('utf-8')
	  conexão.send(msg)
	  print(msg)
	  sum +=1 

	  if sum >4:
	      entrada = conexão.recv(1024)
	      entrada = entrada.decode('utf-8')
	      print(entrada)

  conexão.close()


