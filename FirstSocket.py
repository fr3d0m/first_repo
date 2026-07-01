import socket

s = socket.socket()

s.connect(("example.com", 80))

anfrage = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"

s.send(anfrage.encode())

antwort = s.recv(1024)

print(antwort.decode())

s.close()