class People():
    tax=0.01
    def __init__(self,salary):
        self.salary=salary
    def pay(self):
        return self.salary*People.tax
a=People(10000)
b=People(20000)

# 只要有=，就是一个新开辟的变量了，与类变量无关了
# a.tax=a.tax+1 混合使用，前面的tax是对象属性，后边的那个是类属性
a.tax+=0.01
print(a.tax,id(a.tax))
print(People.tax,id(People.tax))

# 类变量变了，他也不变
People.tax=200
print(a.tax)    # 0.02

# 删除a的属性，就使用类的
delattr(a,'tax')
print(a.tax)    # 200