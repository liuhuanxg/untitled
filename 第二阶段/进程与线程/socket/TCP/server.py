import socket

# 创建一个TCP   TCP的第二个参数是  SOCK_STREAM
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcp_server_socket.bind(("",1111))

# 将创建的服务器socket的主动化为被动
# 监听
# 内置一个参数  这个参数是同时连接服务器的最大值
tcp_server_socket.listen(5)

# 等待连接
# 等待客户端的连接   没有参数  但是有返回值
# 返回一个元组   元组中的第一个元素是新生成的套接字
# 新生成的这个套接字专门处理当前连接的客户端
# 元组的第二个元素是当前连接的用户的IP地址和端口号
# 其实  第二个元素也是一个元组
# sccept陷入阻塞状态  等待客户端的连接
# 当执行到这不的时候  同时连接的资源又回到上一步(listen)
# 当前能够同时连接的人数还是5个人
new_socket,client_address = tcp_server_socket.accept()

# 接收客户端的信息   使用recv方法   不是recvfrom
# 返回值是客户端发送过来的信息
get_data = new_socket.recv(1024)

print(get_data.decode("gbk"))

new_socket.close()

tcp_server_socket.close()
