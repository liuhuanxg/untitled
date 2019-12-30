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
#     c2=Thread(target=consumer,args=(q,'222'))
#     c3=Thread(target=consumer,args=(q,'333'))
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
#     print(A.name)
#     hanshu2()
# def hanshu2():
#     time.sleep(1)
#     print(threading.current_thread(),A.name)
# if __name__ == '__main__':
#     t1=Thread(target=hanshu1,args=('张三',),name='线程帅哥')
#     t2=Thread(target=hanshu1,args=('李四',),name='线程美女')
#     t1.start()
#     t2.start()

'''
使用threadLocal解决
使每个线程有自己独有的局部变量，互不影响。
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
#     t1=Thread(target=hanshu1,args=('张三',),name='线程帅哥')
#     t2=Thread(target=hanshu1,args=('李四',),name='线程美女')
#     t1.start()
#     t2.start()