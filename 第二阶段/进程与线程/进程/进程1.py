#使用进程，先要导入进程的包和进程的模块
#进程的包是multiprocessing
#进程的模块是process
from multiprocessing import Process
import os
import time
#定义一个函数，这个函数是子进程的进程体，这个进程的工作
def son_process(num):
    print("这个是我创建的子进程，这是第%d个子进程，进程的ID是%d"%(num,os.getpid()))

if __name__=='__main__':
    #获取当前进程的ID  使用getpid方法
    print('当前进程的ID为%d'%os.getpid())
    #目前我要创建出10条子进程
    #使用循环的方式创建出子进程
    start_time=time.time()
    for i in range(10):
        #使用Process创建进程，其实就等同于实例化Process类
        #实例化Process类，至少要有两个参数
        #第一个参数是一个函数，函数就是我要创建的进程的工作[是一个自定义函数]使用target传入
        #第二个进程是一个元组，因为我的第一个参数是使用target传入的
        #所以第一个参数等同于函数的调用，但是又少了实参列表
        #我们就不可以把第二个函数看成是实参列表
        #第二个参数就是函数（子进程体）的参数
        p=Process(target=son_process,args=(i+1,))
        #因为在p的对象里面不允许创建完成后直接执行
        #他需要启动一下进程。使用start方法
        p.start()
        #为了规范（创建的子进程）进程的执行循环，那么我们使用join方法限制
        p.join()
    end_time=time.time()
    print(end_time-start_time)

