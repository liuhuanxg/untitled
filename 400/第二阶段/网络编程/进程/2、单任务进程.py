
from time import  sleep
def run():
    while True:
        print('sunck is a good man ')
        sleep(1.2)
if __name__=='__main__':
    while True:
        print('sunck is a nice man ')
        sleep(1)
        #并不会执行到run()方法
    run()