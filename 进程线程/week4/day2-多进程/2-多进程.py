from multiprocessing import Process

count = 0


def hanshu():
    global count
    for i in range(1000):
        count += 1
    print("函数1：", count)


def hanshu2():
    global count
    for i in range(1000):
        count += 1
    print("函数2：", count)


if __name__ == '__main__':
    t1 = Process(target=hanshu)
    t2 = Process(target=hanshu2)
    t1.start()
    t2.start()
    # t1.join()
    # t2.join()
    print(count)
