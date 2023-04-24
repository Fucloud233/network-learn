# import socket module
from socket import *

if __name__ == '__main__':
    # 准备TCP套接字
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 将TCP套接字绑定到指定端口
    serverSocket.bind(("", 30000))
    # 设置最大连接数
    serverSocket.listen(1)

    while True:
        # 接收到客户连接请求后，建立新的TCP连接套接字
        connectionSocket, addr = serverSocket.accept()
        # 准备迎接客户端的连接
        print('Ready to serve...')

        # 获取客户发送的报文
        message = connectionSocket.recv(1024)
        # 获取客户端需要的文件名，根据html格式来进行切分
        print(message.decode().split(' '))
        filename = '.' + message.decode().split(' ')[1]

        try:
            # 读取文件
            f = open(filename)
            # 200响应行
            response_line = "HTTP/1.1 200 OK\r\n"
        # 找不到这个文件，返回404
        except IOError:
            # 读取404页面文件
            f = open("404.html")
            # 404响应行
            response_line = "HTTP/1.1 404 Not Found\r\n"
        
        # 响应体
        response_body = f.read() 
        # 响应头
        response_header = "Connection: close\r\n"
        response_header += "Content-Type: text/html\r\n"
        response_header += f"Content-Length: {len(response_body)}\r\n"
        response_header += "charset: utf-8\r\n"
        # 空行
        empty = '\r\n'
        # 拼接响应
        response = response_line + response_header + empty + response_body
        # 发送响应
        connectionSocket.send(response.encode())
        # 关闭连接
        connectionSocket.close()
    serverSocket.close()
