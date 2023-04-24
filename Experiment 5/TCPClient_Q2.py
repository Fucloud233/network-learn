from socket import *

if __name__ == '__main__':
    client_socket = socket(AF_INET, SOCK_STREAM)
    server_ip = "localhost"
    server_port = 12345

    # 建立TCP连接
    client_socket.connect((server_ip, server_port))
    print("客户端连接成功")
    
    # 发送消息
    msg = input("Please enter message: ")
    req = msg.encode()
    client_socket.send(req)

    # 接收返回消息
    ret_msg = client_socket.recv(1024)
    print("返回消息: ", ret_msg.decode())

    # 关闭连接
    client_socket.close()

