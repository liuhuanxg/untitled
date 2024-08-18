# from multiprocessing import Process
# from os import getppid,getpid
# from time import sleep
#
# class SubProcess(Process):   #进程子类化
#     def __init__(self,x):
#         super(SubProcess, self).__init__()
#         self.x = x
#
#     def run(self) -> None:   #重写run函数，覆盖父类的run方法，进程启动时调用此方法
#         for i in range(self.x):
#             print("启动进程",i,getppid(),getpid())
#             sleep(1)
#
# def main():
#     p = SubProcess(3)
#     p.start()
#     p1 = SubProcess(3)
#     p1.start()
#
# if __name__ == "__main__":
#     main()

count = 0


def func():
    global count
    count += 1


func()
print(count)
