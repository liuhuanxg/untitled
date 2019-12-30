import threading
from socket import *
udp_s=socket(AF_INET,SOCK_DGRAM)
local_address=('10.10.107.240',9999)
udp_s.bind(local_address)    # 我
dest_address=('10.10.107.68',8899)    # 对方
def send():
    while True:
        data = input()
        udp_s.sendto(data.encode('utf-8'), dest_address)
def get():
    while True:
        s, addr = udp_s.recvfrom(124)
        print(s.decode('utf-8'))
if __name__ == '__main__':
    t1=threading.Thread(target=send)
    t2=threading.Thread(target=get)
    t1.start()
    t2.start()