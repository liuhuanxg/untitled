from threading import Thread, Lock
import time


def func1():
    lock1.acquire()
    print("函数1的锁1")
    # time.sleep(1)
    lock2.acquire()
    print("111111111")
    lock2.release()
    lock1.release()


def func2():
    lock2.acquire()
    print("函数2的锁2")
    lock1.acquire()
    time.sleep(1)
    print("222222222")
    lock1.release()
    lock2.release()


if __name__ == '__main__':
    lock1 = Lock()
    lock2 = Lock()
    t1 = Thread(target=func1)
    t2 = Thread(target=func2)
    t1.start()
    t2.start()
