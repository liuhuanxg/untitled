import time

list = [x for x in range(10**7)]
num = int(input('请输入一个数：'))
start_time=time.time()
for i in list:
    if i == num:
        end_time=time.time()
        print(end_time-start_time)
