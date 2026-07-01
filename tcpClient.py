import socket

target_host = "www.google.com"
target_port = 9998

# Create Socket Object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# send data
client.send(b"GET / HHTP/1.1\r\nHost: google.com\r\n\r\n")

# receive data
response = client.recv(4096)

print(response.decode())
client.close()