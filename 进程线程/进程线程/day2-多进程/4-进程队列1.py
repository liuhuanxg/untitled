from multiprocessing import Queue, Process

q = Queue(3)  # 队列的长度   可以不写默认值
q.put("包子")
q.get()
q.put("香蕉")
q.put("西瓜")

print("执行到这了")

# q.get(block=False)与q.get_nowait("")作用等同
print(q.get(block=False))  # 可选参数block，默认为True，False时强取，取不出内容时报错

# q.put("",block=False)与q.put_nowait("")作用等同
q.put("猪肘子", block=False)  # 可选参数block，默认为True，False时强放，队列满时放不下会报错

print("开始吃")
print(q.qsize())
# while q.qsize()>0:
#     print(q.get())
# print(q.empty())
# print(q.full())
print(q.get_nowait())
print(q.get_nowait())  # 取不到时会报错
print(q.put_nowait("油条"))

q.close()  # 队列关闭之后不能再取，再取会报错
# print(q.join_thread())
