import numpy as np
arr=np.array([[4,3,1],[2,1,2]])
#只排序行，不对列进行排序
arr.sort()
'''
[[1 2 3]
 [1 2 4]]
'''
print(arr)

arr.sort(axis=0)
#对列也进行排序
'''
[[1 2 2]
 [1 3 4]]
'''
print(arr)

list1=[6,8,1,2,3,4]
#直接在原始数据进行更改，改变了物理结构
# new_list=list1.sort()   #[1, 2, 3, 4, 6, 8]
# print(list1)            #None
new_list=sorted(list1)
print(list1)                #[6, 8, 1, 2, 3, 4]
print(new_list)             #[1, 2, 3, 4, 6, 8]
