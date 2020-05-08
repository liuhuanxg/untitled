import abc
class Person(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass

    def breath(self):
        print("breath")

class Hero():
    def kungfu(self):
        print("功夫")
class Man(Person,Hero):
    # 抽象类必须复写所有的抽象方法，不管有没有调用
    # 只要有一个没有复写就会在实例化对象时报错
    def eat(self):
        print('人吃饭')

    def sleep(self):
        print("人睡觉")


list2=[23]
list3=sorted(list2)
m=Man()
m.kungfu()
# m.eat()