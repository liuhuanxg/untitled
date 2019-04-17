import random
print(random.random()) #随机生成0-1之间的数字
print(random.uniform(1,10))  #随机生成1-10之间的数字（包括小数跟整数）
print(random.randint(1,10))   #生成1-10之间的整数
print(random.randrange(1,10,2))  #生成1-10之间 步长为2的数字 所以只会生成奇数
list=[1,4,5,5,6,7,8]
print(random.choice(list))  #从list中随机抽取
print(random.sample(list,2))  #从list中随机抽取2个元素的片段