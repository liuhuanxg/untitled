'''
父子进程ID
传参
'''
from multiprocessing import Process
import os
def sing(num):
    print('参数：',num,'进程的ID：',os.getpid(),'父进程ID：',os.getppid())

def dance(num):
    print('参数：',num,'进程的ID：',os.getpid(),'父进程ID：',os.getppid())

if __name__ == '__main__':
    print('主进程ID：',os.getpid())
    p1=Process(target=sing,args=(9,))
    p2=Process(target=dance,args=(99,))
    p1.start()
    p2.start()