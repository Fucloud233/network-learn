from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)

server_ip = "127.0.0.1"
server_port = 123456

server_socket.bind((server_ip, server_port))
server_socket.listen()
print("服务器正在监听...")

while True:
    connection_socket, client_addr = server_socket.accept()
    resp = connection_socket.recv(1024)
    print(f"来自客户端{client_addr}的消息: {resp.decode()}")
    connection_socket.close()
    
    