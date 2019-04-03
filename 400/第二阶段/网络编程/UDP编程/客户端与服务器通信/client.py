import  socket

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input('客户端说：')
    client.sendto(data.encode('gbk'),('10.10.77.226',8090))
    info=client.recv(1024).decode('gbk')
    print('服务器说：',info)
client.close()