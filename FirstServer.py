import socket
import threading

server = socket.socket()

server.bind(('127.0.0.1', 12345))

server.listen()

print('Waiting for connection...')

client_socket, adresse = server.accept()

print('Connected to', adresse)

while True:
    answer = client_socket.recv(1024)

    if not answer:
        break

    print('Client:', answer.decode())

    message = input('> ')

    if not message:
        break

    client_socket.send(message.encode())

print('Connection closed')
client_socket.close()
server.close()