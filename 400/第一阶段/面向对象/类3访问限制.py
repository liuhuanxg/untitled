class Person(object):
    def __init__(self, name, age, weight, height,money):
        self.name=name
        self.age=age
        self.__weight__=weight
        self._height=height
        self.__money=money
    def setMoney(self,money):
        if money<0:
            money=0
        self.__money=money
    def getMoney(self):
        return self.__money



per4=Person('西瓜',22,177,72,6000)
print(per4.age)


'''
如果要让内部的属性不被外部直接访问，在属性前加两个下划线  __，
在python中如果属性前加两个下划线，那么这个属性就变成了私有属性
外部无法使用，只能在内部使用。此时内部存储名字已经改变为：_Person__money
而不是__money

通过内部的方法可以修改私有属性。set方法和get方法可以修改私有属性
通过自定义的方法实现对私有属性的赋值与取值。

print(per4.__money)       会出现标识错误。
 '''
per4.setMoney(10)
print(per4.getMoney())

#用这种方法也可以调用私有属性
per4._Person__money=1
print(per4.getMoney())

#在python中类似   __xx__  属于特殊变量，可以直接访问
print(per4.__weight__)

'''
在python中   _xxx  变量，这样的实例外边是可以访问的,
 但是，按照约定的规则，当我们看到这样的变量时，
 意思是“虽然我可以被访问，但是请把我视为私有变量，不要直接访问”
 例如上边的_height
'''
print(per4._height)
