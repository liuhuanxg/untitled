# 输入一个年份，判断是否是闰年
# year=int(input('请输入一个年份：'))
# if (year%4==0 and year!=100) or year%400==0:
#     print(year,'是闰年')
# else:
#     print(year,'不是闰年')

'''
元组和列表的区别以及定义
区别：元组是不可修改的数据类型；列表是可以修改的数据类型
定义：
元组--不可修改的，以逗号分隔，用小括号括起来的有序序列
列表--可修改的，以逗号分隔，用中括号括起来的有序序列
'''

# 赋值，深拷贝，浅拷贝的区别
# import copy
# a=[1,2,3,[4,5],6]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# a.append(99)
# print(a)
# print(b)
# print(c)
# print(d)
#
# a[3].append(30)
# print(a)
# print(b)
# print(c)
# print(d)

# 列表倒序
# a=[1,2,3,4,5,6]
# i=0
# j=len(a)-1
# while i<j:
#     a[i],a[j]=a[j],a[i]
#     i+=1
#     j-=1
# print(a)