from multiprocessing import  *
import time
def f_write(q):
    lists=['a','b','c','d','e','g','h']
    for i in lists:
        q.put(i)
    time.sleep(2)

def f_read(q):
    while True:
        if not q.empty():
            print(q.get())
        else:
            break
if __name__=='__main__':
    q=Queue(10)
    pw=Process(target=f_write,args=(q,))
    pw.start()
    pw.join()
    pr = Process(target=f_read, args=(q,))
    pr.start()
    pr.join()