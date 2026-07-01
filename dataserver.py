import socket

HOST = "0.0.0.0"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server wartet auf Verbindung...")

client, addr = server.accept()
print(f"Verbunden mit {addr}")

with open("empfangene_datei.txt", "wb") as f:
    while True:
        daten = client.recv(1024)

        if not daten:
            break

        f.write(daten)

print("Datei empfangen.")
client.close()
server.close()