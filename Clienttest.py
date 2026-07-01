import socket
import threading

s = socket.socket()

s.connect(('127.0.0.1', 12345))

while True:
    message = input('> ')

    if not message:
        break

    s.send(message.encode())

    answer = s.recv(1024)

    if not answer:
        break

    print('Server:', answer.decode())

print('Connection closed')
s.close()
