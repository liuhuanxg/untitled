import matplotlib.pyplot as plt
import numpy as np

#数据
x=np.linspace(-1,1,50)
y1=2*x+1
y2=2*x-1

#定义画布
plt.figure()

#属性
plt.xticks([-1,0,1],[r'bad','normal','$good$'])

#使用plt.gca获取当前坐标轴信息
ax=plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')


#显示中文
plt.title('图2-1')
plt.rcParams['font.sans-serif']='SimHei'
#设置正常显示符号，解决保存图像的符号‘-’显示为方块的问题
plt.rcParams['axes.unicode_minus']=False


#绘制  自定义图例的名字，需要加 “,”
l1,=plt.plot(x,y1)
l2,=plt.plot(x,y2)

#绘制完成后添加
# plt.legend(['y=2*x+1'],loc='upper right')  #表示将图例添加到右上角
plt.legend(handles=[l1,l2],labels=['我的工资','她的工资'],loc='best')  #表示将图例添加到右上角

# plt.savefig('案例4.png')
#显示
plt.show()