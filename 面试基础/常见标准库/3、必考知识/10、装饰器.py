#装饰器：返回值是一个函数
#优点：在不修改原代码的基础上给函数增加新的功能


def func(func3):
    def inner(a):
        print('bbbbbbbbb')
        print('a:',a)
        func3(a)
    return inner
def func2(a):
    print(a)
c=func(func2)
c(3)


'''
def eat(fight):
    def inner(a):
        print('inner',a)
        fight(a)
    return inner
@eat
def fight(a):
    print('fight',a)
fight(3)
'''

def father(a):
    print('000000000000000')
    def inner1():
        print('111111')
        a()
        print('22222222')
    return inner1

def mother(b):
    print('ccccccccccccccccc')
    def inner2():
        print('aaaaaaaaaa')
        b()
        print('bbbbbbbb')
    return inner2

@father
@mother
def son():
    print('sonsonnnnnnnnnnnnnnn')
son()
#结果如下：
# 000000000000000
# ccccccccccccccccc
# aaaaaaaaaa
# 111111
# sonsonnnnnnnnnnnnnnn
# 22222222
# bbbbbbbb
