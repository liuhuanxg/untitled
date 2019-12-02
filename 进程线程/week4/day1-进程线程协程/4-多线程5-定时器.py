from threading import Thread,Timer
import time
import timer
print(time.time())
def func(a):
    print(a)
timer1 = Timer(1,func,[2])
timer1.start()
print(time.time())
