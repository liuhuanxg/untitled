from threading import Thread, Lock
import time

g_num = 0


def func1():
    global g_num
    mutextFlag = mutex.acquire(True)
    for i in range(1000000):
        if mutextFlag:
            g_num += 1
    mutex.release()
    print("func1:{}".format(g_num))


def func2():
    global g_num
    mutextFlag = mutex.acquire(True)
    for i in range(1000000):
        if mutextFlag:
            g_num += 1
    mutex.release()
    print("func1:{}".format(g_num))


if __name__ == '__main__':
    mutex = Lock()
    t1 = Thread(target=func1)
    t2 = Thread(target=func1)
    t1.start()
    t2.start()
