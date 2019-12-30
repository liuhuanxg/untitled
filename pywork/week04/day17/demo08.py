'''
进程池
'''
from multiprocessing import Pool
import time

# def hs(name):
#     for i in range(5):
#         print(name,i)
#         time.sleep(1)
# if __name__ == '__main__':
#     p=Pool(3)
#     a='abcde'
#     for x in a:
#         p.apply(hs,(x,))    # 阻塞式，同时只跑一个进程
#     p.close()

def hs(name):
    for i in range(5):
        print(name,i)
        time.sleep(1)
if __name__ == '__main__':
    p=Pool(3)
    a='abcde'
    for x in a:
        # 非阻塞式，同时可跑多个进程，最多要看进程池的容量。
        # 必须加join()，在close()后加
        p.apply_async(hs,(x,))
    p.close()
    p.join()    # 阻塞主进程，等待子进程结束