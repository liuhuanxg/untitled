'''
__hush__()方法--哈希/散列
将一个不定长的输入，通过哈希函数变换成一个定长的输出，即哈希值。
这种哈希变换是一种单向运算，具有不可逆性即不能根据哈希值还原出输入的信息。
set集合要求数据是可哈希（不可修改）的，因为set集合会默认调用对象的__hash__()函数进行快速查询，如果找到了则调用对象的__eq__()函数判断两个是否相同，如果相同则不添加。
在自定义类中，如果没有实现__eq__()和__hash__()，会继承object的__eq__()和__hash__()。如果只定义__eq__()方法，没有定义__hash__()，__hash__()方法会隐式设置为None。
hash()函数默认调用object类的__hash__()方法，Hash值是对象的id值的十六分之一。
'''
# a={'a','b',[1,2,3]}
# print(a)    # 报错 unhashable type: 'list'

# class Stu():
#     def __init__(self,name):
#         self.name=name
# a=Stu('张三')
# b=Stu('李四')
# c=Stu('张三')
# s={a,b,c}
# print(s)
# print(hash(a))
# print(id(a)/16)

# class Stu():
#     def __init__(self,name):
#         self.name=name
#     def __eq__(self, other):
#         print('self',self)
#         print("other",other)
#         print('222')
#         return self.name==other.name
#     def __hash__(self):
#         print('111')
#         print(self,hash(self.name))
#         return hash(self.name)
# a=Stu('张三')
# b=Stu('李四')
# c=Stu('张三')
# e=Stu('王五')
# print(a)
# print(b)
# print(c)
# print(e)
# d={a,b,c,a,a,e}
# print(d)