from socket import *

if __name__ == '__main__':
    server_ip = 'localhost'
    server_port = 12345

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print('服务器连接成功...')

    # 通过while循环持续向服务端发送和接收消息
    while True:
        sentence = input('请输入要发送的消息: ')
        client_socket.send(sentence.encode())
        
        # 当发送消息为bye时 终止连接
        if sentence == 'bye':
            client_socket.close()
            print('与服务端终止连接')
            break
        else:
            ret_msg = client_socket.recv(1024).decode()
            print(f'来自服务端的消息: {ret_msg}')