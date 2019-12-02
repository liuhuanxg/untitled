from threading import Thread, Lock

g_num = 0


def hs1():
    global g_num

    for i in range(100000):
        t = Lock()
        t.acquire()
        g_num += 1
        t.release()
    print("hs1" + str(g_num))


def hs2():
    t = Lock()
    t.acquire()
    global g_num
    for i in range(100000):
        g_num += 1
    t.release()
    print("hs2" + str(g_num))


if __name__ == '__main__':
    t1 = Thread(target=hs1)
    t2 = Thread(target=hs2)

    t1.start()
    t2.start()
