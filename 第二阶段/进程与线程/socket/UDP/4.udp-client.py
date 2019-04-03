from  socket import *

host='10.10.77.226'
port=8101
bufsiz=1024
addc=(host,port)
udpclisock=socket(AF_INET,SOCK_DGRAM)

while  True:
    msg=input('客户端说：')
    udpclisock.sendto(msg.encode('gbk'), addc)
    data,adds=udpclisock.recvfrom(bufsiz)
    if not data:break
    print('服务器回答:',data.decode('gbk'))
udpclisock.close()
