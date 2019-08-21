from random import randint
from time import time,sleep
from threading import Thread


class DownloadTask(Thread):

    def __init__(self,filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print("开始下载{}".format(self._filename))
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("{}下载完成，耗费了{}秒".format(self._filename,time_to_download))

def main():
    start = time()
    t1 = DownloadTask("Python从入门到住院.pdf")
    t1.start()
    t2=DownloadTask("Peking Hot.avi")
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print("总共耗费了{}秒".format(end - start))
if __name__  == "__main__":
    main()