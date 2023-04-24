import random
import time
from socket import *

def run_server():
    server_ip = ''
    server_port = 12345

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen()

    print('The server is running')

    while True:
        connection_socket, client_addr = server_socket.accept()
        hello_msg = '你好，欢迎来到我的服务器！\n输入你的姓名，让我告诉你的运势'
        connection_socket.send(hello_msg.encode())

        # 得到姓名
        name = connection_socket.recv(1024).decode()

        value, err_msg = get_lucky_value(name)

        # 运势消息
        lucky_msg = err_msg
        if value != -1:
            lucky_msg = name + "今天的幸运值: " + str(value) + ' ' + lucky_value_display(value)

        connection_socket.send(lucky_msg.encode())

def get_lucky_value(name):
    # 对名字进行处理
    try:
        assert(isinstance(name, str))

        # 判断是否满足长度        
        if len(name)>4 :
            return -1, '输入名字太长了'
        for c in name:
            if c < '\u4e00' or c > '\u9fa5':
                return -1, '请输入合法名字'
    except TypeError:
        return -1, '输入的不是字符串类型'

    # 生成幸运值
    random.seed(get_seed(name))
    lucky_value = random.randint(0,100)

    return lucky_value, ''

# 计算种子
def get_seed(name):
    # 计算姓名种子
    sum = 0
    
    for i in range(len(name)):
        sum += ord(name[i])
    sum %= 1000

    # 计算日期种子
    date = (int)(time.time() / 24 / 60 / 60)
    return date + sum

# 将幸运值显示出来
def lucky_value_display(value:int):
    total_len = 20
    len = (int) (value * total_len / 100)
    res = '[' + '|'*len + ' '*(total_len - len) + ']'
    return res

# 测试函数
def test(name:str):
    lucky_value, err_msg = get_lucky_value(name)
    
    res_msg = err_msg
    if lucky_value!=-1:
        res_msg = str(lucky_value) + lucky_value_display(lucky_value)
    print(res_msg)


# 主函数
if __name__=='__main__':
    run_server()