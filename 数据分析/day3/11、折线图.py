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

x=(values[:,1])
y=(values[:,2])


#绘制
plt.figure(figsize=(10,10))

plt.plot(x,y,color='r',linestyle='--',marker='o')



#由于X刻度太长，有些需要旋转显示
# plt.xticks(rotation=45)
ys=[]
yz=values[range(0,70,4),1]
for i in yz:
    ys.append(i[:5])
    # print(i[:5])
plt.xticks(range(0,70,4),ys,rotation=45)

plt.title('2000-2017年季度生产总值散点图')
plt.xlabel('年份')
plt.ylabel('生产总值(亿元)')
plt.savefig('报告2.png')
plt.show()