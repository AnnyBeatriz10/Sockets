import socket

HOST = ''
PORT = 50004

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.bind((HOST, PORT))
tcp_socket.listen(1)

print('Aguardando conexão')

while True:
   con, cliente = tcp_socket.accept()
   print('Conectado por: ', cliente)
   while True:
      msg = con.recvfrom(1024)
      if not msg: break
      print(cliente, msg[0].decode('utf-8'))
   
   print('Finalizando conexão do cliente ', cliente)
con.close()
