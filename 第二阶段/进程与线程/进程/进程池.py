from multiprocessing import  Process,Pool
import  os
import  time
def son_process(i):
    print("这是我创建的第%d个子进程，进程的ID是%d"%(i,os.getpid()))
    time.sleep(1)
if __name__=='__main__':
    p=Pool(3)
    #创建进程池
    for i in range(10):
        p.apply_async(son_process,(i+1,))
        #异步创建子进程，直接执行进程池里的全部进程。（异步进程应用比较多）
        # p.apply(son_process)
        #同步创建子进程，
    p.close()
    p.join()