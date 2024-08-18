from multiprocessing import Queue, Process
from time import sleep


def producer(q):
    for i in range(10):
        bz = "包子:{}".format(i + 1)
        q.put(bz)
        print("生产" + bz)
        sleep(1)


def consumer(q):
    for i in range(10):
        bz = q.get()
        print("消费" + bz)


if __name__ == '__main__':
    q = Queue(3)
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
