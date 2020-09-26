import socket

ip = '0.0.0.0'
port = 9922

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)
connection, address = server.accept()

data = connection.recv(1024)
numlines = int(data.decode())

filename = connection.recv(1024)
filename = filename.decode()

print(numlines)
print(filename)

with open(filename, 'wb') as file:
    for i in range(0, numlines):
        data = connection.recv(1024)
        file.write(data)

connection.close()