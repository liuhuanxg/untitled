import numpy as np

#一维数组
'''
arr=np.arange(10)
print(arr)
print(arr[5])
print(arr[1:7])
arr[2:4]=100,101
print(arr)
print(arr[1:-1:2])  #不包含最后一个数

print(arr[5:1:-2])
'''

#二维数组。逗号之前是行，逗号之后是列
arr=np.array([[1,2,3,4,5],[4,5,6,7,8],[7,8,9,10,11]])
print(arr[0,3:5])   #取出第一行下标为3,4的列
print(arr[1:,2:])   #取出第2,3行下标从2开始
print(arr[:,2])
#第0行的第1个，第1行的第2个，第2行的第3个
print(arr[(0,1,2),(1,2,3)])
