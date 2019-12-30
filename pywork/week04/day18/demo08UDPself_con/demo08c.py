# 不同机器，端口号可相同
from socket import *
import threading
udp_s = socket(AF_INET, SOCK_DGRAM)
dest_address = ('10.10.107.240', 9999)    # 对方
udp_s.bind(('10.10.107.240', 8899))    # 我
def send():
    while True:
        data = input()
        udp_s.sendto(data.encode('utf-8'), dest_address)

def get():
    while True:
        s, addr = udp_s.recvfrom(124)    # 一次接收124字节的字符
        print(s.decode('utf-8'))

if __name__ == '__main__':
    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=get)
    t1.start()
    t2.start()