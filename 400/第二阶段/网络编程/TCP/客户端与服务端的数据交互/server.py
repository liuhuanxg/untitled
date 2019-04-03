import socket
#创建一个socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP端口
server.bind(('192.168.191.1',8088))
#监听
server.listen(5)
print('服务器启动成功。')
#等待连接
clientSocket, clientAddress = server.accept()
#此服务器暂时只能接收一个客户端连接
print(['%s--%s'%(str(clientSocket),clientAddress)])
while True:
   data=clientSocket.recv(1024)
   print('客户端说：' +data.decode('utf-8'))
   sendData=input('输入返回给客户端的数据：')
   clientSocket.send(sendData.encode('utf-8'))
