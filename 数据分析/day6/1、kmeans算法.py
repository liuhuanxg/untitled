import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#读取数据
data=pd.read_csv('company.csv',encoding='gbk')
print(data)

#数据----矩阵的方式
mat=data.as_matrix()  #返回的二元数组每一条就是一个数组
mat=mat[:,1:]
print(mat)   #只要后两列的数据


#聚类----K-means算法
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=3)   #聚类质心个数（分成几组就是几个）
result=kms.fit_predict(mat)  #计算聚类中心并预测每个样本的聚类指数
print('聚类后的结果：',result)


#由于聚类后的数据还是很抽象，所以需要将数据可视化进行分析
plt.figure()
#显示中文
plt.rcParams['font.sans-serif']='SimHei'
#显示-号
plt.rcParams['axes.unicode_minus']=False

#x，y标题
plt.xlabel('消费周期（天）：')
plt.ylabel('消费金额（元）：')


for i in  range(len(result)):
    y = data.iloc[i, 1]
    x = data.iloc[i, 2]

    if result[i]==0:
        plt.plot(x, y, '*r')
    elif result[i]==1:
        plt.plot(x, y, '*y')
    else:
        plt.plot(x, y, '*b')


plt.show()