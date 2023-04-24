from socket import *
import sys
import time

max_timeout_time = 5

def print_result(server_ip:str, send_num:int, rtt_list:list[int]) -> None:
    receive_num = len(rtt_list)

    # 计算和打印 数量相关信息
    lost_num = send_num-receive_num
    lost_rate = int((lost_num / send_num) * 100)

    print(f'{server_ip} 的 Ping 统计信息：')
    print(f'\t数据包：已发送 = {send_num}, 已接收 = {receive_num}, ', end='')
    print(f'丢失 = {lost_num} ({lost_rate}% 丢失), ')
    
    # 计算和打印 RTT信息
    if receive_num == 0:
        return

    total_time = 0
    max_rtt = min_rtt = rtt_list[0]
    for rtt in rtt_list:
        total_time += rtt
        if rtt > max_rtt:
            max_rtt = rtt
        if rtt < min_rtt:
            min_rtt = rtt
    average_time = 0
    if receive_num != 0:
        average_time = int(total_time/receive_num)

    print(f'往返形成的估计时间(以毫秒为单位): ')
    print(f'\t最短 = {min_rtt}ms, 最长 = {max_rtt}ms, 平均 = {average_time}ms')

def parse_parameter(argv:list[str]) -> map:
    # 判断参数是否为偶数
    if len(argv)%2 == 1 :
        raise Exception

    # 参数记录字典
    res = {
        "ip": argv[1].split(':')[0],
        "port": int(argv[1].split(':')[1]),
        "num": 4,
        "size": 32,
    }
    
    # 解析参数的闭包
    def parse(field:str, value:str, res:dict) -> None:
        # 判断数据是否为整型
        try:
            isinstance(value, (int))
        except TypeError:
            raise TypeError

        value = int(value)

        # 接收参数
        if field == '-n':
            res['num'] = value
        elif field == '-l':
            res['size'] = value
        else:
            raise Exception

    # 循环解析
    for i in range(2, len(argv), 2):
        parse(argv[i], argv[i+1], res)

    return res

if __name__ == '__main__':
    # 记录接收的参数
    argv = sys.argv

    # 验证参数类型
    try:
        parameters = parse_parameter(argv)
    except Exception:
        print('用法: python %s <IP地址:端口> -n <发送次数> -l <数据大小>'%argv[0])
        exit(0)
    
    # 得到参数
    server_ip = parameters['ip']
    server_port =  parameters['port']
    data_size = parameters["size"]
    send_num = parameters["num"]
    
    # 配置socket
    client_socket = socket(AF_INET, SOCK_DGRAM)
    client_socket.settimeout(max_timeout_time)

    # 记录所有rtt
    rtt_list = []

    # 运行程序 
    print(f'正在 Ping {server_ip} 具有 {data_size} 字节的数据: ')
    for i in range(send_num):
        
        # 发送数据
        data = data_size*'a'
        start_time = time.time()
        client_socket.sendto(data.encode(), (server_ip, server_port))

        try:
            # 接收数据
            ret_message, server_address = client_socket.recvfrom(data_size)
            end_time = time.time()
            
            # 当接收成功时
            rtt = int((end_time - start_time)*1000)
            rtt_list.append(rtt)

            print(f'来自 {server_address[0]} 的回复: ', end='')
            print(f'字节={len(ret_message)} 时间={rtt}ms')
        except Exception :
            # 当接受失败时
            print("请求超时")
    
    # 打印统计数据
    print_result(server_ip, send_num, rtt_list)

    
