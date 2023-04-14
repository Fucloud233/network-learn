import select
import socket
import queue

# http://pymotw.com/2/select/

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12000))
    server_socket.listen(1024) 
    server_socket.setblocking(False)

    # 将服务器套接字加入等待读就绪的套接字列表
    inputs = [server_socket]   
    outputs = []
    exception = []
    # 用来存储接收的数据
    msg_queue = {}

    print('The server is ready to receive')
    while True:
        # 调用select()函数，阻塞等待      
        readable, writable, _ = select.select(inputs, outputs, exception)
        # 数据抵达，循环
        for temp_socket in readable:
            # 监听到有新的连接
            if temp_socket is server_socket:
                connected_socket, _ = temp_socket.accept()
                inputs.append(connected_socket)
            # 接收数据准备完毕
            else:
                # 读取客户端连接发送的数据
                msg = temp_socket.recv(1024).decode()
                # 若有数据递达，对数据进行处理
                if msg:
                    outputs.append(temp_socket)
                    msg_queue[temp_socket] = msg
                    # print(msg)
                # 若未接收到数据，断开连接
                else:
                    temp_socket.close()
                inputs.remove(temp_socket)
        # 发送数据准备完毕
        for temp_socket in writable:
            msg = msg_queue.get(temp_socket)
            if msg != None:
                temp_socket.sendall(msg.upper().encode())
            temp_socket.close()
            outputs.remove(temp_socket)
    server_socket.close() 

if __name__ == '__main__':
    main()