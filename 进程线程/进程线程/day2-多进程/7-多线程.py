from threading import Thread

count = 0


def hanshu1():
    global count
    for i in range(10):
        count += 1


def hanshu2():
    global count
    for i in range(10):
        count += 1


if __name__ == '__main__':
    t1 = Thread(target=hanshu1)
    t2 = Thread(target=hanshu2)
    t1.start()
    print(count)
    t2.start()
    print(count)
