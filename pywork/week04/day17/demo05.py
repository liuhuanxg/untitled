'''
block=False--不等待，直接抛出异常
'''
from multiprocessing import Queue
# q=Queue(3)
# q.put(10)
# q.put(20)
# q.put(30)
# try:
#     q.put(40,block=False)    # 不等待，直接抛出异常
# except:
#     print('队列已满，无法再存放数据')
# print('结束')

a=Queue(3)
a.put(10)
a.put(20)
print(a.get())
print(a.get())
try:
    print(a.get(block=False))
except:
    print('队列已空，取不出东西了')
print('结束')