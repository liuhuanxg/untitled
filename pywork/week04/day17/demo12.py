'''
线程子类化
'''
import threading,time,os
from threading import Thread
# class T(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         for i in range(10):
#             print(self.name,'跳舞%d'%(i+1))
#             time.sleep(1)
# if __name__ == '__main__':
#     t=T('张三')
#     t.start()

class T(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        for i in range(10):
            print(self.name,'跳舞%d'%(i+1))
            time.sleep(1)
        print(os.getpid())
class C(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        for i in range(10):
            print(self.name, '唱歌%d' % (i + 1))
            time.sleep(1)
        print(os.getpid())
if __name__ == '__main__':
    t=T('张三')
    c=C('张三')
    t.start()
    c.start()