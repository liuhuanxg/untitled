'''
multiprocessing 库
跨平台版本的多进程模块，提供了一个Process来代表一个进程对象

'''

from  multiprocessing import Process
from time import  sleep

def run(str):
    while True:
        print('sunck is a %s man '%(str))
        sleep(3)
if __name__=='__main__':
    print('主（父）进程启动')
     #创建一个子进程
    #target说明进程执行的任务，执行上边的run方法
    #用元组表示传递的参数，传递一个参数后边加','
    p=Process(target=run,args=('good',))
    p.start()
    while True:
        print('sunck is a nice man ')
        sleep(2)
