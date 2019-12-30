'''
队列
'''
# import queue
# q=queue.Queue(3)
# q.put(10)
# q.put(20)
# q.put(30)
# print('-------',q.full())
# while q.qsize()>0:
#     print(q.get())
# print('结束')

'''
PriorityQueue--队列优先级
数字越小的优先级越高
'''
# import queue
# q=queue.PriorityQueue(3)
# q.put((2,'西瓜'))
# q.put((-1,'芒果'))
# q.put((3,'香蕉'))
# while not q.empty():
#     print(q.get())

'''
LifoQueue--后入先出队列
'''
# import queue
# q=queue.LifoQueue()
# q.put(10)
# q.put(20)
# q.put(30)
# q.put(40)
# while q.qsize()>0:
#     print(q.get())