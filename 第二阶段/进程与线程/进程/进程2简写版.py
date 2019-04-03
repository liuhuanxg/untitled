# 使用进程，先要导入进程的包和进程的模块
# 进程的包时multiprocessing
# 进程的模块是process
from multiprocessing import Process

import os

import time

# 定义一个函数，这个函数是子进程的进程体，这个进程的工作
def son_process(num):
    print("这个是我创建的子进程，这是第%d个子进程，进程的ID是%d"%(num,os.getpid()))

if __name__ == '__main__':
    print("当前进程的ID为%d"%os.getpid())

    start_time = time.time()
    p = Process(target=son_process,args=(1,))
    p.start()
    p.join()
    end_time = time.time()
    print(end_time - start_time)
    # 结束语
    print("兄弟，游戏结束了兄弟，游戏结束了兄弟，游戏结束了兄弟，游戏结束了兄弟，游戏结束了")
