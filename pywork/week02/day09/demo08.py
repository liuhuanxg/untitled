class Teacher():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return '我叫{}，工资{}'.format(self.name,self.salary)
a=Teacher('张三',999999)
print(a)