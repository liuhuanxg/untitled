'''
进程子类化
'''
from multiprocessing import Queue,Process
import os,time
# class SubProcess(Process):
#     def __init__(self,x):
#         super().__init__()
#         self.x=x
#     # 重新编写run函数，覆盖父类的run方法。进程启动时调用此方法
#     def run(self):
#         for i in range(self.x):
#             print('启动进程',i,os.getpid())
#             time.sleep(1)
# if __name__ == '__main__':
#     p=SubProcess(3)
#     # 不同于直接调用run函数，这里是启动进程
#     p.start()
#     p1=SubProcess(3)
#     p1.start()


# class Producer(Process):
#     def __init__(self,q,name):
#         super().__init__()
#         self.q = q
#         self.name = name
#     def run(self):
#         for i in range(15):
#             bz = '包子：%d' % (i + 1)
#             print(self.name+'生产' + bz)
#             self.q.put(bz)
#             time.sleep(1)
# class Consumer(Process):
#     def __init__(self,q,name):
#         super().__init__()
#         self.q = q
#         self.name = name
#     def run(self):
#         for i in range(10):
#             bz = self.q.get()
#             print(self.name+'消费' + bz)
# if __name__ == '__main__':
#     q=Queue(40)
#     p1=Producer(q,'张三')
#     p2=Producer(q,'李四')
#     c1=Consumer(q,'111')
#     c2=Consumer(q,'222')
#     c3=Consumer(q,'333')
#     p1.start()
#     p2.start()
#     p1.join()    # 阻塞主进程，直到这个子进程结束
#     c1.start()
#     c2.start()
#     c3.start()

class A():
    def __init__(self):
        self.name="张三"
class B(A):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def show(self):
        print(self.name)
b=B("李四")
b.show()