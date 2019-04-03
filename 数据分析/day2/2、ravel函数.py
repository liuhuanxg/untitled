import numpy as np

#1、ravel函数
#是reshape函数的逆操作，并不是修改原来数组，而是创建了一个新数组
'''
a1=np.arange(10)
a2=a1.reshape(2,5)

print(a1)
print(a2)

a3=a2.ravel()
print('a3:',a3)  #[0 1 2 3 4 5 6 7 8 9]

# 2、flatten()函数
#说明：默认为横向展平,需要加“F”参数
a4=a2.flatten()
print('a4:',a4)  #[0 1 2 3 4 5 6 7 8 9]
a5=a2.flatten('F')
print('a5:',a5)   #[0 5 1 6 2 7 3 8 4 9]
'''
#ravle()和flatten()函数区别
#共同点：将多维数组降为一维数组
#区别：返回的拷贝还是视图
#flatten返回的是一份拷贝，对拷贝所作的修改不会影响原始数组
#ravel返回的是一个视图，对拷贝所作的修改会影响原始数组

# a1=np.array([[1,2],[3,4]])
# a2=a1.flatten()
# print('a1:',a1)
# print('a2:',a2)

a1=np.array([[1,2],[3,4]])
a2=a1.ravel()
print('a1:',a1)
print('a2:',a2)
a2[2]=100
print('a1:',a1)
print('a2:',a2)