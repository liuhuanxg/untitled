# 编辑一个web服务器
# 使用socket  也就是说TCP编辑
import socket

import re

import multiprocessing

HTTP_DIR = "./www"

def client_handle(client_socket):
    request = client_socket.recv(2048)

    request_start = request.splitlines()

    request_start_line = request_start[0]

    # print(request_start_line.decode("utf-8"))

    file_name = re.match(r"\w+ (/[^ ]*) ",request_start_line.decode("utf-8")).group(1)
    print(file_name)

    if file_name == "/":
        file_name = "/index.html"
    try:
        file = open(HTTP_DIR + file_name,"rb")
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"

        response_header = "Server : Fuck\r\n"

        response_body = "404   not  found"
    else:
        file_data = file.read()
        file.close()
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server : Fuck\r\n"

        response_body = file_data.decode("utf-8")

    response = response_start_line + response_header + "\r\n" + response_body

    client_socket.send(bytes(response,"utf-8"))

    client_socket.close()


if __name__ == '__main__':
    # 创建一个流式套接字  也就是tcp的socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 绑定IP和端口
    tcp_server_socket.bind(("",8769))

    # 由主动化为被动
    tcp_server_socket.listen(128)

    # 等待客户端的连接
    # 一直等待客户端的连接   也就是说   服务器没有关闭的时候
    while True:
        # 等待连接  生成新的套接字和接收当前连接的客户端的地址
        new_socket,client_address = tcp_server_socket.accept()

        # 进行服务器交互
        client_process = multiprocessing.Process(target=client_handle,args=(new_socket,))

        # 启动进程
        client_process.start()

        # 关闭当前连接的客户端的资源
        new_socket.close()

    tcp_server_socket.close()
