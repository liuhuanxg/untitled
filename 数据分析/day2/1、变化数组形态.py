import numpy as np
arr1=np.array([1,2,3,4,5,6])
print(arr1,arr1.shape)

arr2=arr1.reshape(2,3)
print(arr2,arr2.shape)

arr3=arr1.reshape(6,1)
print(arr3,arr3.shape)

z=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(z.shape)
new_z=z.reshape(-1)
print(new_z)


# big_array=np.arange(10000).reshape(100,100)
# print(big_array)
# #如果数组太大，在输出时，numpy自动省略中间部分，而只打印两边内容
# #如果要强制显示，需要禁用numpy这种行为，并强制打印整个数据，在打印之前在设置
# np.set_printoptions(threshold=np.NaN)
# print(big_array)