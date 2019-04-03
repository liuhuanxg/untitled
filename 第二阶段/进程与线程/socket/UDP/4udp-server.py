from  socket import *

host='10.10.77.226'
port=8101
bufsiz=1024
adds=(host,port)
udpsersock=socket(AF_INET,SOCK_DGRAM)
udpsersock.bind(adds)
while  True:
    msg=input('服务器说：')
    data,addc=udpsersock.recvfrom(bufsiz)
    udpsersock.sendto(msg.encode('gbk'),addc)
    if not data:break
    print('客户端回答:',data.decode('gbk'))
udpsersock.close()

