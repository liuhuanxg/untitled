import matplotlib.pyplot as plt
import numpy as np

#显示中文
plt.rcParams['font.sans-serif']='SimHei'
#显示-号
plt.rcParams['axes.unicode_minus']=False
#内容太大时，强制显示所有内容，不省略
np.set_printoptions(threshold=np.NaN)

#读取数据,二进制
data=np.load('国民经济核算季度数据.npz')
print(type(data))
for i in data:
    print(i)
name=data['columns']
values=data['values']
# print(name)
# print(values)
# 数据
x=range(9)
y=values[0,6:]

print(x)
print(y)
#绘制
plt.figure()


plt.title('2000年第一季度各产业生产总值直方图')

plt.ylabel('生产总值(亿元)')

plt.bar(x,y,width=0.1)
labels=['农业','工业','建筑业','批发','交通运输','餐饮','金融','房地产','其他行业']
plt.xticks(range(9),labels)

# plt.savefig('报告3.png')
plt.show()
