'''
__del__()方法
销毁魔术方法：当一个对象在内存中被销毁的时候自动执行
至少有一个self，接收对象
程序自动调用此方法，不需要我们手动调用
'''
class A():
    num=0    # 类属性，也叫静态属性
    def __init__(self,name):
        A.num+=1    # 每定义一个对象，计数器加1
        self.name=name
    def __del__(self):
        A.num-=1
        print(self.name,'被删除，还剩下{}个对象'.format(A.num))
a=A('张三')
b=A('李四')
c=A('王五')
print(A.num)
del a    # 自动调用__del__()
del b
del c