import socket

udpServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind(('10.10.77.226',8090))

while True:
    data,addr=udpServer.recvfrom(1024)
    print('客户端说：',data.decode('gbk'))
    info=input('服务器：')
    udpServer.sendto(info.encode('gbk'),addr)
udpServer.close()
