from threading import Thread
import time
from os import getpid


def sing():
    for i in range(10):
        print("唱歌{}".format(i + 1), getpid())
        time.sleep(1)


def dance():
    for i in range(10):
        print("跳舞{}".format(i + 1), getpid())
        time.sleep(1)


if __name__ == '__main__':
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()
