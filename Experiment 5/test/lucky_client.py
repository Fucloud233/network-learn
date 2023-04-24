from socket import *

if __name__ == '__main__':
    # 连接服务器
    client_socket = socket(AF_INET, SOCK_STREAM)
    server_ip = "47.120.5.208"
    server_port = 12345

    client_socket.connect((server_ip, server_port))
    print("服务器连接成功!")

    # 接收返回消息
    ret_msg = client_socket.recv(1024)
    print(ret_msg.decode())

    # 输入名字
    name = input()
    client_socket.send(name.encode())

    # 输出返回值
    lucky_msg = client_socket.recv(1024)
    print(lucky_msg.decode())

    client_socket.close()

