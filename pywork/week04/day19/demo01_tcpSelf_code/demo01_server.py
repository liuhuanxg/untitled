import threading
from socket import *
server_socket=socket(AF_INET,SOCK_STREAM)
local_address=('10.10.107.240',9999)
server_socket.bind(local_address)
server_socket.listen(5)    # 监听 5--最多可收5个链接
print('server_socket:',server_socket)
lianjie=server_socket.accept()
def send():
    while True:
        # print('收到的链接',lianjie)
        # lianjie[0]比server_socket多一个远程地址
        x=input('')
        if x=='q' or x=='quit' or x=='exit':
            break
        lianjie[0].send(x.encode('utf-8'))
def get():
    while True:
        r = lianjie[0].recv(124)
        print(r.decode('utf-8'))
if __name__ == '__main__':
    t1=threading.Thread(target=send)
    t2=threading.Thread(target=get)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    server_socket.close()