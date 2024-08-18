from multiprocessing import Process, Pool
import time


def hanshu(name):
    for i in range(5):
        print(name, i)
        time.sleep(1)


if __name__ == '__main__':
    p = Pool(3)
    a = "abcd"
    for x in a:
        # p.apply(hanshu, (x,))
        p.apply_async(hanshu, (x,))  # 阻塞，一次只跑一个进程

    p.close()
    p.join()  # 阻塞主进程，等待子进程结束
