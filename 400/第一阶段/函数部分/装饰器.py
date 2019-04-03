'''
概念：是一个闭包，把一个函数当做参数返回一个替代版的函数，本质上是一个返回函数的函数
'''

#简单的装饰器
'''
def outer(func):
    def inner():
        print('*******')
        func()
    return inner
# f是func1的加强版本

@outer
def func1():
    print('sunck is a good man')
func1()
'''


#复杂点的装饰器

'''
def outer(func):
    def inner(age):
        if age<0:
            age=-(age)
        func(age)
    return inner
@outer  #相当于  say=outer(say)
def say(age):
    print('xigua is %d years old'%age)

say(-10)
'''

a={'name':'Tom'}
def func1(func2):
    def inner(a):
        if a.get('name')=='Tom':
            return func2(a)
        else:
            return '不存在'
    return inner
@func1
def func(a):
    print(a)
    return '111111'
func(a)
