'''
继承：有两个类，A类和B类。当我们说A类继承B类时候，
那么A类就拥有了B类中所有的属性和方法
object类是所有类的父类，还可以称为基类或者超类

继承者称为子类，被继承者称为父类。
可以继承多个类

作用：1、简化了代码，减少冗余，
      2、提高了代码的健壮性，可以直接对父类进行修改。
      3、提高了代码的安全性。
      4、是多态的前提。

缺点：耦合与内聚是描述类与类之间的关系的，
内聚性（内在的功能多少）越高，耦合性（两者之间的联系）越低，代码越好，但是继承正好相反。
'''

#单继承的实现
'''
class Person(object):
    def __init__(self,name,age,money):
        self.name=name
        self.age=age
        self.__money=money
    def setMoney(self,money):
        self.__money=money
    def getMoney(self,money):
        return  self.__money
    def run(self):
        print('run')
    def eat(self,food):
        print('eat '+food)

class Student(Person):
     def __init__(self,name,age,__money,stuId):
         super(Student,self).__init__(name,age,__money)
        #属性必须全部继承，不能部分继承，如：name，age，__money,必须全部都有
         self.stuId=stuId
     
         
         
         
stu=Student('西瓜',15,123,123)
print(stu.name)
stu.eat('小豆芽')
print(stu.stuId)
'''

'''
子类可以有自己独有的属性如：stuId
私有属性不能继承。但是可以继承getMoney和setMoney方法。
可以有自己的独有方法。
'''


'''
多态：一种事物的多种形态。
最终目标：人可以喂任何一种动物。
'''
'''
class Cat(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name +' 吃')
class Mouse(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name +' 吃')
tom=Cat('Tom')
jerry=Mouse('jerry')

tom.eat()
jerry.eat()
'''
#思考：当有100中动物，也都有name属性和eat方法，怎么做？
#定义了一个有name属性和eat方法的Animal类，让所有动物都继承自Animal
'''
class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name +' 吃')

class Cat(Animal):
    def __init__(self,name):
       super(Cat,self).__init__(name)

class Mouse(Animal):
    def __init__(self,name):
        super(Mouse, self).__init__(name)
tom=Cat('Tom')
jerry=Mouse('jerry')

tom.eat()
jerry.eat()
'''

class Person(object):
    def feedCat(self,cat):
        print('给你食物')
        cat.eat()
    def feedMouse(self,mouse):
        print('给你食物')
        mouse.eat()
class Animal(object):
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name +' 吃')
class Cat(Animal):
    def __init__(self,name):
       super(Cat,self).__init__(name)

class Mouse(Animal):
    def __init__(self,name):
        super(Mouse, self).__init__(name)
tom=Cat('西瓜')
per=Person()
per.feedCat(tom)



