'''
脏数据
'''
# import threading
# g_num=0
# def hs1():
#     global g_num
#     for i in range(1000000):
#         g_num+=1
#     print(g_num)
# def hs2():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
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
#     for i in range(1000000):
#         l.acquire()    # 锁定
#         g+=1
#         l.release()    # 释放
#     print('函数1：',g)
# def hs2():
#     global g
#     for i in range(1000000):
#         l.acquire()
#         g += 1
#         l.release()
#     print('函数2：',g)
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
#     print('函数1：',g)
#     l.release()
# def hs2():
#     global g
#     l.acquire()
#     for i in range(100000):
#         g += 1
#     print('函数2：',g)
#     l.release()
# if __name__ == '__main__':
#     l=Lock()
#     t1=Thread(target=hs1)
#     t2=Thread(target=hs2)
#     t1.start()
#     t2.start()