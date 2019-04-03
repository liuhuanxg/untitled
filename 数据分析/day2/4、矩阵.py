#矩阵与通用函数
import numpy as np

#一、创建矩阵
#1、mat()函数
A=np.mat('1 0 0 0;0 1 0 1;0 0 1 0;0 0 0 1')
print(A)
B=np.mat([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print(B)

#2、matrix()函数
C=np.matrix('1 0 0 0;0 1 0 1;0 0 1 0;0 0 0 1')
print('C:',C)
D=np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print('D:',D)

#3、bmat()函数
#通过分块矩阵创建大矩阵
ABCD=np.bmat('A B;C D')
# print(ABCD)

print('~'*200)
#矩阵运算
#1、矩阵与数相乘：matrl*3
A=np.matrix('1 2;3 4')
B=A*3
print(B)
#2、加减运算
# arr1=np.ones((2,2),int)
# A=5*np.matrix(arr1)
# print(A)
# A=np.matrix('5 5;5 5')
# B=np.matrix('2 2;2 2')
# C=A-B
# D=A+B
# print('C:',C)
# print('D:',D)


print('~'*200)
#矩阵相乘
A=np.mat('1 0 0 0;0 1 0 0;-1 2 1 0;1 1 0 1')
B=np.mat('1 0 1 0;-1 2 0 0;1 0 4 0;-1 -1 2 1')
C=A*B
print(C)

#矩阵特有的属性
print('转置：',C.T)
print('共轭：',C.H)
print('逆矩阵：',C.I)
print('视图：',C.A)