from socket import *

# 开启UDP监听 
# input: 输入小写字母
# ouput: 返回大写字母

# ref: https://blog.csdn.net/zzyandzzzy/article/details/72236388
# 使用数据包式

if __name__ == '__main__':
    server_ip = ''
    server_port = 12000

    server_socket = socket(AF_INET, SOCK_DGRAM)

    # 绑定服务器ip和端口
    server_socket.bind((server_ip, server_port))

    print('服务器开始接收...')

    while True:
        # 接收消息
        resp, client_addr = server_socket.recvfrom(5)
        print(f"来自客户端{client_addr}的消息: {resp.decode()}")

        # 返回消息  
        msg = resp.decode().upper()
        server_socket.sendto(msg.encode(), client_addr)
