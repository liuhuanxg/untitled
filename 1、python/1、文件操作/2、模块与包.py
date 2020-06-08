import datetime
#判断一个日期是这一年的第几天

def dayofyear():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    return (date1-date2).days+1
if __name__ == '__main__':
    print(dayofyear())

#打乱一个排好序的对象：
import random
alist=[1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)

"""
import copy
list1 = [1, [5, 6, [7,8]]]
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)
list1[0]=0
print(list1, list2)
list1[1][0]=0
print(list1, list2)
print(list3,list1)
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lst2 = list(map(lambda x:x**2,lst))
print(lst2)

lst3 = list(filter(lambda x:x%2==0,lst))
print(lst3)
from functools import reduce


def func(x,y):
    return x+y
lst4 = reduce(func,[],0)
print(lst4)


lst2 = [3, 7, 9, 5, 4, 10]
lst2.sort()
print(lst2)

lst3 = [3, 7, 9, 5, 4, 10]
lst4 = sorted(lst3)
print(lst4)