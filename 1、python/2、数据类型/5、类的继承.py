
import time

def outer(func):
    def inner():
        start = time.time()
        re = func()
        end = time.time()
        runtime=start-end
        print(runtime)
        return re
    return inner
@outer
def fun():
    for i in range(10000000):
        i+=1
    return 'ok'
print(fun())

from math import pi
class Circle():
    def __init__(self,r):
        self.r = r

    def Area(self):
        area=self.r**2*pi
        return area

    def Perimeter(self):
        perimeter=self.r*2*pi
        return perimeter

    def __str__(self):
        area=self.Area()
        perimeter=self.Perimeter()
        return "圆的半径是{}m，周长是{}m，面积是{}m2".format(self.r,area,perimeter)

c=Circle(5)
print(c)

a = ["师范", "理工", "综合", "理工", "综合", "综合", "农林", "综合", "综合","理工"]
a=set(a)
print(a)

nums = [11, 22,11,33,11,44, 55,11]
for i in range(len(nums)):
    if nums[i]==11:
        nums[i]=10
print(nums)