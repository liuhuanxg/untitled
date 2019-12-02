from time import time
import threading
def func():
    start = time()
    count = 0
    for i in range(100000000):
        count += 1
    end = time()
    print(end-start)
if __name__ == '__main__':
    t1=threading.Thread(target=func)
    t2=threading.Thread(target=func)
    t1.start()
    t2.start()
#21.96125602722168