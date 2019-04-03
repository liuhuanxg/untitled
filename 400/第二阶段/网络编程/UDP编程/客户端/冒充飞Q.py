'''
tcp是建立可靠的连接，并且通信双方都可以以流的形式发送数据。
相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，
就可以直接发送数据包，单数不知道能不能到达

虽然UDP差US农户数据不可靠，但他的优点是和TCP相比速度，对于要求
不高的数据可用UDP

'''
import  socket
import time
'''
udp_data=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# udp_data.bind=(('',8888))
udp_data.connect(('10.10.77.226',8080))
s=input('请输入数据：')+'\r\n'
udp_data.send(s.encode('gbk'))
time.sleep(1)
udp_data.close()
'''
for i in range(256):
    ip='10.10.77.%d'%i
    print(ip)
    udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp.connect((ip,8080))