'''
is与==的区别
is比较两个对象的id值是否相等，是否指向同一个内存地址。
==比较的是两个对象的内容是否相等，默认调用对象的__eq__()方法。
继承自object的__eq__方法比较两个对象的id。
对于自定义对象一般认为对象的值相同就同一个对象，因此需要重写__eq__()方法。
'''
# a=[1,2,3]
# b=[1,2,3]
# print(a==b)
# print(a is b)

class Stu():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __eq__(self, other):    # equal
        return self.__dict__==other.__dict__
a=Stu('张三',19)
b=Stu('张三',19)
c=Stu('李四',20)
# __eq__()不注释时
# print(a==b)    # True
# print(a is b)    # False

# __eq__()注释时
# print(a==b)    # False

d=[]
d.append(a)
if b not in d:    # 去调用了__eq__()，发现a==b，所以列表中只有一个对象。说明这里的in是根据==判断的。
    d.append(b)
print(d)