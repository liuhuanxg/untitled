'''
进程是资源分配的最小单位，线程是CPU调度的最小单位
线程--轻型进程
进程中的所有线程共享进程中的所有资源
'''
from threading import Thread
import time
import os
# count=0
# def hanshu1():
#     global count
#     for i in range(100):
#         count+=1
#     print('函数1',count)
# def hanshu2():
#     global count
#     for i in range(100):
#         count+=1
#     print('函数2',count)
# if __name__ == '__main__':
#     t1=Thread(target=hanshu1)
#     t2=Thread(target=hanshu2)
#     t1.start()
#     t2.start()

# 同一个进程中的两个线程
def sing():
    for i in range(10):
        print('唱歌%d'%(i+1))
        time.sleep(1)
    print(os.getpid())
def dance():
    for i in range(10):
        print('跳舞%d'%(i+1))
        time.sleep(1)
    print(os.getpid())
if __name__ == '__main__':
    t1=Thread(target=sing)
    t2=Thread(target=dance)
    t1.start()
    t2.start()



