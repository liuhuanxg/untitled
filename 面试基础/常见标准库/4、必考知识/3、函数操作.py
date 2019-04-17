# 必选参数–>默认参数–>可变参数–>命名关键字参数–>关键字参数

#必选参数：形参必须传值
def bit(n):
    print('n:',n)
bit(9)

# m为默认参数
def fight(m=18):
    print('m:',m)  #10，传参时为所传参数，不传参时为默认参数
fight(10)


#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kwargs):
    print('name:',name,'age:',age,'orthers:',kwargs)
    print(kwargs['wuwu'])
person('张三',19,cc='3',wuwu='cc')


#可变参数       *args接收的参数为元组   是可变参数类型，接收不定长参数
def total(a=5,*args,**kwargs):
    print('a:',a)
    print('args:',args)
    print('kwargs:',kwargs)
total(19,22,23,24,23,name='张三',age=19)
# a: 19
# args: (22, 23, 24, 23)
# kwargs: {'name': '张三', 'age': 19}

#命名关键字参数   在可变参数的后边    没可变参数时需要加*，
def eat(fruit,food,*args,milk):
    print(fruit)
    print(food)
    print(args)
    print(milk)
eat('西瓜','鸡蛋',11,23,24,milk='蒙牛')

def sleep(*,hour):
    print(hour)
sleep(hour=9)