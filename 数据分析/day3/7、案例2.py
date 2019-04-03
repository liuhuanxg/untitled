#同一画布下画两条线

import matplotlib.pyplot as plt
import numpy as np

#数据集
x=np.arange(0,1.1,0.01)
y1=x**2
y2=x**4
#创建画布
plt.figure()

#设置属性
plt.title('line')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,1)
plt.ylim(0,1)

#绘制
plt.plot(x,y1)
plt.plot(x,y2)

#必须先绘制完成，才设置图例
plt.legend(['y=x^2','y=x^4'])

#展示
plt.show()
