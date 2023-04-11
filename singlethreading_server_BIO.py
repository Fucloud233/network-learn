from socket import *

def singlethreading_server_BIO(ip: str, port: int):
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口号和套接字
    serverSocket.bind((ip, port))
    # 开启监听，设置1024个连接缓冲，暂时将连接挂起
    serverSocket.listen(1024)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        conn, addr = serverSocket.accept()
        # 这里为了方便，用try-catch来处理客户端自动断开连接
        try:
            # 接受客户端的数据
            data = conn.recv(1024).decode()
            # print(data)
            # 服务器发送响应，代表本次的数据结束了
            conn.sendall('over'.encode())
            # 连接关闭
            conn.close()
        except Exception as e:
            pass

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    singlethreading_server_BIO('', serverPort)
