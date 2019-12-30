'''
__str__()函数--打印对象名称时默认调用__str__()方法，默认返回的是对象的内存地址
可重写__str__()打印对象保存的信息
'''
class Dog():
    def __init__(self,color,age):
        self.color=color
        self.age=age
    def __str__(self):
        return '颜色%s 年龄%d'%(self.color,self.age)
d=Dog('黄色',4)
print(d)

b=d
print(b,type(b))