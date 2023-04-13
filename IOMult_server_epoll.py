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
    epoll.register(server_socket.fileno(), select.EPOLLIN)
    
    new_socket_list = {}       
    client_address_list = {}     

    # 循环等待数据到达
    while True:
        # 检测并获取epoll监控的已触发事件
        epoll_list = epoll.poll(1)
        # 对事件进行处理
        for fd, event in epoll_list:
            # 如果有新的连接请求递达
            if fd == server_socket.fileno():
                new_socket, client_address = server_socket.accept()
                print('有新的客户端到来%s'%str(client_address))
                
                # 为新套接字的文件描述符注册读事件
                new_socket.setblocking(0)
                epoll.register(new_socket.fileno(), select.EPOLLIN)
                new_socket_list[new_socket.fileno()] = new_socket
                client_address[new_socket.fileno()] = client_address
            # 如果监听到EPOLLIN事件, 表示对应的文件描述符可以读
            elif event & select.EPOLLIN:
                # 处理逻辑
                msg = new_socket_list[fd].recv(1024).decode()
                new_socket_list[fd].send(msg.upper().encode())
                
                epoll.modify(fd, select.EPOLLOUT)
                new_socket_list.pop(fd)
                client_address.pop(fd)

                



if __name__ == '__main__':
    main()