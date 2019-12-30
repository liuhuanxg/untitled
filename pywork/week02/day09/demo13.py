'''
类属性和实例属性
'''
class People():
    tax=0.01
    def __init__(self,salary):
        self.salary=salary
    def pay(self):
        return self.salary*People.tax
a=People(10000)
b=People(20000)
print(a.pay())
print(b.pay())
People.tax=0.02
print(a.pay())
print(b.pay())
print(id(a.tax))
print(id(People.tax))
a.tax=0.07
print(People.tax)