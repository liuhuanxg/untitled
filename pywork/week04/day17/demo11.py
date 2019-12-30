'''
设置守护线程
'''
from threading import Thread
import threading
import time
def get(num):
    for i in range(num):
        print(i)
        time.sleep(1)
if __name__ == '__main__':
    t1=Thread(target=get,args=(5,))
    # 将当前线程设置为守护线程来守护主线程
    # 需要在子线程开启之前设置
    # 当主线程结束时，守护线程也就结束，不管是否执行完成
    t1.setDaemon(True)
    t1.start()
    print('主线程结束了')

'''
threading.currentThread()--返回当前的线程变量
threading.enumerate()--返回一个包含正在运行的线程的列表
threading.active_count()--返回正在运行的线程的个数
threading.activeCount()--返回正在运行的线程的个数
与len(threading.enumerate())有相同的结果
'''
def sing():
    for i in range(10):
        print('唱歌%d'%(i+1),threading.current_thread())
        time.sleep(2)
def dance():
    for i in range(10):
        print('跳舞%d'%(i+1),threading.current_thread())
        time.sleep(1.5)
if __name__ == '__main__':
    t1=Thread(target=sing,name='刘德华')
    t2=Thread(target=dance,name='张惠妹')
    t1.start()
    t2.start()
    print(threading.enumerate())
    print(threading.activeCount())
    t1.join()
    t2.join()
    print('主线程结束')