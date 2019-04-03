import numpy as np
#一、组合数组
#1、hstack()/vstack()
'''
arr1=np.arange(1,6,2)
arr2=np.arange(7,12,2)

#横向组合为一维数组
arr3=np.hstack((arr1,arr2))
print(arr3)
 #纵向组合
arr4=np.vstack((arr1,arr2))
print(arr4)
'''

#2、concatenate()函数
#横向：axis=1
#纵向：axis=0
arr1=np.array([[1,1],[2,2]])
arr2=np.array([[3,3],[4,4]])
arr3=np.concatenate((arr1,arr2),axis=1)
arr4=np.concatenate((arr1,arr2))
print(arr3)
print(arr4)


#二、切割
#split横向切割

arr6=np.array([[1,1,3,3],[2,2,4,4]])
print('arr6:',arr6)
print('~'*200)
arr6_sub=np.split(arr6,2)
print(arr6_sub)
print('~'*200)
arr6_sub=np.split(arr6,2,axis=1)
print(arr6_sub)

#纵向
print('~'*200)
arr6_sub=np.vsplit(arr6,2)
print(arr6_sub)
arr6_sub=np.split(arr6,2,axis=0)
print(type(arr6_sub))
print(type(arr6))
