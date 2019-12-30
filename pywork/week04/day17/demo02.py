'''
多进程时，每个进程需要一份系统资源，资源不共享，两个进程互不干扰。
'''
from multiprocessing import Process
count=0
def hs1():
    global count
    for i in range(1000):
        count+=1
    print('函数1：',count)
def hs2():
    global count
    for i in range(1000):
        count+=1
    print('函数2：',count)
if __name__ == '__main__':
    # hs1()
    # hs2()
    p1=Process(target=hs1)
    p2=Process(target=hs2)
    p1.start()
    p2.start()