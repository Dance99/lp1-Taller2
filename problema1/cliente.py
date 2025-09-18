#!/usr/bin/env python3
"""
Problema 1: Sockets básicos - Cliente
Objetivo: Crear un cliente TCP que se conecte a un servidor e intercambie mensajes básicos
"""

import socket

HOST = 'localhost'
PORT = 9000

# Crear un socket TCP/IP
# AF_INET: socket de familia IPv4
# SOCK_STREAM: socket de tipo TCP (orientado a conexión)
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al servidor en la dirección y puerto especificados
cliente.connect((HOST, PORT))

# Enviar datos al servidor (convertidos a bytes)
# sendall() asegura que todos los datos sean enviados
mensaje = "Hola servidor, este es un mensaje del cliente"
cliente.sendall(mensaje.encode('utf-8'))

# Recibir datos del servidor (hasta 1024 bytes)
respuesta = cliente.recv(1024)

# Decodificar e imprimir los datos recibidos
print("Respuesta del servidor:", respuesta.decode('utf-8'))

# Cerrar la conexión con el servidor
cliente.close()
