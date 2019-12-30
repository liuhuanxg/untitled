'''
变量作用域：
Local（函数内部）
Enclosing（嵌套函数的外层函数内部）
Global（模块全局）
Built-in（内建）
'''
'''
命名空间查找顺序
（1）先在local中搜索
（2）然后在父函数的命名空间enclosing中搜索
（3）接着在模块命名空间global中搜索
（4）最后在内置命名空间built-in搜索
'''
# a=3
# b=30
# c=300
# def out():
#     a=4
#     b=40
#     def inside():
#         a=5
#         print(a)#L  local 优先使用本地的
#         print(b)#E  enclosing 本地没有找嵌套作用域
#         print(c)#G  globle 本地嵌套都没有，找全局
#         print(__name__)#B built-in 全局也没有，找内置
#     inside()
# out()