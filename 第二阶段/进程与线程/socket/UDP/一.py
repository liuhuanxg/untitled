#使用UDP   那么先使用socket套接字
#使用socket创建UDPsocket套接字
from socket import  *
'''
第一件事   创建一个UDPsocket
第一个参数  家庭地址   使用udp的传输方式
如果使用本机传输数据的话，   AF_UNIX   用于同一台计算机之间的传输，是最不常用的
一般使用  AF_INET   用于互联网之间的传输
第二个参数是   类型
我们创建的是UDP   他的类型是：  SOCK_DGRAM（数据报套接字）
'''
udp_socket=socket(AF_INET,SOCK_DGRAM)

udp_socket.bind(('',1110))
#print(udp_socket)
# 发送数据
#首先要有数据   我们从键盘中获取数据
send_data=input('请输入数据：')+'\r\n'

#发送数据     确定对方IP地址
send_address=('10.10.77.226',8080)
'''
发送数据
使用udp_socket对象中的sendto方法  内置两个参数第一个参数是发送的数据
第二个参数是一个元组     元组里边是两个元素   第一个元素是IP地址，第二个元素是端口号
是你要发送给谁   对方的IP地址和端口号
'''
udp_socket.sendto(send_data.encode('gbk'),send_address)

'''
接受信息
使用udp_socket对象中的recvfrom方法
内置一个函数   函数是接收数据的最大值   单位是字节
返回值是一个元组    元组的第一个元素是16进制的信息  也就是接收到的内容
元组的第二个元素还是元组  元组内部是发送方的IP和端口号

'''
# get_data=udp_socket.recvfrom(1024)
# print(get_data[0].docode('gbk'))
# print(get_data[1])
#关闭资源
udp_socket.close()