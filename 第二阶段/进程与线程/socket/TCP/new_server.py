import socket
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server_socket.bind(("",1111))
tcp_server_socket.listen(5)
while True:
    new_socket,client_address = tcp_server_socket.accept()
    get_data = new_socket.recv(1024)
    print(get_data.decode("gbk"))
    send_data='world'
    new_socket.send(send_data.encode('gbk'))
    new_socket.close()
tcp_server_socket.close()
