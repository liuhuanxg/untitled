'''
在类的外部增加属性（不推荐使用）
'''
class Teacher():
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name,self.age)
zs=Teacher('张三')
zs.age=29
zs.show()

ls=Teacher('李四')
ls.show()    # 报错