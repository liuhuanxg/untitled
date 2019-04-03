from greenlet import  *
import time
def test1():
    while True:
        print('====a====')
        g2.switch()
        time.sleep(1)
        print('====c====')
def test2():
    while True:
        print('====b====')
        g1.switch()
        time.sleep(1)
        print('====d====')
g1=greenlet(test1)
g2=greenlet(test2)
g2.switch()


'''
def test1():
    while True:
        print('====a====')
        yield   #将a挂起
        time.sleep(1)
        print('====c====')
def test2(c):
    while True:
        print('====b====')
        next(c)     #此时直接执行输出c语句
        time.sleep(1)
        print('====d====')

a=test1()
test2(a)
'''


'''
def test1():
    while True:
        print('====a====')
        time.sleep(1)
        print('====c====')
        test2()
def test2():
    while True:
        print('====b====')
        time.sleep(1)
        print('====d====')
        test1()
test1()

'''