from threading import Thread
import time
from queue import Queue


def producer(q,name):
    count = 1
    while True:
        bz = name + "生产的包子{}".format(count)
        q.put(bz)
        print("bz",bz)
        time.sleep(1)
        count += 1


def consumer(q,name):
    while True:
        time.sleep(1)
        bz = q.get()
        print(name,"吃",bz)

if __name__ == '__main__':
    q = Queue(5)
    p =Thread(target=producer,args=(q,"张三"))
    q =Thread(target=consumer,args=(q,"李四"))
    p.start()
    q.start()