from socket import *

word = ' hello world'
print(word.split(' '))

client_socket = socket(AF_INET, SOCK_STREAM)
server_ip = "47.120.5.208"
server_port = 12345

client_socket.connect((server_ip, server_port))
print("客户端连接成功")
msg = input("Please enter message: ")
req = msg.encode()
client_socket.send(req)

client_socket.close()

