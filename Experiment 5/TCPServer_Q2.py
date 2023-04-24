from socket import *

if __name__ == '__main__':
    server_ip = ''
    server_port = 12000

    # 初始化socket
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定IP和端口
    server_socket.bind((server_ip, server_port))
    # 监听端口
    server_socket.listen()  
    print("服务器正在监听...")

    while True:
        # 接受建立客户端请求的连接
        connection_socket, client_addr = server_socket.accept()
        # 接收消息
        resp = connection_socket.recv(1024)
        print(f"来自客户端{client_addr}的消息: {resp.decode()}")

        # 返回消息
        return_msg = resp.decode().lower()
        connection_socket.send(return_msg.encode())

        # 关闭连接
        connection_socket.close()
        