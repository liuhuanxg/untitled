# Python 0715 吕佳
'''
脏数据
'''
import threading
# g_num=0
# def hs1():
#     global g_num
#     for i in range(1000000):
#         g_num+=1
#     print(g_num)
# def hs2():
#     global g_num
#     for i in range(1000000):
#         g_num+=1
#     print(g_num)
# if __name__ == '__main__':
#     t1=threading.Thread(target=hs1)
#     t2=threading.Thread(target=hs2)
#     t1.start()
#     t2.start()

# 可以通过线程同步来进行解决--互斥锁
# from threading import Thread,Lock
# g=0
# def hs1():
#     global g
#     for i in range(100000):
#         l.acquire()
#         g+=1
#         l.release()
#     print('函数1',g)
# def hs2():
#     global g
#     for i in range(100000):
#         l.acquire()
#         g+=1
#         l.release()
#     print('函数2',g)
# if __name__ == '__main__':
#     l=Lock()
#     t1=Thread(target=hs1)
#     t2=Thread(target=hs2)
#     t1.start()
#     t2.start()

# from threading import Thread,Lock
# g=0
# def hs1():
#     global g
#     l.acquire()
#     for i in range(100000):
#         g+=1
#     l.release()
#     print('函数1',g)
# def hs2():
#     global g
#     l.acquire()
#     for i in range(100000):
#         g+=1
#     l.release()
#     print('函数2',g)
# if __name__ == '__main__':
#     l=Lock()
#     t1=Thread(target=hs1)
#     t2=Thread(target=hs2)
#     t1.start()
#     t2.start()

'''
死锁
'''
# from threading import Thread,Lock
# import time
# g=0
# def hanshu1():
#     global g
#     for i in range(100000):
#         lock1.acquire()
#         print('函数1得到锁1，请求锁2')
#         time.sleep(1)
#         lock2.acquire()
#         print('111111111111111111111')
#         g+=1
#         lock2.release()
#         lock1.release()
#     print('函数1',g)
# def hanshu2():
#     global g
#     for i in range(100000):
#         lock2.acquire()
#         print('函数2得到锁2，请求锁1')
#         time.sleep(1)
#         lock1.acquire()
#         print('222222222222222222222')
#         g+=1
#         lock1.release()
#         lock2.release()
#     print('函数2',g)
# if __name__ == '__main__':
#     lock1=Lock()
#     lock2=Lock()
#     t1=Thread(target=hanshu1)
#     t2=Thread(target=hanshu2)
#     t1.start()
#     t2.start()

# from threading import Thread,Lock
# import time
# g=0
# def hanshu1():
#     global g
#     for i in range(5):
#         lock1.acquire()
#         print('函数1得到锁1，请求锁2')
#         time.sleep(1)
#         lock2.acquire()
#         print('111111111111111111111')
#         g+=1
#         lock2.release()
#         lock1.release()
#     print('函数1',g)
# def hanshu2():
#     global g
#     for i in range(5):
#         lock1.acquire()
#         print('函数2得到锁1，请求锁2')
#         time.sleep(1)
#         lock2.acquire()
#         print('222222222222222222222')
#         g+=1
#         lock2.release()
#         lock1.release()
#     print('函数2',g)
# if __name__ == '__main__':
#     lock1=Lock()
#     lock2=Lock()
#     t1=Thread(target=hanshu1)
#     t2=Thread(target=hanshu2)
#     t1.start()
#     t2.start()

'''
队列
'''
# import queue
# q=queue.Queue(3)
# q.put(10)
# q.put(20)
# q.put(30)
# print('------------',q.full())
# while q.qsize()>0:
#     print(q.get())
# print('结束')

'''
PriorityQueue--队列优先级
数字越小的优先级越高
'''
# import queue
# q=queue.PriorityQueue(3)
# q.put((2,'西瓜'))
# q.put((-1,'芒果'))
# q.put((3,'香蕉'))
# while not q.empty():
#     print(q.get())

'''
LifoQueue--后入先出队列
'''
# import queue
# q=queue.LifoQueue()
# q.put(10)
# q.put(20)
# q.put(30)
# q.put(40)
# while q.qsize()>0:
#     print(q.get())

# from threading import Thread
# import queue,time
# def producer(q,name):
#     count=1
#     while True:
#         bz=name+'生产包子%d'%count
#         print(bz)
#         q.put(bz)
#         time.sleep(1)
#         count+=1
# def consumer(q,name):
#     while True:
#         bz=q.get()
#         print(name+'吃'+bz)
# if __name__ == '__main__':
#     q=queue.Queue(5)
#     p1=Thread(target=producer,args=(q,'张三'))
#     p2=Thread(target=producer,args=(q,'李四'))
#     c1=Thread(target=consumer,args=(q,'111'))
#     c2 = Thread(target=consumer, args=(q, '222'))
#     c3 = Thread(target=consumer, args=(q, '333'))
#     p1.start()
#     p2.start()
#     c1.start()
#     c2.start()
#     c3.start()

# from threading import Thread
# import threading,time
# class A():
#     pass
# def hanshu1(name):
#     A.name=name
#     hanshu2()
# def hanshu2():
#     time.sleep(1)
#     print(threading.current_thread(),A.name)
# if __name__ == '__main__':
#     t1=Thread(target=hanshu1,args=('张三',),name='线程1')
#     t2=Thread(target=hanshu1,args=('李四',),name='线程2')
#     t1.start()
#     t2.start()

'''
使用threadLocal解决
使每个线程有自独有的局部变量，互不影响
'''
# from threading import Thread
# import threading,time
# local=threading.local()
# def hanshu1(name):
#     local.name=name
#     hanshu2()
# def hanshu2():
#     time.sleep(1)
#     print(threading.current_thread(),local.name)
# if __name__ == '__main__':
#     t1=Thread(target=hanshu1,args=('张三',),name='线程1')
#     t2=Thread(target=hanshu1,args=('李四',),name='线程2')
#     t1.start()
#     t2.start()

'''
全局解释器锁
'''
import threading,time
# def hanshu1():
#     s=time.time()
#     count=0
#     for i in range(200000000):
#         count+=1
#     e=time.time()
#     print(e-s)
# def hanshu2():
#     s=time.time()
#     count=0
#     for i in range(100000000):
#         count+=1
#     e=time.time()
#     print(e-s)
# if __name__ == '__main__':
#     # t1=threading.Thread(target=hanshu1)
#     # t1.start()
#     t1=threading.Thread(target=hanshu2)
#     t2 = threading.Thread(target=hanshu2)
#     t1.start()
#     t2.start()

# 协程
# def hanshu1():
#     for i in range(3):
#         print('函数1',i)
#         yield
# def hanshu2(a):
#     for i in range(3):
#         next(a)
#         print('函数2',i)
# h=hanshu1()
# hanshu2(h)

# 通讯
# import threading
# from socket import *
# udp_s=socket(AF_INET,SOCK_DGRAM)
# local_address=('10.10.107.240',9999)
# udp_s.bind(local_address)
# dest_address=('10.10.107.68',9999)
# def send():
#     while True:
#         data=input()
#         udp_s.sendto(data.encode('utf-8'),dest_address)
# def get():
#     while True:
#         s,addr=udp_s.recvfrom(124)
#         print(s.decode('utf-8'))
# if __name__ == '__main__':
#     t1=threading.Thread(target=send)
#     t2=threading.Thread(target=get)
#     t1.start()
#     t2.start()

# ------------------------------------------------------------------------------
# 作业题
# 协程应用
# import time
# import random
# import gevent
# from gevent import monkey
#
# monkey.patch_all()
#
# def peach(name):
#     for i in range(1,6):
#         start_time=time.time()
#         time.sleep(random.random())
#         end_time=time.time()
#         # 使用 round() 控制小数点位数!
#         print('%s产出第%s个桃子，耗时%s'%(name,i,round(end_time-start_time,2)))
#
# def apple(name):
#     for i in range(1,8):
#         start_time = time.time()
#         time.sleep(random.random())
#         end_time = time.time()
#         # 使用 round() 控制小数点位数!
#         print('%s产出第%s个苹果，耗时%s' % (name, i, round(end_time - start_time, 2)))
#
# if __name__ == '__main__':
#     gevent.joinall([
#         gevent.spawn(peach,'LI'),
#         gevent.spawn(apple,'HO'),
#     ])





