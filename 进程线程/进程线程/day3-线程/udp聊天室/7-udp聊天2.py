from socket import *

udp_s=socket(family=AF_INET,type=SOCK_DGRAM)

udp_s.bind(("10.10.107.111",9999))
dest_address=("10.10.107.111",8899)


while True:
    data = input("请输入要发送的数据：")
    udp_s.sendto(data.encode("utf-8"),dest_address)

    msg,addr=udp_s.recvfrom(1024)
    print("msg:",msg.decode())