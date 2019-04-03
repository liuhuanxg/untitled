import matplotlib.pyplot as plt
import numpy as np

#创建画布
plt.figure(facecolor='skyblue',edgecolor='red')  #默认是空白画布

x=np.linspace(-1,1,50)
y=2*x+1
print('x:',x)
print('y:',y)

#参数设置
#标题
plt.title('y=2*x+1')
#X轴
plt.xlabel('X')
#Y轴
plt.ylabel('Y')

#绘制
plt.plot(x,y)
plt.show()
