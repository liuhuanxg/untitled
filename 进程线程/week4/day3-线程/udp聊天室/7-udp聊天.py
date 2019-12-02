from socket import *
import threading
udp_s=socket(family=AF_INET,type=SOCK_DGRAM)

dest_address=("10.10.107.68",8899)
udp_s.bind(("10.10.107.111",9999))
def send():
    while True:
        data = input("请输入要发送的数据：")
        udp_s.sendto(data.encode("utf-8"),dest_address)

def get():
    while True:
        msg = udp_s.recvfrom(124)
        print("msg:", msg[0].decode())

if __name__ == '__main__':
    t1=threading.Thread(target=send)
    t2=threading.Thread(target=get)
    t1.start()
    t2.start()