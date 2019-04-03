from socket import  *
from  threading import Thread

udp_socket=socket(AF_INET,SOCK_DGRAM)
udp_socket.bind(('10.10.77.226',0000))
send_address=('10.10.77.226',1111)
def send_data():
    while True:
        content=input('客户端说：')+'\r\n'
        udp_socket.sendto(content.encode('gbk'),send_address)
def recv_data():
    while True:
        get_data=udp_socket.recvfrom(1024)
        print('%s:%s:%d'%(get_data[0].decode('gbk'),get_data[1][0],get_data[1][1]))
if __name__=='__main__':
    s_data=Thread(target=send_data)
    s_data.start()
    r_data=Thread(target=recv_data)
    r_data.start()






