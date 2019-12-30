'''
形如：__变量名--私有变量
'''
class Girl():
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)
zs=Girl('张三',18)
zs.show()
print(zs.name)
print(zs.__age)    #  报错 'Girl' object has no attribute '__age'