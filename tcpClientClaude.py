import socket

target_host = "127.0.0.1"  # <-- Das war der Fehler! Nicht 0.0.0.0
target_port = 9998

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send(b"Daten gesendet")
response = client.recv(4096)
print(f"Antwort vom Server: {response.decode()}")
client.close() 