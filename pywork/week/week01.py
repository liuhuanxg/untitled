# week01
# day01~day04

# day01
'''
数据类型六大类：数字、字符串、列表、字典、集合、元组
其中数字又分为：整型、浮点型、布尔类型、复数
'''
# 复数--complex
# a=complex(2,3)
# print(a,type(a))    # (2+3j) <class 'complex'>

'''
类型转换
'''
# 有时是不可逆的
# a=3
# b=bool(a)
# print(b,type(b))    # True <class 'bool'>
# c=int(b)
# print(c,type(c))    # 1 <class 'int'>

# 输入的为整型，运行成功
# 输入的为浮点型，则提示出错
# price=input('请输入西红柿单价：')
# a=int(price)
# print(a,type(a))
#解决--先转float再转int，不管输入int还是float类型都不会出错
# price=int(float(input('请输入西红柿单价：')))
# print(price,type(price))

'''
10进制-->其他进制：
16：hex()
8：oct()
2：bin()
!!!使用上述函数转换的结果，皆为字符串类型
'''
# 8进制转16进制：
# a=hex(0o42)
# print(a,type(a))

'''
其他进制-->10进制
形如 int('...',...)
!!!第一个参数，必须是字符串类型，第二个参数int类型
'''
# 例子
# a=int('11',8)
# print(a)
# b=int('11',16)
# print(b)
# c=int('11',2)
# print(c)

'''
输出关键字列表
'''
# import keyword
# print(keyword.kwlist)

'''
chr()--根据ASCII码，将一个整数转换为对应的字符
'''
# a=int(input('请输入一个整数：'))
# print(chr(a))

'''
ord()--根据ASCII码，将一个字符转换为对应的的整数
'''
# 输入一个大写字母，判断这个大写字母是字母表中第几个字母
# a=input('请输入一个大写字母：')
# print(ord(a)-65+1)

'''
'//'--向下取整
!!!若两个运算数中有一个小数，则结果为小数
'''
# a=-9.5
# b=3
# c=a//b
# print(c)
# a=10
# b=3
# c=a//b
# print(c)

'''
'**'--幂
'''
# a=5
# print(5**2)
# print(5**3)

'''
'%'--取余
!!!同'//',有一为浮点，结果为浮点
'''
# b=5%3.0
# print(b)

'''
题
'''
# 1.三位数字倒置
# 2.任意位数数字倒置

'''
'/'--除号
!!!结果永远为浮点型
'''
# a=4
# a+=5
# print(a)    #9
# a-=5
# print(a)    #4
# a*=2
# print(a)    #8
# a/=2
# print(a)    #4.0
# a%=5
# print(a)    #4.0
# a//=2
# print(a)    #2.0
# a**=3
# print(a)    #8.0

'''
eval(str)--用来计算在字符串中的有效 python 表达式,并返回一个对象
'''
# a='1+2'
# print(a)
# b=eval(a)
# print(b)

'''
题
'''
# 1.输出50以内所有的偶数
# 2.砍价，抹去小数和个位数

# ------------------------------------------------------------------------------
# day02
'''
单分支
'''
# salary=int(input("请输入你的工资："))
# if salary>=10000 and salary<20000:
#     print('买辆迈腾')
# if salary>=20000 and salary<30000:
#     print('速腾')
# if salary>=30000:
#     print('买辆A6')
# if salary<=3000:
#     print('电动72 35v 50迈，续航：90')

'''
双分支
'''
# score=int(input("请输入四级成绩："))
# if score<425:
#     print("下次加油")
# else:
#     print("恭喜获得四级证书")
# print("结束")

'''
多层分支
'''
# score=int(input("请输入学习成绩："))
# if score>=90 and score<=100:
#     print("优秀")
# elif score>=80:
#     print("良好")
# elif score>=70:
#     print("一般")
# elif score>=60:
#     print("及格")
# else:
#     print("不及格")
# print('结束')

'''
若改为下面这样，会对90-100的成绩产生影响
!!!因为两个if之间没有任何关系，不受影响
'''
# score=int(input("请输入学习成绩："))
# if score>=90 and score<=100:
#     print("优秀")
# if score>=80 and score<90:
#     print("良好")
# elif score>=70 and score<80:
#     print("一般")
# elif score>=60 and score<70:
#     print("及格")
# else:
#     print("不及格")
# print('结束')

'''
连续比较
'''
# char=input('请输入一个字符：')
# n=ord(char)
# if 65 <= n <=90:
#     print('这是一个大写字母')
# elif 97 <= n <= 122:
#     print('这是一个小写字母')
# elif '0' <= char <= '9':
#     print('这是一个数字')
# elif n == 95:
#     print('这是一个下划线')
# else:
#     print('其他字符')

'''
嵌套判断
'''
# price=float(input('请输入西红柿单价：'))
# num=float(input('请输入购买数量：'))
# total=price*num
# if total>=50:
#     level=input('请输入vip级别：')
#     if level == '1':
#         total *= 0.8
#         print('享受总金额打八折优惠，金额为：%.2f' % total)
#     elif level == '2':
#         total=int(total)
#         total=total-total%10
#         print('享受抹零优惠，金额为：%d' % total)
#     elif level == '3':
#         print('享受去小数优惠，金额为：%d' % total)
# else:
#     sex=input('请输入性别:')
#     if sex == '男':
#         print('赠送玩具劳斯莱斯一个')
#     elif sex == '女':
#         print('赠送小猫一只')

'''
while循环
!!!循环三大件：
    1.初始值
    2.控制条件
    3.步长
'''
# money = int(input('请输入金额：'))
# while money >= 10:
#     print('吃一块西瓜')
#     money -= 10
#     print('剩余', money, '元')

'''
题
'''
# 1.求1-10的和
# 2.求6--2之间的所有整数的乘积
# 3.输入十个数，计算这十个数的和
# 4.求1--100之间所有偶数的和
# 5.1-2+3-4...+99
# 方法1
# n = 1
# sum = 0
# while n < 100:
#     if n % 2 == 0:
#         sum -= n
#     else:
#         sum += n
#     n += 1
# print(sum)
# 方法2
# n=1
# s=0
# while n<100:
#     s+=n*(-1)**(n-1)
#     n+=1
# print(s)
# 6.输入五个数，求最大值

'''
break--中断循环
continue--退出本次循环，进入下一次循环
'''
# 输入十个数
# 如果输入的<18,不参加运算
# 如果输入的>65，跳出循环
# 求输入的年龄的平均值
# i=1
# n=0
# sum=0
# while i<=10:
#     age=int(input('请输入年龄：'))
#     if age<18:
#         i+=1
#         continue
#     elif age>65:
#         break
#     else:
#         sum+=age
#         i+=1
#         n+=1
# if n==0:
#     print('无有效数据！')
# else:
#     print("平均值为：",(sum//n))

# ------------------------------------------------------------------------------
# day03
'''
for循环
range--前闭后开
'''
# range(5)--> [0,5)
# for i in range(5):
#     print(i)

'''
列表
!!!有序，可修改
'''
# []--空列表
# 遍历
# a=[1,'a','b','c']
# i=0
# while i<len(a):
#     print('第',i+1,'个值为：',a[i])
#     i+=1

# a=[1,'a','b','c']
# for i in range(len(a)):
#     print('第', i, '个值为：', a[i])

'''
'+'--拼接
!!!不去重
'*'--重复
'''
# a = [1, 2,3]
# b = [3, 4, 5]
# c = a + b
# print(c)
# d = a * 3
# print(d)

'''
切片
!!!同range，前闭后开
'''
# a=[10,20,30,40,50,60,70]
# b=a[2:5]
# print(b)
# a=['a','b','c',1,2,3,4,5]
# b=a[2:7:2]
# print(b)
# b=a[2:]
# print(b)
# b=a[:3]
# print(b)
# print(a)

'''
python支持负索引
最后一个值索引为-1，向前越来越小
'''
# 使用负索引逆向输出
# a=['a','b','c']
# for i in range(-1,-len(a)-1,-1):
#     print(i,':',a[i])

'''
使用'*'可进行可变赋值
'''
# a,b=[1,2]
# print('a:',a)
# print('b:',b)
# a,*b=[1,2,3,4]
# print('a:',a)
# print('b:',b)
# *a,b=[1,2,3,4,5]
# print('a:',a)
# print('b:',b)

'''
添加
append()--追加，在末尾，不去重
extend()--扩展，功能与'+'差不多，区别在于extend()会改变原列表的值
insert()--插入，在指定索引处插入指定元素
'''
# a=[1,2,3,4]
# a.append(4)
# a.append(9)
# print(a)
# a.extend('b')
# print(a)
# a.insert(2,'a')
# print(a)

'''
删除
pop()--可无参数也可有参数，无参默认弹出最后一个，有参数时弹出指定索引处的元素
remove()--有参，参数是想要删掉的那个值，删掉从左往右的第一个
del--可删除列表中的一个元素，也可删除整个列表
'''
# a=[1,2,3,4]
# b=a.pop()
# print(b)
# b=a.pop(1)
# print(b)
# print(a)

# a=[1,2,3,4,3,7,6]
# a.remove(3)
# print(a)

# a=[1,2,3,4,5,6,7]
# del a[2]
# print(a)
# del a

'''
修改
reverse()--将列表倒置
sort()--默认升序排列
    reverse=True--表示降序
    key=str.lower--表示按照小写进行比较
'''
# a=[3,1,2,4,3,6,7]
# a.reverse()
# print(a)
# a=[3,1,2,4,3,6,7]
# a.sort(reverse=True)
# print(a)

# a=['ab','Ab','Bc']
# a.sort()
# print(a)     #['Ab', 'Bc', 'ab']
# key=str.lower -- 按照小写进行比较
# a=['ab','Ab','Bc']
# a.sort(key=str.lower)
# print(a)     #['ab', 'Ab', 'Bc']

'''
查找
count()--参数为元素值，统计列表中该元素值的个数
index()--参数为元素值，从左到右查找，返回第一次出现的位置的索引值
'''
# a=[1,2,3,4,1,1,3,4]
# x=a.index(4)
# print(x)
# x=a.index(4,4,7)    # 该范围内没有，左闭右开
# print(x)    # 报错

'''
深浅拷贝预备知识
is和'=='的区别：
is判断的是这两个对象是不是就是一个，是通过id来判断的
'=='判断的是两个对象的值是否相同，是通过value来判断的
'''
# # 同
# a=[1,2,3]
# b=a
# a.append(4)
# print(a,id(a))
# print(b,id(b))
# # 不同
# a=[1,2,3]
# b=[1,2,3]
# print(a,id(a))
# print(b,id(b))
# # 不同
# a=3
# b=a
# a=5
# print(a,id(a))
# print(b,id(b))
# # 同
# a='abc'
# b='abc'
# print(a,id(a))
# print(b,id(b))

'''
赋值、深拷贝、浅拷贝
赋值--两对象指向同一地址空间，变化完全一致
浅拷贝--仅拷贝最外一层，所以原列表最外层变化时，它并不改变；但内层再改变就会跟着改变
深拷贝--从内到外全部拷贝，原列表的变化与它无关
'''
# import copy
# a=[1,2,3,[4,5,[10,20]],6]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# print(d,id(d))
#
# a.append(7)
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# print(d,id(d))
#
# a[3].append(99)
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# print(d,id(d))

'''
元组
!!!有序，不可修改
但元组内部的可变数据类型可以修改
'''
# 不可修改
# a=(1,2,3,4)
# print(a,type(a))
# a[0]=9    # 报错

# 元组不可修改；元组中可修改类型的数据，可修改
# a=(1,2,3,[4,5])
# a[0]=9       #报错
# a[3].append(99)
# print(a)     #(1, 2, 3, [4, 5, 99])

# 遍历
# a=(1,2,3,4)
# for x in a:
#     print(x)

'''
切片
'''
# a=(1,2,3,4)
# print(a[2: :1])

'''
'+'--拼接，不去重
'*'--重复
'''
# a=(1,2,3)
# b=(3,4)
# print(a+b)
# print(a*2)

'''
'*'可变赋值
'''
# a,b,c=(1,2,3)
# print(a)
# print(b,c)
#
# a,*b=(1,2,3,4,5)
# print(a)
# print(b)    # !!!b会变为列表类型

'''
强制类型转换
tuple()--转换为元组
list()--转换为列表
'''
# a=[1,2,3]
# b=tuple(a)
# print(type(b))
# c=list(b)
# print(type(c))

'''
在元组中，最重要的就是','号
'''
# a=(1)
# print(type(a))    # <class 'int'>
# a=(1,)
# print(type(a))    # <class 'tuple'>
# a=1,2
# print(a,type(a))    # (1, 2) <class 'tuple'>

'''
查找
index()--用法同列表，参数为元素值，从左到右查找，返回第一次出现的位置的索引值
count()--用法同列表，参数为元素值，统计列表中该元素值的个数
enumerate(a)--枚举,返回值为一个元组，(索引，对应值)
'''
# a=(1,2,3,3,4)
# print(a,type(a))
# # print(a.index(4,0,3))    # 报错，该范围内没有，范围左开右闭
# print(a.count(3))

# a=(11,12,13,'a')
# for x in enumerate(a):
#     print(x)

'''
元组题
'''
# 1.求元组a=(1,2,3,4,5,6,7,8,9,10,14)中是7的倍数或以7结尾的数的个数
# 2.求元组a=(1,2,3,4,5,6,7,8,9,10,14)中奇数个数和偶数个数
# 3.求出元组中的最大最小值和最大最小值对应的索引

'''
列表题
'''
# 1.两个列表big=[1,2,3,3,2,5]，small=[11,22,8,7,5,9]对应项相加，并给一个新列表
# 2.利用死循环和列表写传送站
# import time
# a=[1,2,3,4,5,6]
# while True:
#     t = a[0]
#     i = 0
#     while i < len(a) - 1:
#         a[i] = a[i + 1]
#         i += 1
#     a[i] = t
#     time.sleep(1)
#     print(a)
# 3.将列表倒置，即手动完成reverse()函数的功能
# 4.a=[1,2,3,4,1,2,5,1,1,2]，b=[1,2]，求a列表中b列表的个数

# ------------------------------------------------------------------------------
# day04
# 补充知识点
'''
逻辑运算符：and  or  not
'''
# stu=True
# if not stu:
#     print('你不是学生')
# else:
#     print('是学生，可以进学校')

'''
短路逻辑
x or y
若x成立，返回True
若x不成立，返回y的值

x and y
若x成立，返回y的值
若x不成立，返回False
'''
# a=5
# b=a>7 or 4
# print(b)    # 4
# a=5
# b=a>3 or 7
# print(b)    # True
#
# a=6
# b=a>7 and 5
# print(b)    # False
# a=6
# b=a>3 and 5
# print(b)    # 5

'''
三元表达式
满足if条件，值为前面的值
不满足则为后面的值
'''
# b=11
# a=7 if b>10 else 8
# print(a)
# b=9
# a=7 if b>10 else 8
# print(a)

'''
while/for...else...
'''
# i=1
# while i<5:
#     print(i)
#     i+=1
# else:
#     print('好像不成立了')

# 应用--判断是否为质数
# n=int(input('请输入一个数：'))
# i=2
# while i<n//2:
#     if n%i==0:
#         print(n,'不是质数')
#         break
#     i+=1
# else:
#     print(n,'是质数')

# 2-100质数放入列表
# s=[]
# for n in range(2,101):
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             break
#     else:
#         s.append(n)
# print(s)

'''
嵌套循环题
'''
# 1.输出一个由'*'组成的5*5矩阵
# 2.输出一个由'*'组成的正三角
# 3.输出一个由'*'组成的倒三角
# 4.9*9乘法表
# 5.输出一个由'*'组成的5*5空心矩阵

'''
字典--键值对
!!!无序，可修改
!!!key必须是不可修改的数据类型
'''
a={'name':'张三','age':19,'sex':'男'}

'''
添加
形如a['score']=99--不存在，添加；存在，覆盖
setdefault()--不存在，添加；存在，不操作
'''
# a={'name':'张三','age':19,'sex':'男'}
# print(a)
# print(a['name'])
# a['score']=99
# print(a)
# a['age']=18
# print(a)

# a={'name':'张三','age':19,'sex':'男'}
# a.setdefault('age',67)
# print(a)
# a.setdefault('score',90)
# print(a)

'''
删除
pop()--弹出指定键对应的值
!!!返回值为value，不同于列表，必须有参数，参数为key
popitem()--随机弹出一个键值对，随机是因为字典无序
!!!返回值为一个键值对元组
clear()--清空
del--可删除字典中的一个键值对，也可用于删除整个字典
'''
# a={'name':'张三','age':19,'sex':'男'}
# b=a.pop('name')
# print(b)
# print(a)

# a={'name':'张三','age':19,'sex':'男'}
# b=a.popitem()
# print(b)
# print(a)

# a={'name':'张三','age':19,'sex':'男'}
# a.clear()
# print(a)    # {}

# a={'name':'张三','age':19,'sex':'男'}
# del a['name']
# print(a)
# del a

'''
查找
keys()--返回所有的key，列表类型
values()--返回所有value，列表类型
items()--返回所有键值对，元组类型
len()--返回键值对的对数
get()--以键取值，若指定键不存在，默认返回None，可指定返回值
'''
# a={'name':'张三','age':19,'sex':'男'}
# print(a.keys())    # dict_keys(['name', 'age', 'sex'])

# a={'name':'张三','age':19,'sex':'男'}
# print(a.values())    # dict_values(['张三', 19, '男'])

# a={'name':'张三','age':19,'sex':'男'}
# print(a.items())    # dict_items([('name', '张三'), ('age', 19), ('sex', '男')])

# a={'name':'张三','age':19,'sex':'男'}
# print(len(a))    # 3

# info={'name':'张三','age':19,'sex':'男'}
# name=info.get('name')
# print(name)    # 张三
# a=info.get('a')
# print(a)    # None
# a=info.get('a','不存在')
# print(a)    # 不存在

'''
修改
update()--以字典形式更新指定的字典内容
!!!若键不存在，创建；若存在，覆盖
'''
# a={'name':'张三','age':19,'sex':'男'}
# b={'name':'李四','score':89}
# a.update(b)
# print(a)    # {'name': '李四', 'age': 19, 'sex': '男', 'score': 89}

'''
字典常见操作
in a/not in a--判断指定的key是否在字典当中
!!!是key！与value无关！
想要判断value是否存在可用in a.values()/not in a.values()
'''
# a={'name':'张三','age':19,'sex':'男'}
# if 'name' in a:
#     print('有姓名')
# if 'score' not in a:
#     print('没有成绩')
# if '张三' in a:    # 不成立
#     print('张三在里面')
# if 19 in a.values():    # 成立
#     print('有人19岁')

'''
初始化时，键重复，后面的会覆盖前面的
'''
# a={'name':'张三','age':19,'sex':'男','age':99}
# print(a)    # {'name': '张三', 'age': 99, 'sex': '男'}

'''
题
'''
# 1.
a={
    '001':{'name':'张三','age':18,'sex':'男'},
    '002':{'name':'李四','age':28,'sex':'男'},
    '003':{'name':'王五','age':38,'sex':'女'},
    '004':{'name':'赵四','age':48,'sex':'男'},
}
# （1）以num:001,name=张三,age:18,sex:男格式打印
# 方法1
# for x,y in a.items():
#     print('num:%s'%x,end=' ')
#     for k,v in y.items():
#         print('%s:%s'%(k,v),end=' ')
#     print()
# 方法2
# for k1 in a.keys():
#     print('num:%s'%k1,end=' ')
#     for k2 in a[k1].keys():
#         print('%s:%s' % (k2, a[k1][k2]), end=' ')
#     print()
# （2）给所有性别为男的添加1000元工资
# for k,v in a.items():
#     if v['sex']=='男':
#         v['salary']=1000
#     print(k,':',v)

'''
集合
!!!无序，唯一，可修改
'''
# 唯一
# a={1,2,3,3,3,3,3}
# print(a)    # 自动去重，{1, 2, 3}
# 无序
# a={1,2,3,3,3,3,3}
# print(a[1])    # 报错，不支持索引，无序

'''
定义空集合，只能用set(),只能！！
{}代表的是空字典，不可用
'''

'''
添加
add()--添加，重复不操作
update()--添加，参数可以是各种类型
'''
# a={1,2,3,3,3,3,3}
# print(a)    # {1,2,3}
# a.add(9)
# print(a)    # {1,2,3,9}
# a.add(9)
# print(a)

'''
set()--类型转换
'''
# 类型转换
# a=[1,2,3]
# b=set(a)
# print(b)    # {1, 2, 3}
# 类型转换
# a='1234'
# b=set(a)
# print(b)    # {'2', '1', '4', '3'}，顺序不定
# b={'name':'张三','age':19}
# a=set(b)
# print(a)    # {'age', 'name'},只有key没有value

'''
集合的顺序遍历
'''
# a={1,2,3,4}
# for x in a:
#     print(x)

'''
删除
pop()--随机弹出一个，无参，不可加参数
remove()--移除指定值
clear()--清空
del--删除整个集合，此处不可用于删除集合中的某个元素
'''
# a={1,2,3,4}
# b=a.pop()
# print(b)
# print(a)

# a={10,20,30,40}
# a.remove(20)
# print(a)

# a={10,20,30,40}
# a.clear()
# print(a)    # set()

# a={1,2,3,4}
# del a
# print(a)    # 报错，a不存在

'''
集合的应用
'''
# 求出a中每个元素的个数
# a=[1,2,3,1,2,3,1,1,3,3,3,3]
# b=set()
# for i in a:
#     b.add(i)
# for x in b:
#     print(x,'有',a.count(x),'个')

'''
集合的数学运算
交集--'&'或intersection()，取公共部分
差集--'-'或different()
反交集--'^'或symmetric_difference()
'''
# a={1,2,3,4}
# b={3,4,5,6}
# c=a.intersection(b)
# print(c)    # {3,4}
# d=a&b
# print(d)    # {3,4}

# a={1,2,3,4}
# b={3,4,5,6}
# c=a-b
# print(c)    # {1, 2}
# c=b-a
# print(c)    # {5, 6}

# a={1,2,3,4}
# b={3,4,5,6}
# c=a^b
# print(c)    # {1, 2, 5, 6}
# c=a.symmetric_difference(b)
# print(c)    # {1, 2, 5, 6}