import socket
import threading

s = socket.socket()

s.connect(('127.0.0.1', 12345))


def sende():
    while True:
        message = input("> ")

        if not message:
            print("Connection closed")
            s.close()
            break

        s.send(message.encode())


def empfange():
    while True:
        answer = s.recv(1024)

        if not answer:
            print("Server closed connection")
            s.close()
            break

        print("\nServer:", answer.decode())


thread_send = threading.Thread(target=sende)
thread_recv = threading.Thread(target=empfange)

thread_send.start()
thread_recv.start()
