from queue import Queue,PriorityQueue,LifoQueue
import time


q=Queue(3)  #正常队列，先进先出
q.put((1,"张三"))
q.put((-1,"李四"))
q.put(3)
k=q.qsize()
for i in range(k):
    print(q.get(),k)

p=PriorityQueue()   #可添加顺序
p.put((1,"包子"))
p.put((0,"西瓜"))
p.put((-7,"玉米"))
k=p.qsize()
for i in range(k):
    print(p.get(),k)

l=LifoQueue()   #栈   后进先出
l.put(1)
l.put(2)
k=l.qsize()
for i in range(k):
    print(l.get(),k)
