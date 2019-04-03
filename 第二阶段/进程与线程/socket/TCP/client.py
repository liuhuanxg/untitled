import  socket
tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

tcp_client_socket.connect(('10.10.77.226',52690))
tcp_client_socket.send('西瓜'.encode('gbk'))
tcp_client_socket.close()