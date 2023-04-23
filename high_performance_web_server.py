from socket import *
import threading

def thread_func(conn) -> None:
    # 接收数据
    msg = conn.recv(1024).decode()
    # print(msg)
    # 返回数据
    conn.send(msg.upper().encode())
    # 关闭连接
    conn.close()

def multithreading_server_BIO(ip: str, port: int):
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 重复使用绑定的信息
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定端口号和套接字
    serverSocket.bind((ip, port))
    # 开启监听，设置1024个连接缓冲，暂时将连接挂起
    serverSocket.listen(1024)
    print('The server is ready to receive')

    # 用来存储正在运行的线程
    threads = []

    while True:
        # 等待接受客户端的连接
        conn, addr = serverSocket.accept()
        # print(addr)
        
        # (1) 使用多线程
        thread = threading.Thread(target=thread_func, args=(conn, ))
        threads.append(thread)
        thread.start()

        # (2) 使用单线程
        # msg = conn.recv(1024).decode()
        # conn.send(msg.upper().encode())
        # conn.close()

    # 等待多线程运行完毕
    for thread in threads:
        thread.join()
       
    serverSocket.close()

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    multithreading_server_BIO('', serverPort)
