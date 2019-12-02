import time
from threading import Thread


def get(num):
    for i in range(num):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=get, args=(5,))
    t1.setDaemon(True)  # 设置守护线程，主线程结束就会结束
    t1.start()
    print("主线程结束了")
