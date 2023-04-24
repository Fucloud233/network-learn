from socket import *

if __name__ == "__main__":
    server_ip = ''
    server_port = 12345
    
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen()
    print('服务器正在运行中...')

    while True:
        connetion_socket, client_addr = server_socket.accept()

        # 通过while循环持续接收客户端发送的消息
        while True:
            msg = connetion_socket.recv(1024).decode()

            # 当接收消息为bye时 终止连接
            if msg == 'bye':
                print(f"与客户端{client_addr}终止连接")
                connetion_socket.close()
                break
            else:
                print(f"来自客户端{client_addr}的消息: {msg}")
                ret_msg = msg.lower()
                connetion_socket.send(ret_msg.encode())