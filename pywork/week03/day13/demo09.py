'''
观察者模式
'''
class Boss():
    def __init__(self):
        self.observers=[]
        self.status=''
    # 绑定观察者
    def attach(self,ob):
        self.observers.append(ob)
    # 通知观察者
    def notify(self):
        for ob in self.observers:
            ob.update()
class Employee():
    def __init__(self,name,boss):
        self.name=name
        self.boss=boss    # 绑定通知者
    def update(self):
        print('{}，{}赶快工作'.format(self.boss.status,self.name))
if __name__=='__main__':
    ljc=Boss()
    # 互相绑定
    zs=Employee('张三',ljc)
    ls=Employee('李四',ljc)
    ljc.attach(zs)
    ljc.attach(ls)

    ljc.status='李嘉诚回来了'
    ljc.notify()