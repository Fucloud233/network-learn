import socket
import random
from socket import *

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
    serverSocket.listen(1)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        connectionSocket, addr = serverSocket.accept()
        # 设置mes编号
        mes_idx = 1

        word = ''
        # 不断处理客户端的请求
        while True:
            # 从客户端获得长度为5的数据
            tmp = connectionSocket.recv(5).decode('utf-8')

            # 根据间隔符对数据进行分组
            tmp_list = tmp.split(' ')

            # 当分割数量大于1时 对前n-1个进行输出
            for i in range(len(tmp_list)-1):
                word += tmp_list[i]
                print('server get mes{}: {}'.format(mes_idx, word))
                mes_idx += 1
                word = ''
                
            last = tmp_list[len(tmp_list) - 1]

            # 若以\0为结束，则停止监听
            if last == '\0':
                print('server end listening from client')
                break
            else:
                word += last
            
        # 连接关闭
        connectionSocket.close()
