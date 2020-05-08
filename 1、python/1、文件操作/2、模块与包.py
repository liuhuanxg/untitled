import datetime
#判断一个日期是这一年的第几天
"""
def dayofyear():
    year = input("请输入年份: ")
    month = input("请输入月份: ")
    day = input("请输入天: ")
    date1 = datetime.date(year=int(year),month=int(month),day=int(day))
    date2 = datetime.date(year=int(year),month=1,day=1)
    return (date1-date2).days+1
if __name__ == '__main__':
    print(dayofyear())
"""
#打乱一个排好序的对象：
import random
alist=[1,2,3,4,5]
random.shuffle(alist)
print(alist)