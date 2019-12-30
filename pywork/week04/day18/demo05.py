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
def hanshu2():
    s=time.time()
    count=0
    for i in range(100000000):
        count+=1
    e=time.time()
    print(e-s)
if __name__ == '__main__':
    # t1=threading.Thread(target=hanshu1)
    # t1.start()
    t1=threading.Thread(target=hanshu2)
    t2=threading.Thread(target=hanshu2)
    t1.start()
    t2.start()
