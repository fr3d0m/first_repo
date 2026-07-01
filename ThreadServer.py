import socket
import threading

server = socket.socket()

server.bind(('127.0.0.1', 12345))

server.listen()

print("Waiting for connection...")

client_socket, adresse = server.accept()

print("Connected to", adresse)


def sende():
    while True:
        message = input("> ")

        if not message:
            print("Connection closed")
            client_socket.close()
            break

        client_socket.send(message.encode())


def empfange():
    while True:
        answer = client_socket.recv(1024)

        if not answer:
            print("Client closed connection")
            client_socket.close()
            break

        print("\nClient:", answer.decode())


thread_send = threading.Thread(target=sende)
thread_recv = threading.Thread(target=empfange)

thread_send.start()
thread_recv.start()