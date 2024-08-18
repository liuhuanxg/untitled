print("-")
# 单进程执行
"""
from random import randint
from time import time, sleep
def download_task(filename):
    print("开始下载：%s ..." % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("%s 下载完成！耗费了%d秒" % (filename, time_to_download))


def main():
    start = time()
    download_task("python从入门到住院.pdf")
    download_task("Peking Hot.avi")
    end = time()
    print("总共耗费了%.2f。" % (end - start))  # 12
    
if __name__ == "__main__":
    main()
"""

# 多进程执行
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print("启动下载进程，进程号[{}].".format(getpid()))
    print("开始下载{}".format(filename))
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("{}下载完成！耗费了{}秒".format(filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=("Python从入门到住院.pdf",))
    p1.start()
    p2 = Process(target=download_task, args=('Peking.pdf',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("总共耗费了{}秒。".format(start - end))  # 8


if __name__ == "__main__":
    main()
