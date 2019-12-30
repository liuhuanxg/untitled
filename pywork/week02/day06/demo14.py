'''
lambda--匿名函数
用来快捷定义一个小函数
不能包含循环、return，可以包含if...else...
表达式计算的结果直接返回
'''
# hs=lambda x,y:x+y
# b=hs(2,3)
# print(b)    # 5

# func=lambda :3<2
# print(func())    # False

# x=lambda a,b:a if a>b else b
# print(x(2,3))

# lst=[{'name':'Tom','age':19},{'name':'jerry','age':29},{'name':'mary','age':39}]
# getAge=lambda x:x['age']
# l=max(lst,key=getAge)
# print(l)

# hs=lambda x:x*x
# a=[1,2,3]
# b=map(hs,a)
# print(list(b))

# hs=lambda x:True if x%2==0 else False
# hs=lambda x:not x%2
# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(hs,a)
# print(list(b))

# hs=lambda x:True if x%3==0 or x%7==0 else False
# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(hs,a)
# print(list(b))

# a=[1,2,3]
# b=['a','b','c']
# hs=lambda x:{x[0]:x[1]}
# x=map(hs,zip(a,b))
# print(list(x))