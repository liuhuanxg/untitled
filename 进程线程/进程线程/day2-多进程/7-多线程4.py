import time
from threading import Thread
import threading


def sing():
    for i in range(10):
        print("唱歌{}".format(i + 1), threading.current_thread())
        time.sleep(1)


def dance():
    for i in range(10):
        print("跳舞{}".format(i + 1), threading.current_thread())
        time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=sing, name="线程1")
    t2 = Thread(target=dance)
    t1.start()
    t2.start()
    print(threading.enumerate())
    print(threading.active_count())  # 激活中的线程数量
    print(threading.activeCount())
    t1.join()
    t2.join()

    print("结束")
