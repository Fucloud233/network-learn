from socket import *
import time

max_timeout_time = 5

if __name__ == '__main__':
    # 配置参数
    server_ip = "47.120.5.208"
    server_port = 12345
    data_size = 32
    send_num = 10
    
    # 配置socket
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.settimeout(max_timeout_time)

    # 运行程序 
    for i in range(send_num):
        # 发送数据
        data = data_size*'a'
        start_time = time.time()
        client_socket.sendto(data.encode(), (server_ip, server_port))

        try:
            # 接收数据
            ret_message, server_address = client_socket.recvfrom(32)
            end_time = time.time()
            
            # 当接收成功时
            need_time = end_time - start_time
            print("Ping %d RTT : %.2fs"%(i, need_time))
        except Exception:
            # 当接受失败时
            print("Ping %d lost"%(i))