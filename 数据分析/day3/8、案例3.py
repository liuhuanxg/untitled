import matplotlib.pyplot as plt
import numpy as np


#创建画布f   宽*dpi，高*dpi
f=plt.figure(figsize=(8,6),dpi=80)

#2行1列的画布
f.add_subplot(2,1,1)

#数据集
x=np.arange(0,1.1,0.01)
y1=x**2
y2=x**4

#设置属性
plt.title('数据函数')
plt.rcParams['font.sans-serif']='SimHei'
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,1)
plt.ylim(0,1)

#绘制
plt.plot(x,y1)
plt.plot(x,y2)

#必须先绘制完成，才设置图例
plt.legend(['y=x^2','y=x^4'])

f.add_subplot(2,1,2)
plt.title('数据函数')
x=np.arange(0,2*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1,color='black',linewidth=3.0,linestyle='--',marker='p')
plt.plot(x,y2)

plt.xlim(0,2*np.pi)
plt.ylim(-1,1)

plt.xticks([0,np.pi/2,np.pi,np.pi*3/2,2*np.pi])
plt.legend(['y=sinx','y=cosx'])

#保存画布
plt.savefig('案例3.png')

#展示
plt.show()