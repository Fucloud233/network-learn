import socket
import random
from socket import *

import time

def get_random_buffer_size():
    return random.randint(0, 5) + 1

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 设置端口重用，以便服务能迅速重启
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定端口号和套接字
    serverSocket.bind(('', serverPort))
    # 开启监听
    serverSocket.listen(100)
    print('The server is ready to receive')

    while True:
        # 等待接受客户端的连接
        connectionSocket, addr = serverSocket.accept()
        # 设置mes编号
        mes_idx = 1

        # 不断处理客户端的请求
        while True:
            # 用于记录接收的头部数据
            length_text = ''
            # 一次读取头部信息中的长度 直到分隔符'$'截止
            while True:
                n = connectionSocket.recv(1).decode('utf-8')
                # 当接收到分隔符后 终止接收
                if n == '$':
                    break
                length_text += n
            length = int(length_text)

            # 通过缓存变量 知道接收到指定长度的字节为止
            buf = bytes()
            while length != 0:
                tmp = connectionSocket.recv(length)
                length -= len(tmp)
                buf += tmp
            word = buf.decode('utf-8')

            # 当接收到终止符 终止循环
            if word=='\0':
                print('server end listening from client')
                break
            
            print('server get mes{}: {}'.format(mes_idx, word))
            mes_idx += 1
            
        # 关闭连接
        connectionSocket.close()
 