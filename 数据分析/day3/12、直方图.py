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

# 数据
x=range(3)
y=values[-1,3:6]

#绘制
plt.figure()

#由于X刻度太长，有些需要旋转显示
# plt.xticks(rotation=45)
ys=[]
yz=values[range(0,70,4),1]
for i in yz:
    ys.append(i[:5])
    # print(i[:5])



plt.title('2017年第一季度各产业生产总值直方图')

plt.ylabel('生产总值(亿元)')

plt.bar(x,y,width=0.1)
labels=['第一产业','第二产业','第三产业']
plt.xticks(range(3),labels)

plt.savefig('报告3.png')
plt.show()