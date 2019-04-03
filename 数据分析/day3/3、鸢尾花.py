import numpy as np


#整个花萼长度
data=np.loadtxt('iris_sepal_length.csv')
print('花萼长度表：',data)

#排序
data.sort()
print('排序：',data)

#去重
new_data=np.unique(data)
print('去重：',new_data)

#统计总长度
print('总长度：',np.sum(new_data))
print('均值：',np.mean(new_data))

print('标准差：',data.std())
print('方差：',data.var())

print('最大值：',new_data.max())
print('最小值：',new_data.min())