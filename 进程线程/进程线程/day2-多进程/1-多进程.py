from multiprocessing import Process
import time


def sing():
    for i in range(10):
        print("我在唱第{}句歌词。".format(i + 1))
        time.sleep(1)


def dance():
    for i in range(10):
        print("我在跳第{}支舞。".format(i + 1))
        time.sleep(1)


if __name__ == '__main__':
    t1 = Process(target=sing)
    t2 = Process(target=dance)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

