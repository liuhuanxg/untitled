'''
__new__()方法--实例化方法
在实例化对象时自动触发
至少有一个cls参数接收当前类，返回一个对象实例
先触发__new__才会触发__init__
'''
class Stu():
    # 实例化
    def __new__(cls, *args, **kwargs):
        print('111111111111111111111')
        # 如果不写这句，就没有创建对象，只打印111，不打印222。调用父类的__nuw__()方法就可以创建对象了。
        return object.__new__(cls)
    # 初始化
    def __init__(self,name,age):
        print('222222222222222222222')
        self.name=name
        self.age=age
zs=Stu('张三',19)
print(zs.name)