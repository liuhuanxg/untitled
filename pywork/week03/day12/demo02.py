'''
迭代器的应用场景
'''
# 1.数据类型转换
# str1='hello'
# lst1=list(str1)
# print(lst1)
#
# tuple1=('a','b','c')
# lst2=list(tuple1)
# print(lst2)

# 2.斐波那契序列
class Fib():
    def __init__(self,num):
        self.num=num
        self.a=1
        self.b=1
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.num:
            print(self.a)
            self.a,self.b=self.b,self.a+self.b
            self.current+=1
        else:
            raise StopIteration
for x in Fib(10):
    pass