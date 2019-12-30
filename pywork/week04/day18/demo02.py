'''
死锁
'''
from threading import Thread,Lock
import time
# g=0
# def hs1():
#     global g
#     for i in range(100000):
#         lock1.acquire()
#         print('函数1得到锁1，请求锁2')
#         time.sleep(1)
#         lock2.acquire()
#         print('11111111111111111111')
#         g+=1
#         lock2.release()
#         lock1.release()
#     print('函数1：',g)
# def hs2():
#     global g
#     for i in range(100000):
#         lock2.acquire()
#         print('函数2得到锁2，请求锁1')
#         time.sleep(1)
#         lock1.acquire()
#         print('22222222222222222222')
#         g += 1
#         lock1.release()
#         lock2.release()
#     print('函数2：',g)
# if __name__ == '__main__':
#     lock1=Lock()
#     lock2=Lock()
#     t1=Thread(target=hs1)
#     t2=Thread(target=hs2)
#     t1.start()
#     t2.start()

# 不会死锁
# g=0
# def hs1():
#     global g
#     for i in range(5):
#         lock1.acquire()
#         print('函数1得到锁1，请求锁2')
#         time.sleep(1)
#         lock2.acquire()
#         print('11111111111111111111')
#         g+=1
#         lock2.release()
#         lock1.release()
#     print('函数1：',g)
# def hs2():
#     global g
#     for i in range(5):
#         lock1.acquire()
#         print('函数2得到锁1，请求锁2')
#         time.sleep(1)
#         lock2.acquire()
#         print('22222222222222222222')
#         g += 1
#         lock2.release()
#         lock1.release()
#     print('函数2：',g)
# if __name__ == '__main__':
#     lock1=Lock()
#     lock2=Lock()
#     t1=Thread(target=hs1)
#     t2=Thread(target=hs2)
#     t1.start()
#     t2.start()