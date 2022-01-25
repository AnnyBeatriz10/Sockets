#!/usr/bin/python3

import socket
import _thread
import os

HOST = input('Informe o IP:')  # Endereco IP do Servidor
PORT = int(input('Informe a porta da conexão:'))  # Porta que o Servidor está
nome = input('informe o nome do usuário para conexão:')
chave = input('Informe a chave da conexão:')
dic_login = {}

#-------------------------------------------------------------------------
# Função chamada quando uma nova thread for iniciada
def conectado(conexão, cliente):
    print('Para sair use CTR+X\n')
    print('\nCliente conectado:', cliente)

    if conexão and cliente == True:

       dic_login[cliente] = nome

    while True:
        msg = con.recv(1024)
        if not msg: break
        print('O usuário {0} com endereço {1} disse: {2}'.format(nome,cliente,msg.decode('utf-8')))

    print('\nFinalizando conexao do usuário {0} na porta {1}'.format(nome,PORT))
    con.close()
    _thread.exit()

#-------------------------------------------------------------------------
def crip(chave,nome):



#-------------------------------------------------------------------------
# Bloco principal
os.system('clear')

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)

tcp.listen(2)
print('\nServidor TCP-THREAD iniciado no IP', HOST, 'na porta', PORT)

while True:
    con, cliente = tcp.accept()
    print('\nNova thread iniciada para essa conexão')

    # Abrindo uma thread para a conexão
    _thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()
