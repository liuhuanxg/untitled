from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("10.10.77.226",1024))
num=1
while True:
    get_data=udp_socket.recvfrom(1024)
    print('%s:%s:%d'%(get_data[0].decode('gbk'),get_data[1][0],get_data[1][1]))
    if num<6:
        udp_socket.sendto('OK'.encode('gbk'),get_data[1])
    else:
        udp_socket.sendto('你好'.encode('gbk'),get_data[1])
    num+=1
udp_socket.close
