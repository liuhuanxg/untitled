'''
可变参数
'''
'''
'*'
1.'*'使参数变为了一个元组，所有传递的参数变为元组的元素
2.'*'具有打散序列的功能
'''
# 使参数变为了一个元组
# def kb(*a):
#     print(a)
#     # for x in a:
#     #     print(x)
# kb(1)    # (1,)
# kb(1,2,3,4)    # (1,2,3,4)
# kb()    # ()

# def kb2(*a):
#     print(a)
# x=(1,2,3)
# kb2(*x)    # (1, 2, 3)
# # 传递的参数变为元组的元素
# kb2(x)    # ((1, 2, 3),)

# 打散序列
# def func(a,b,c):
#     print(a,b,c)
# tup=(1,2,3)
# func(*tup)
# lst=[1,2,3]
# func(*lst)

'''
'**'
1.'**'使参数变成一个字典，所有传递的参数变为字典的键值对
!!!这里传参要求是键=值的形式
2.'**'有打散字典的功能，实参的key值必须与形参名相同，否则报错
3.'**kwargs'必须放在'*args'后面
'''
# def kb(**kwargs):
#     print(kwargs,type(kwargs))
# kb(name='张三',age=18)    # {'name': '张三', 'age': 18} <class 'dict'>
# kb(name='张三',age=18,sex='男')    # {'name': '张三', 'age': 18, 'sex': '男'} <class 'dict'>
# kb()    # {} <class 'dict'>

# def kb(name,age):
#     print(name,age)
# # 这里的key值必须与形参名相同，否则报错
# a={'name':'张三','age':18}
# kb(**a)

# 若写成def kb(**b,*a)，会报错
# def kb(*a,**b):
#     print(a,b)
# a={'name':'张三','age':18}
# kb(1,2,3,**a)    # (1, 2, 3) {'name': '张三', 'age': 18}
# kb(1,2,3,*a)    # (1, 2, 3, 'name', 'age') {}

'''
!!!总结：
定义函数时，参数的位置：位置参数，元组参数，默认参数，字典参数
'''
def kb(a,*b,c=9,**d):
    print('a=', a)
    print('b=', b)
    print('c=', c)
    print('d=', d)
kb(1,2,3,4,5)
'''
a= 1
b= (2, 3, 4, 5)
c= 9
d= {}
'''
kb(1,2,3,name='张三')
'''
a= 1
b= (2, 3)
c= 9
d= {'name': '张三'}
'''

# 也可执行，但最好别用
# def kb(a,b=9,*c,**d):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)
#     print('d=', d)
# kb(1,2,3,4)
# '''
# a= 1
# b= 2
# c= (3, 4)
# d= {}
# '''