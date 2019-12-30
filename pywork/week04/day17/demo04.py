'''
队列--先进先出
put()--向队列中存放数据，若已满，此方法将阻塞至有空间可用为止。
get()--返回队列中的一个项目，若列表为空，此方法将阻塞，直到队列中有项目可用为止。
qsize()--获取队列中的数据数量
full()--判断队列是否已满
empty()--判断队列是否已空
'''
from multiprocessing import Queue

# q=Queue(4)    # 4--队列容量，若超出，程序阻塞
# q.put('包子')
# q.put('香蕉')
# q.put('西瓜')
# print(q.full())
#
# while q.qsize()>0:
#     print(q.get())
# print(q.empty())