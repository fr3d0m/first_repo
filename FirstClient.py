import socket

s = socket.socket()

s.connect(('127.0.0.1', 12345))

message = input('> ')

s.send(message.encode())

answer = s.recv(1024)

print('Server: ', answer.decode())

s.close()
