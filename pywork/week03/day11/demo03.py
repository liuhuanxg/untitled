'''
__str__()方法,__repr__()方法
改变对象的字符串显示
是__str__()方法的备胎，如果找不到__str__()就会找它
%r和repr()默认调用__repr__()
%s和str()默认调用__str__()
'''
class Per():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '%s:%d'%(self.name,self.age)
    def __repr__(self):
        return '我叫{}，年龄{}'.format(self.name,self.age)
a=Per('张三',19)
print(a)
print(str(a))
print('%s'% a)
print('%r'% a)
print(repr(a))