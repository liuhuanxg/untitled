class Girl():
    def __init__(self):
        pass
    def setAge(self,age):
        if age<0 or age>95:
            print('错误')
            self.age=0
        else:
            self.age=age
    def getAge(self):
        return self.age
zs=Girl()
zs.setAge(20)
print(zs.getAge())    # 20

# 可通过对象添加属性将之前的值进行覆盖
# 解决办法：使用私有属性
zs.age=-9
print(zs.getAge())    # -9

zs.setAge(200)
print(zs.getAge())    # 0