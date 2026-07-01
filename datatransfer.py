import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

with open("datei.txt", "rb") as f:
    while True:
        daten = f.read(1024)

        if not daten:
            break

        client.sendall(daten)

print("Datei gesendet.")
client.close()