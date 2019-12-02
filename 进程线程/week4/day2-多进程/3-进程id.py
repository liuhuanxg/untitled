from multiprocessing import Process
import time
import os


def sing():
    print("进程1:", os.getpid(), "父进程：", os.getppid())
    for i in range(10):
        print("我在唱第{}句歌词。".format(i + 1))
        time.sleep(1)


def dance():
    print("进程2:", os.getpid(), "父进程：", os.getppid())
    for i in range(10):
        print("我在跳第{}支舞。".format(i + 1))
        time.sleep(1)


def eat():
    print("进程3:", os.getpid(), "父进程：", os.getppid())
    for i in range(10):
        print("我在吃第{}碗饭。".format(i + 1))
        time.sleep(1)


def drink():
    print("进程4:", os.getpid(), "父进程：", os.getppid())
    for i in range(10):
        print("我在喝第{}杯酒。".format(i + 1))
        time.sleep(1)


def run():
    print("进程5:", os.getpid(), "父进程：", os.getppid())
    for i in range(10):
        print("我在跑第{}圈步。".format(i + 1))
        time.sleep(1)


if __name__ == '__main__':
    t1 = Process(target=sing)
    t2 = Process(target=dance)
    t3 = Process(target=eat)
    t4 = Process(target=drink)
    t5 = Process(target=run)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
