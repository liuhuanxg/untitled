import  matplotlib.pyplot as plt

'''
input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)
#设置图表标题
plt.title('WenDuJi',fontsize=24)
#设置横坐标名字
plt.xlabel('TianQi',fontsize=14)
#设置纵坐标名字
plt.ylabel('WenDu',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
plt.show()
'''


#绘制一系列点
'''
x_value=[1,2,3,4,5]
y_value=[1,5,9,13,17]
plt.scatter(x_value,y_value,s=100)
plt.title('xigua',fontsize=24)
plt.show()
'''

#自动计算数据
'''
x_value=list(range(1,100))
y_value=[x*x  for x in x_value]
plt.scatter(x_value,y_value,c='red',edgecolors='none',s=40)
#向scatter传递参数c来设置颜色，还可以用元组来表示颜色(0,0,1)分别表示红绿蓝，值越接近0，颜色越深，越接近1，颜色越浅
plt.show()
'''
'''
def  huabiao(x,y):
    plt.scatter(x,y,s=40)
    plt.show()
x=list(input('请输入横坐标：'))
y=list(input('请输入纵坐标:'))
huabiao(x,y)
'''

#颜色映射
'''
x_value=list(range(1,100))
y_value=[x*x  for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=40)
#根据y坐标进行颜色渐变
plt.show()
'''
#保存图标
'''
x_value=list(range(1,100))
y_value=[x*x  for x in x_value]
plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,s=40)
plt.show()
plt.savefig('s.png',bbox_inches='tight')
#保存图标，第一个坐标是要保存的名字，第二个参数是清除空白区域
'''

'''
打印立方数
'''

'''
x=list(x for x in range(1,6))
y=[x**3 for x in x]
print(y)
plt.scatter(x,y,s=40)
plt.show()
'''
'''
x=list(x for x in range(1,5000))
y=[x**3 for x in x]
plt.scatter(x,y,c=y ,cmap=plt.cm.Greens,s=10)
plt.show()
'''
