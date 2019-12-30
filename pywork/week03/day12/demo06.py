'''
生成器表达式
'''
# b=(i for i in range(5))
# print(b)
# for x in b:
#     print(x)

# a=('鸡蛋%d个'%(i+1) for i in range(10))
# print(a)
# next记录了当前的状态
# print(next(a))
# print(a.__next__())
# print(list(a))    # 从第三个开始

'''
生成器作用：
可以实现多任务（协程-->模式并发）
'''