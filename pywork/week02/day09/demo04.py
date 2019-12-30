'''
__init__()在创建对象的时候自动执行
在__init__()中做初始化操作
'''
# class Student():
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def show(self):
#         print('我叫{}，年龄{}，性别{}'.format(self.name,self.age,self.sex))
# zs=Student('张三',18,'女')
# zs.show()
#
# ls=Student('李四',23,'男')
# ls.show()

# class Student():
#     def __init__(self,name):
#         self.name=name
#     def hehe(self,age):
#         self.age = age
#     def show(self):
#         print('我叫{}，年龄{}'.format(self.name,self.age))
# zs=Student('张三')
# zs.show()    # 报错

# class Student():
#     def __init__(self,name):
#         self.name=name
#     def hehe(self,age):
#         self.age = age
#     def show(self):
#         print('我叫{}，年龄{}'.format(self.name,self.age))
# zs=Student('张三')
# zs.hehe(19)
# zs.show()