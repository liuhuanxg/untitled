# Python 0715 吕佳
# 进程
# from multiprocessing import Process
# import time
# def sing():
#     for i in range(3):
#         print('我在唱第{}句歌词'.format(i+1))
#         time.sleep(1)
# def dance():
#     for i in range(3):
#         print('我在跳第{}段舞蹈'.format(i+1))
#         time.sleep(1)
# if __name__ == '__main__':
#     # sing()
#     # dance()
#     p1=Process(target=sing)
#     p2=Process(target=dance)
#     p1.start()
#     p2.start()

'''
多进程时，每个进程需要一份系统资源，资源不共享，两个进程没有关系
'''
# from multiprocessing import Process
# count=0
# def hs1():
#     global count
#     for i in range(100):
#         count+=1
#     print('函数1：',count)
# def hs2():
#     global count
#     for i in range(100):
#         count+=1
#     print('函数2：',count)
# if __name__ == '__main__':
#     # hs1()
#     # hs2()
#     p1=Process(target=hs1)
#     p2=Process(target=hs2)
#     p1.start()
#     p2.start()

'''
父子进程ID
传参
'''
# from multiprocessing import Process
# import os
# def sing(num):
#     print('参数：',num,'进程ID：',os.getpid(),'父进程ID：',os.getppid())
# def dance(num):
#     print('参数：', num, '进程ID：', os.getpid(), '父进程ID：',os.getppid())
# if __name__ == '__main__':
#     print('主进程ID：',os.getpid())
#     p1=Process(target=sing,args=(9,))
#     p2=Process(target=dance,args=(99,))
#     p1.start()
#     p2.start()

'''
队列--先进先出
put()--向队列中存放数据，若已满，此方法将阻塞至有空间可用为止。
get()--返回队列中的一个项目，若列表为空，此方法将阻塞，直到队列中有项目可用为止。
qsize()--获取队列中的数据数量
full()--判断队列是否已满
empty()--判断队列中的数据是否空
'''
# from multiprocessing import Queue
# q=Queue(4)
# q.put('包子')
# q.put('面条')
# print(q.qsize())
# q.put('香蕉')
# print(q.full())
# while q.qsize()>0:
#     print(q.get())
# print(q.empty())

'''
block=False--不等待，直接抛出异常
'''
from multiprocessing import Queue
# q=Queue(3)
# q.put(10)
# q.put(20)
# q.put(30)
# try:
#     q.put(40,block=False)
# except:
#     print('队列已满')
# print('结束')

# q=Queue(3)
# q.put(10)
# q.put(20)
# q.get()
# q.get()
# try:
#     q.get(block=False)
# except:
#     print('队列已空')
# print('结束')

'''
多进程间的通信
'''
# from multiprocessing import Process,Queue
# import time
# def producer(q):
#     for i in range(10):
#         bz='包子：%d'%(i+1)
#         print('生产',bz)
#         q.put(bz)
#         time.sleep(1)
# def consumer(q):
#     for i in range(10):
#         bz=q.get()
#         print('消费',bz)
# if __name__ == '__main__':
#     q=Queue(3)
#     p1=Process(target=producer,args=(q,))
#     p2=Process(target=consumer,args=(q,))
#     p1.start()
#     p2.start()

'''
进程子类化
'''
from multiprocessing import Process,Queue
import time,os
# class SubProcess(Process):
#     def __init__(self,x):
#         super().__init__()
#         self.x=x
#     def run(self):
#         for i in range(self.x):
#             print('启动进程',i,os.getpid())
#             time.sleep(1)
# if __name__ == '__main__':
#     p=SubProcess(3)
#     p.start()
#     p1=SubProcess(3)
#     p1.start()

# class Producer(Process):
#     def __init__(self,q,name):
#         super().__init__()
#         self.q=q
#         self.name=name
#     def run(self):
#         for i in range(15):
#             bz = '包子：%d' % (i + 1)
#             print(self.name + '生产' + bz)
#             self.q.put(bz)
#             time.sleep(1)
# class Consumer(Process):
#     def __init__(self,q,name):
#         super().__init__()
#         self.name=name
#         self.q=q
#     def run(self):
#         for i in range(10):
#             bz=self.q.get()
#             print(self.name+'消费'+bz)
# if __name__ == '__main__':
#     q=Queue(40)
#     p1=Producer(q,'张三')
#     p2=Producer(q,'李四')
#     c1=Consumer(q,'111')
#     c2=Consumer(q,'222')
#     c3=Consumer(q,'333')
#     p1.start()
#     p2.start()
#     p1.join()
#     c1.start()
#     c2.start()
#     c3.start()

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
#         p.apply(hs,(x,))
#     p.close()

# def hs(name):
#     for i in range(5):
#         print(name,i)
#         time.sleep(1)
# if __name__ == '__main__':
#     p=Pool(3)
#     a='abcde'
#     for x in a:
#         p.apply_async(hs,(x,))
#     p.close()
#     p.join()

from multiprocessing import  Pool
import time
# def zuoye(name):
#     print(name+'在写代码')
#     time.sleep(1)
#     return name+'写完代码了'
# def wan(status):
#     print('出去玩，'+status)
# if __name__ == '__main__':
#     p=Pool(1)
#     p.apply_async(zuoye,('张三',),callback=wan)
#     p.close()
#     p.join()

# 下载器
# def downLoad(movie):
#     for i in range(5):
#         print(movie,'下载进度%.2f%%'%((i+1)/5*100))
#         time.sleep(1)
#     return movie
# def alert(name):
#     print(name,'下载完毕，请收看')
# if __name__ == '__main__':
#     movies=['哪吒','金刚葫芦娃','黑猫警长','小青龙','亚洲飞鹰','A计划']
#     p=Pool(4)
#     for movie in movies:
#         p.apply_async(downLoad,(movie,),callback=alert)
#     p.close()
#     p.join()

'''
进程是资源分配的最小单位，线程是CPU调度的最小单位
线程--轻型进程
进程中的所有线程共享进程中的所有资源
'''
from threading import Thread
import time,os
# count=0
# def hs1():
#     global count
#     for i in range(100):
#         count+=1
#     print('函数1：',count)
# def hs2():
#     global count
#     for i in range(100):
#         count+=1
#     print('函数2：',count)
# if __name__ == '__main__':
#     t1=Thread(target=hs1)
#     t2=Thread(target=hs2)
#     t1.start()
#     t2.start()

# def sing():
#     for i in range(10):
#         print('唱歌%d'%(i+1))
#         time.sleep(1)
#     print(os.getpid())
# def dance():
#     for i in range(10):
#         print('跳舞%d'%(i+1))
#         time.sleep(1)
#     print(os.getpid())
# if __name__ == '__main__':
#     t1=Thread(target=sing)
#     t2=Thread(target=dance)
#     t1.start()
#     t2.start()

# def get(num):
#     for i in range(num):
#         print(i)
#         time.sleep(1)
# if __name__ == '__main__':
#     t1=Thread(target=get,args=(5,))
#     # 将当前线程设置为守护线程来守护主线程
#     # 需要在子线程开启之前设置
#     # 当主线程结束时，守护线程也就结束，不管是否执行完成
#     t1.setDaemon(True)
#     t1.start()
#     print('主线程结束了')

import threading
'''
threading.currentThread()--返回当前的线程变量
threading.enumerate()--返回一个包含正在运行的线程的列表
threading.active_count()--返回正在运行的线程的个数
threading.activeCount()--返回正在运行的线程的个数
与len(threading.enumerate())有相同的结果
'''
# def sing():
#     for i in range(10):
#         print('唱歌%d'%(i+1),threading.current_thread())
#         time.sleep(2)
# def dance():
#     for i in range(10):
#         print('跳舞%d' % (i + 1), threading.current_thread())
#         time.sleep(1.5)
# if __name__ == '__main__':
#     t1=Thread(target=sing,name='刘德华')
#     t2=Thread(target=dance,name='张惠妹')
#     t1.start()
#     t2.start()
#     print(threading.enumerate())
#     print(threading.active_count())
#     t1.join()
#     t2.join()
#     print('主进程结束')

'''
线程子类化
'''
# class T(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         for i in range(10):
#             print(self.name+'跳舞%d'%(i+1))
#             time.sleep(1)
#         print(os.getpid())
# class C(Thread):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         for i in range(10):
#             print(self.name+'唱歌%d'%(i+1))
#             time.sleep(1)
#         print(os.getpid())
# if __name__ == '__main__':
#     t=T('张三')
#     c=C('张三')
#     t.start()
#     c.start()

'''
共享全局变量
'''
# import threading
# g_num=10
# def hanshu1():
#     global g_num
#     g_num+=5
# def hanshu2():
#     print(g_num)
# if __name__ == '__main__':
#     t1=threading.Thread(target=hanshu1)
#     t2=threading.Thread(target=hanshu2)
#     t1.start()
#     t2.start()
# ------------------------------------------------------------------------------
# 作业题
# 多任务文件拷贝
# from multiprocessing import Pool,Manager
# import os
# def CopyFile(oldPath,newPath,fileName,queue):
#     fr=open(oldPath+'/'+fileName,'r')
#     fw=open(newPath+'/'+fileName,'w')
#
#     content=fr.read()
#     fw.write(content)
#
#     fr.close()
#     fr.close()
#     queue.put(fileName)
#
# def Main():
#     oldPath=input('please input folder path:')
#     newPath=oldPath+'-backups'
#     os.makedirs(newPath)
#     fileNames=os.listdir(oldPath)
#     pool=Pool(5)
#     queue=Manager().Queue()
#     for name in fileNames:
#         pool.apply_async(CopyFile,args=(oldPath,newPath,name,queue))
#     num=0
#     allNum=len(fileNames)
#     while num<allNum:
#         queue.get()
#         num+=1
#         copyRate=num/allNum
#         print('\r当前copy进度：%.2f%%'%(copyRate*100),end='')
#     print('\n已完成copy!')
# if __name__ == '__main__':
#     Main()