'''
认识函数：在一个完整项目中，某些功能会反复的使用，那么会将功能封装成函数，
当我们要使用功能时直接调用函数即可

本质：函数是对功能的封装

优点：
1、简化代码结构，增加了代码的复用度（重复使用的程度）。
2、如果想修改某些功能，或者调试某个BUG，只需修改对应的函数即可。

'''
'''
定义函数：
格式：
def 函数名(参数1，参数2，···，参数n)
      语句
      return  表达式

def:      函数代码块以def关键字开始
函数名：  遵循标识符规则   
（）：    是参数列表的开始和结束
参数列表  (参数1，参数2，···，参数n)：任何传入函数的参数和变量必须放在圆括号之间，用逗号分隔。
 函数从函数的调用者那里获取的信息
：   函数内容（封装的功能）以冒号开始，并且缩进
语句：    函数封装的功能
return:   一般用于结束函数，并返回信息给函数的调用者
表达式：  即为要返回给函数的调用者的信息。
注意：     最后的return可以不写，相当于return  None
                                           
'''

'''
函数的调用
格式：函数名（参数列表）

函数名：是要使用的功能的函数函数名字
参数列表：函数的调用者给函数传递的信息，没有信息小括号也不能省略。
          参数按顺序传递，个数要对应
函数调用的的本质：实参给形参赋值的过程
'''

# 最简单函数，无参无返回值的函数
'''
def xigua():
    print('西瓜')
xigua()
'''

# 函数的参数
# 形参（形式参数）：定义函数时小括号中的变量，本质是变量。
'''
def s(str,age):
    print(str,age)
s(1234,18)
'''

# 实参(实际参数):调用函数时给函数传递的参数，本质是值


# 函数的返回值
'''
def mySum(sum1,sum2):
    #将结果返回给函数的调用者，执行完return语句之后函数结束，后边语句不再执行。
    return  sum1+sum2

print(mySum(1,2))
'''
'''
传递参数：
值传递:传递不可变类型（string、tuple、number是不可变的）
'''
# def func1(num):
#     num=10
#
# temp=20
# func1(temp)
# # 传递一个temp，temp值没有改变
# print(temp)
# print(func1(temp))

'''
引用传递：传递可变类型（list，dict、set是可变的）
'''
def func2(lis):
    lis[0]=100
li=[1,2,3,4]
func2(li)
print(li)


'''
5、关键字参数：允许函数调用时参数的顺序与定义时不一致

'''
# def myPrint(str,age):
#     print(str,age)
# myPrint(age=18,str='xc is a good girl')

'''
6、默认参数：调用函数时，如果没有传递参数，则使用默认参数
要用默认参数，最好将默认参数放在最后
'''
# def myPring(str,age=19,):
#     print(str,age)
# myPring('sfsf')

'''
7、不定长参数：能处理比定义时更多的参数
'''
# 加了*号的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是空元组
# def func(name,*args):
#     print(name)
#     for x in a:
#         print(x)
# func('sunck','asd','asd')

# def mySum(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(mySum(1,2,3,4))

# def func2(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# func2(x=1,y=2,name='张三')


# def func3(*args,**kwargs):
#     #这种类型可以存放任意参数
#     pass



'''
8、匿名函数：不适用def这样的语句定义函数，使用lambda来创建函数匿名函数

特点：
1、lambda只是一个表达式，函数体比def简单
2、lambda的主体只是一个表达式，而不是代码块。仅仅只能在lambda表达式中封装简单的逻辑
3、lambda函数有自己的命名空间，且不能访问自有参数列表之外的或全局命名空间里的参数
4、虽然lambda是一个表达式，而且看起来只能写一行，与C和C++内联函数不同。不是为了增加效率

格式：lambda 参数1，参数2，·····，参数n：expression（表达式）
'''
sum=lambda sum1,sum2:sum1+sum2
print(sum(1,2))
