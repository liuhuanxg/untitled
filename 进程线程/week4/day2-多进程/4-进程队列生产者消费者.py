from multiprocessing import Process, Queue
import time


class Producer(Process):
    def __init__(self, q, name):
        super().__init__()
        self.q = q
        self.name = name

    def run(self):
        for i in range(15):
            bz = '包子：%d' % (i + 1)
            print(self.name + '生产' + bz)
            self.q.put(bz)
            time.sleep(1)


class Consumer(Process):
    def __init__(self, q, name):
        super().__init__()
        self.q = q
        self.name = name

    def run(self):
        for i in range(11):
            bz = self.q.get()
            print(self.name + '消费' + bz)


if __name__ == '__main__':
    q = Queue(3)
    p1 = Producer(q, '张三')
    p2 = Producer(q, '李四')
    c1 = Consumer(q, '进程1')
    c2 = Consumer(q, '进程2')
    c3 = Consumer(q, '进程3')
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    c3.start()
    p1.join()
    p2.join()
    c1.join()
    c2.join()
    c3.join()
    print("吃完了")
