'''
random模块
random()--产生大于0且小于1之间的小数
uniform(a,b)--产生指定范围内的随机小数
randint(a,b)--产生范围内的随机整数，包含头和尾
randrange(s,e,[step])--产生范围内的随机整数，左闭右开
choice(lst)--参数为列表，随机返回序列中的一个数据
shuffle()--打乱列表顺序，直接修改原列表
'''
import random
# print(random.random())
# print(random.uniform(2,3))

# a=[random.randint(1,10) for i in range(10)]
# print(a)

# a=random.randrange(1,13,2)
# print(a)
# a=[random.randrange(1,10,3) for i in range(10)]
# print(a)

# a=[10,20,30,40]
# b=random.choice(a)
# print(b)

# a=[10,20,30,40]
# random.shuffle(a)
# print(a)