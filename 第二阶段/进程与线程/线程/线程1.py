from threading import  Thread


def son_thread(num):
    print('第%d条线程已经创建'%num)

if __name__=='__main__':
    #创建多条线程
    for i in range(10):
        #创建线程的同时等同于实例化Thread类
        #内置两个参数，第一个参数是一个函数，函数是线程体
        #第二个参数是一个元组   元组内是第一个参数（函数）的实参列表
        t=Thread(target=son_thread,args=(i+1,))
        t.start()
    print("game over")