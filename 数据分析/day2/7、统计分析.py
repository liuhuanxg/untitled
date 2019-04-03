import numpy as np

arr=np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]])
#以二进制保存，不用加后缀名
np.save('data',arr)

#读取，写上文件路径
# data=np.load('data.npy')
# print(data)

# np.savez() #可以将多个数组保存到一个文件当中去


#2、读取文本格式的数据(txt,csv)
#保存
np.savetxt('data.txt',arr,fmt='%d',delimiter=',')
#fmt:存储类型
#delimiter:以什么分割
#读取
# data=np.loadtxt('data.txt',int,delimiter=',')
# print(data)

#自定义存储类型
#读取jobs.txt文件数据，使用刚才定义的类型
new_type=np.dtype([('name',np.str_,40),('num',np.int32),('address',np.str_,40)])
data=np.loadtxt('jobs.txt',dtype=new_type,delimiter='，',encoding='utf-8')

print(data)
