#numpy维度叫
import numpy as np
arrl=np.array([1,2,3])
#1、数组当中的秩是多少
print('arr1秩为：',arrl.ndim)   #一维数组秩为1，二维数组秩为2

#2、数据的轴为多少
print('arr1轴为：',arrl.shape)    #(3,)

#例2：
arr2=np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(arr2)
print('arr2秩为：',arr2.ndim)  #2

#2、数据的轴为多少
print('arr2轴为：',arr2.shape)          #(3,4)
print('size为：',arr2.size)             #(3*4)
print('元素类型：',arr2.dtype)           #(int(32))
print('每个元素大小：',arr2.itemsize)    #(4)
print('缓冲区：',arr2.data)              #内存地址