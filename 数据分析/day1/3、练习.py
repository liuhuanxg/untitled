import numpy as np
a=np.arange(15)
print(a,type(a))


a1=np.arange(15).reshape(3,5)
print(a1)


#生成符合正态分布的随机数，必须大样本量
# r3=np.random.randn(1000)
# import matplotlib.pyplot as mp
# mp.hist(r3)
# mp.show()

# np.random.randint(a,b)  #用于生成一个指定范围内的整数,值域[a,b]

r4=np.random.randint(2,10,size=(2,5))
print(r4)


