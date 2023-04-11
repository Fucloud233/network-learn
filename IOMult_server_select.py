import select
import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12000))
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.listen(1024) 

    # 将服务器套接字加入等待读就绪的套接字列表
    inputs = [server_socket]   

    while True:
        # 调用select()函数，阻塞等待      
        readable, _, _ = select.select(inputs, [], [])
        # 数据抵达，循环
        for temp_socket in readable:
            # 监听到有新的连接
            if temp_socket == server_socket:
                connected_socket, _ = temp_socket.accept()
                inputs.append(connected_socket)
            # 有数据到达
            else:
                # 读取客户端连接发送的数据
                msg = temp_socket.recv(1024).decode()
                # 若有数据递达，对数据进行处理
                if msg:
                    temp_socket.sendall(msg.upper().encode())
                # 若未接收到数据，断开连接
                inputs.remove(temp_socket)
                temp_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()