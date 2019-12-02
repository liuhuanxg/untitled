from threading import Thread
import time, threading


class A():
    pass


def func1(name):
    A.name = name
    func2()


def func2():
    # time.sleep(1)
    print(threading.current_thread(), A.name)


if __name__ == '__main__':
    t1 = Thread(target=func1, args=("张三",), name=" ")
    t2 = Thread(target=func1, args=("李四",), name="线程2")
    t1.start()
    t2.start()
