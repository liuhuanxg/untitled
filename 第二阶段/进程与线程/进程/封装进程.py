from multiprocessing import Process
import os
import time

class MyProcess(Process):
    def __init__(self,i):
        super().__init__()
        self.num = i
    def run(self):
        print("这是第%d个子进程，当前进程为子进程，子进程ID为%d"%(self.num,os.getpid()))
        time.sleep(1)
if __name__ == '__main__':
    print("当前进程ID为%d"%os.getpid())
    for i in range(10):
        m = MyProcess(i+1)
        m.start()
        m.join()
