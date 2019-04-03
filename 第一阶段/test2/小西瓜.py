# class Stu():
#     @property
#     def name(self):
#         print('调用此处')
#         return self._setname
#     @name.setter
#     def name(self,value):
#         if len(value)<3:
#             print('调用设置方法名字太短，不符合要求')
#             self._setname=value*2
#         else:
#             print('调用设置方法')
#             self._setname=value
# student=Stu()
# student.name='小花猫'
# print(student.name)
# x=Stu()
# student.name='12'
# print(student.name)

# for shuju  in range(100,1000):
#     gw=shuju%10
#     sw=shuju//10%10
#     bw=shuju//100
#     i=gw**3+sw**3+bw**3
#     if shuju ==i:
#         print(shuju)

# for x in range(5,10):
#     if x==9:
#         print (x)
#     else:
#         print (x,end=",")

a={'001':{'name':'张三','age':23,'num':'001'},
   '002':{'name':'李四','age':25,'num':'002'}
   }
class Oper():
    @staticmethod
    def writeData(a):
        with open('user.txt','w')as f:
            for key1,value1 in a.items():
                i=1
                for key2,value2 in value1.items():
                    f.write(key2)
                    f.write(':')
                    f.write(str(value2))
                    if i<3:
                        f.write(',')
                    else:
                        f.write('\n')
                    i+=1
    @staticmethod
    def readData(a):
        zd={}
        with open ('user.txt','r')as f:
            line=f.readline()
            while len(line)>0:
                con=line.split(',')
                xzd={}
                for kv in con:
                    x=kv.split(':')
                    if x[0]=='num':
                        num=x[1][0:-1]
                        xzd[x[0]]=num
                    elif x[0]=='age':
                        xzd[x[0]]=int(x[1])
                    else:
                        xzd[x[0]]=x[1]
                zd[num]=xzd
                line=f.readline()
        return zd
Oper.writeData(a)
b=Oper.readData(a)
print(b)
# class People():
#     tax=0.0
#     def __init__(self,name,age,work,salary,energy=100):
#         self.name=str(name)
#         self.age=int(age)
#         self.work=str(work)
#         self.salary=int(salary)
#         self.__energy=energy
#     def working(self):
#         People.tax+=self.salary*0.2
#         self.__energy-=30
#         if self.__energy<0:
#             self.__energy=0
#     def eat(self,money):
#         self.__energy+=10
#         self.salary-=money
#     def say(self):
#         print('自我介绍')
#     def sleep(self):
#         self.__energy+=60
#         if self.__energy>100:
#             self.__energy=100
#     def get_energy(self):
#         return  self.__energy
# class Woman(People):
#     def shoping(self,money):
#         self.salary-=money
#         print(self.salary)
# class Man(People):
#     def say(self):
#        super().say()
#        print('笑话')
# man=Man('宋泽萌',20,'IT',20000)
# man.say()
# women=Woman('刘梦琳',19,'IT',15000)
# women.shoping(3000)