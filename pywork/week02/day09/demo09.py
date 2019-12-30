from math import pi
class Circle():
    def __init__(self,radis):
        self.radis=radis
    def area(self):
        return pi*self.radis*self.radis
    def c(self):
        return 2*pi*self.radis
    def __str__(self):
        return '我的半径是%d,周长为%.2f,面积为%.2f'%(self.radis,self.area(),self.c())
a=Circle(5)
print(a)