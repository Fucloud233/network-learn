from socket import *
import threading
import time
import random

# 总共10个线程
client_thread_num = 100
# 服务器的IP地址或主机名
serverName = '192.168.118.128'
# serverName = 'localhost'
# 服务器端口号
serverPort = 12000

done_num = 0
done_mutex = threading.Lock()

# 随意定义一些数据，用于发送
data = 'q8e7777773yr387yrx12yeemxhy120xn120ye817mexh12emh812h345435435v45v4v43v4v433v4435v3m'

# 发送函数
def send(data, thread_i):
    global done_num
    global done_mutex
    # 每个线程如果失败的话循环重来！
    while True:
        try:
            while True:
                try:
                    clientSocket = socket(AF_INET, SOCK_STREAM)
                    break
                except Exception as e:
                    pass
            # 设置socket选项 
            clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            clientSocket.connect((serverName, serverPort))
            clientSocket.sendall(data.encode())
            ret_msg = clientSocket.recv(1024).decode()
            # 检测传输的消息是否正常
            if ret_msg != data.upper():
                print('err ' + ret_msg)

            done_mutex.acquire()
            done_num += 1
            done_mutex.release()
            # print(done_num)
            break
        except Exception as e:
            # print(e)
            pass
        finally:
            clientSocket.close()

if __name__ == '__main__':
    thread_list = []
    # 创建线程
    for i in range(client_thread_num):
        t = threading.Thread(target=send, args=(data, i))
        thread_list.append(t)
    
    # 等待线程运行，并计时
    time_start = time.time_ns()

    # 启动线程
    for t in thread_list:
        while True:
            try:
                t.start()
                break
            except Exception as e:
                pass

    for t in thread_list:
        t.join()
    time_end = time.time_ns()
    print("thread_num: %d, done_num: %d" % (client_thread_num, done_num))
    print('time cost: ', time_end - time_start, 'ns', (time_end - time_start) / (1e9), 's')
