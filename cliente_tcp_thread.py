#!/usr/bin/python3

import socket
import os

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = int(input('Informe a porta da conexão:'))             # Porta que o Servidor está

os.system('clear')

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp.connect((HOST,PORT))

print('\nDigite suas mensagens')
print('Para sair use CTRL+X\n')

nome = input('Digite seu nome(nickname):')
mensagem = input('Digite sua mensagem: ')

# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '\x18':
    tcp.send(mensagem.encode('utf-8'))
    mensagem = input('Digite sua mensagem: ')

# Fechando o Socket
tcp.close()
