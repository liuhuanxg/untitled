from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("192.168.191.1",0000))
while True:
    get_data=udp_socket.recvfrom(1024)
    print('%s:%s:%d'%(get_data[0].decode('gbk'),get_data[1][0],get_data[1][1]))
udp_socket.close