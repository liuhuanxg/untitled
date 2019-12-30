import threading
from socket import *
client_socket=socket(AF_INET,SOCK_STREAM)
dest_address=('10.10.107.240',9999)
client_socket.connect(dest_address)
def send():
    while True:
        d=input('')
        if d=='q' or d=='quit' or d=='exit':
            break
        client_socket.send(d.encode('utf-8'))
def get():
    while True:
        r = client_socket.recv(124)
        print(r.decode('utf-8'))
if __name__ == '__main__':
    t1=threading.Thread(target=send)
    t2 = threading.Thread(target=get)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    client_socket.close()