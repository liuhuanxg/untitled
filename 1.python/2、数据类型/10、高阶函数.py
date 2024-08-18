#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 10、高阶函数.py
@Time: 2020/5/24 16:39
@user：liuhuan   
"""

list1 = [1, 2, 3, 4, 5]

# 1、map函数，对list1列表集体进行某种操作
list2 = list(map(lambda x:x+3,list1))
print(list2)

# 2、filter函数，对list1列表进行筛选
list3 = list(filter(lambda x:True if x%2==0 else False,list1))
print(list3)


from functools import reduce
# 3、reduce函数,对数据进行累加操作
total = reduce(lambda x,y:x+y,list1)
print(total)


# 4、排序
list5 = [4, 9, 7, 5, 1]
list5.sort(reverse=True)
print(list5)

dict1 = {"python":50,"java":70,"c++":60}
result = sorted(dict1, key=lambda x:dict1[x])
print(result)

# 5、计数
list6 = [1, 2, 4, 5, 1, 1, 1]
print(list6.count(1))

# 6、求最大值
list7 = [1, 2, 4, -5, 1, 1, 1,-4]
print(max(list7))
print(max(list7,key=abs))
dict2 = {"python":50,"java":70,"c++":60}
print(max(dict2,key=lambda x:dict2[x]))

list8 = []
print(max(list8,default=1))

