import socket
import select
def main():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本机信息
    server_socket.bind(("127.0.0.1", 12000)) 
    # 重复使用绑定的信息
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 变为被动
    server_socket.listen(1024)
    # 设置套接字为非阻塞模式
    server_socket.setblocking(False)
    # 创建一个epoll对象
    epoll = select.epoll()
    # 为服务器端套接字server_socket的文件描述符注册事件
    epoll.register(...)
    
    new_socket_list = {}       
    client_address_list = {}     

    # 循环等待数据到达
    while True:
        # 检测并获取epoll监控的已触发事件
        epoll_list = ...
        # 对事件进行处理
        for fd, events in epoll_list:
            # 如果有新的连接请求递达
            if fd == server_socket.fileno():
                new_socket, client_address = server_socket.accept()
                print('有新的客户端到来%s'%str(client_address))
                
                # 为新套接字的文件描述符注册读事件
                ...

            # 如果监听到EPOLLIN事件, 表示对应的文件描述符可以读
            elif ...:
                # 处理逻辑
                ...


if __name__ == '__main__':
    main()