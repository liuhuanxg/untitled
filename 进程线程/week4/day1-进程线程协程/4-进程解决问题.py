from  time import time


#单进程计算 1-100000000 的和
"""
def main():
    total = 0
    number_list = [x for x in range(1,100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print("Excution time:{}".format(end - start))  #13.115750074386597

if __name__ == '__main__':
    main()
"""

from  multiprocessing import Process,Queue
from random import randint

def task_handler(curr_list,result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1,100000001)]
    result_queue = Queue()
    index = 0
    #启动8个进程将数据切片后进行计算
    for _ in range(8):
        p = Process(target=task_handler,args=(number_list[index:index + 1250000],result_queue))
        index += 12500000
        processes.append(p)
        p.start()

    #开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    #合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)  #443750005000000
    end = time()
    print("Execution time:",end - start)
if __name__ == '__main__':
    main()
