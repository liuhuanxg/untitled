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
plt.figure(figsize=(6,4))

exp=[0.1,0.01,0.1]   #一般用于分离各个数据
labels=['第一产业','第二产业','第三产业']

plt.pie(y,explode=exp,labels=labels,autopct='%1.1f%%')

plt.title('各产业比例。')
# plt.savefig('报告4.png')
plt.show()