import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

client.sendto('AAABBBCCC',("127.0.0.1",80))

data, addr = client.recvfrom(4096)

print (data)
