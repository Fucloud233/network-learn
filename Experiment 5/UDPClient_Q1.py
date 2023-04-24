import time
from socket import *

if __name__ == '__main__':
    # 服务器的IP地址或主机名
    serverName = '127.0.0.1'
    # 服务器端口号
    serverPort = 12000
    # 创建客户套接字，使用IPv4协议，UDP协议
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    # 提示用户输入信息
    message = input('Input lowercase sentence:')
    # 发送报文,传入服务器主机名，套接字端口号
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    # 接收报文
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    # 打印接收的报文
    print(modifiedMessage.decode())
    time.sleep(1)
    # 关闭客户套接字
    clientSocket.close()
