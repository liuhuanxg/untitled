import time
from multiprocessing import Process, Queue


class Producer(Process):
    def __init__(self, q, name):
        self.q = q
        self.name = name
        super().__init__()

    def run(self):
        for i in range(15):
            bz = '包子：%d' % (i + 1)
            print(self.name + '生产' + bz)
            self.q.put(bz)
            time.sleep(1)


class Consumer(Process):
    def __init__(self, q, name):
        self.q = q
        self.name = name
        super().__init__()

    def run(self):
        for i in range(10):
            bz = self.q.get()
            print(self.name + '消费' + bz)


if __name__ == '__main__':
    q = Queue(40)
    p1 = Producer(q, '张三')
    p2 = Producer(q, '李四')
    c1 = Consumer(q, '111')
    c2 = Consumer(q, '222')
    c3 = Consumer(q, '333')
    p1.start()
    p2.start()
    p1.join()  # 阻塞主进程，直到这个子进程结束
    c1.start()
    c2.start()
    c3.start()
