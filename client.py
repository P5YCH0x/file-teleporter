import socket
import time

ip = '127.0.0.1'
port = 9922
numlines = 0
filename = str(input("filename: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ip, port))

with open(filename, 'rb') as file:
    for line in file.readlines():
        numlines = numlines+1

client.send(str(numlines).encode())
time.sleep(1)
client.send(filename.encode())

with open(filename, 'rb') as file:
    for line in file.readlines():
        client.send(line)

