from queue import Queue as Q
from threading import Thread
from multiprocessing import Process
import time
import os, sys


def func2():
    print("func2 getppid:", os.getppid(), "func2 getpid:", os.getpid())
    # time.sleep(150)


def func1():
    print("func1 getppid:", os.getppid(), "getpid", os.getpid())
    # time.sleep(150)


if __name__ == '__main__':
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p1.start()
    p2.start()
    print(333)
    print("pid:", os.getpid())
    # time.sleep(10)
    sys.exit()
print("外层getppid：", os.getppid(), "外层getpid：", os.getpid())
