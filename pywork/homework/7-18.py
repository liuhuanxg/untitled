# Python 0715 吕佳

# for循环
# range--前闭后开

# range(5)--> [0,5)
# for i in range(5):
#     print(i)
# for i in range(3,9):
#     print(i)
# for i in range(10,20,2):
#     print(i)
# for i in range(18,8,-3):
#     print(i)

# 列表：有序，可修改
# a=[]
# b=[1,2]
# print(a,type(a))
# print(b,type(b))

# a=[1,'a','b','c']
# print(a[0],a[1],a[2],a[3])

# i=0
# while i<len(a):
#     print('第',i+1,'个元素为：',a[i])
#     i+=1

# for i in range(len(a)):
#     print('第',i+1,'个元素为：',a[i])

# 拼接
# a=[1,2]
# b=[3,4,5]
# c=a+b
# print(c)

# 重复
# d=a*3
# print(d)

# x=a[1]+b[2]
# print(x)

# 切片
#[2:5]--> [2,5),同range，前闭后开
# a=[10,20,30,40,50,60,70]
# b=a[2:5]
# print(b)
# print(a)    #[10, 20, 30, 40, 50, 60, 70],不改变原列表

# a=['a','b','c',1,2,3,4,5]
# b=a[2:7:2]
# print(b)
# b=a[2:]
# print(b)
# b=a[:3]
# print(b)

# a=['a','b','c']
# for i in range(-1,-len(a)-1,-1):
#     print(i,':',a[i])

# '*'--可变
# a,b=[1,2]
# print(a)
# print(b)

# a,*b=[1,2,3,4]
# print(a)
# print(b)

# *a,b=[1,2,3,4]
# print(a)
# print(b)

# 追加
a=[1,2,3,4]
# a.append(9)
# print(a)

# 扩展，改变原列表
# a.append('b')
# print(a)

# 插入，再指定位置插入指定元素
# a.insert(2,'a')
# print(a)

# pop()函数--弹出，默认弹出最后一个
# b=a.pop()
# print(b)
# b=a.pop(1)
# print(b)
# print(a)    #[1, 3],原列表改变

# remove-- 移除从左到右第一个出现的值为参数的元素
# a=[1,2,3,4,3,7,6]
# a.remove(3)
# print(a)

# del
# a=[1,2,3,4,5,6,7]
# del a[2]
# print(a)
#
# del a
# print(a)   #报错，del+列表名，删除整个列表

# 修改
a=[3,1,2,4,3,6,7]
# a[3]=99
# print(a)

# reverse -- 倒序
# a.reverse()
# print(a)

# sort--默认升序排序
# a.sort()
# print(a)
# reverse=True -- 表示降序
# a.sort(reverse=True)
# print(a)

# key=str.lower -- 按照小写进行比较
# a=['ab','Ab','Bc']
# a.sort(key=str.lower)
# print(a)     #['ab', 'Ab', 'Bc']

# sorted -- 对列表进行排序，并写入新的列表(不改变原列表)
# b=sorted(a)
# print(b)
# print(a)

# count--元素'3'的个数
# a=[1,2,3,4,1,1,3,4]
# b=a.count(3)
# print(b)

# index--返回第一次出现元素'4'的索引值
# x=a.index(4)
# print(x)

#遍历二维列表
a=[[1,2,3],[4,5,6,7],[8,9],10]
# for x in a:
#     if type(x)!=list:
#         print(x)
#     else:
#         for y in x:
#             print(y,end=' ')
#         print()

# 输出3/6/9
# print(a[0][2])
# print(a[1][2])
# print(a[2][1])

# 赋值  '='
# a=[1,2,3]
# b=a
# a.append(4)
# print(a,b)
# print(id(a),id(b))
# print(a is b)

# a=3
# b=a
# a=5
# print(a,b)

'''
is和==的区别：
is--判断的是两对象是否就是同一个，是通过id来进行判断的
==--判断的是值是否相同
'''
# a=[1,2,3]
# b=[1,2,3]
# print(a==b)
# print(a is b)

# a='abc'
# b='abc'
# print(id(a))
# print(id(b))

# 赋值，浅拷贝，深拷贝
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
#
# a[3][2].append(30)
# print(a,id(a))
# print(b,id(b))
# print(c,id(c))
# print(d,id(d))

# 元组：有序，不可修改
a=(1,2,3,4)
# print(a,type(a))
# a[0]=9   #报错

# 遍历
# for x in a:
#     print(x)
#
# i =0
# while i<len(a):
#     print(a[i])
#     i+=1

# 切片
# print(a[2: :1])

# 合并、重复
# a=(1,2)
# b=(3,4)
# print(a+b)
# print(a*3)

# a,b,c=(1,2,3)
# print(a)
# print(b,c)

# * 可变，b会变为列表
# a,*b=(1,2,3,4,5)
# print(a)
# print(b)

# 元组不可修改；元组中可修改类型的数据，可修改
# a=(1,2,3,[4,5])
# a[3].append(99)
# print(a)

# 强制类型转换 tuple--元组 list--列表
# a=[1,2,3]
# b=tuple(a)
# print(type(b))
# c=list(b)
# print(type(c))

# 元组中','很重要
# a=(1)
# print(type(a))
# a=(1,)
# print(type(a))
# a=1,2
# print(a,type(a))
# a=[1]
# print(type(a))

#index--查找参数第一次出现的索引值
# a=(1,2,3,4)
# print(a.index(4))
# print(a.index(4,0,3))     #报错,范围内没有  后两个参数为查找的范围，同样左闭右开

# 遍历
# name=('tom','jerry','赵四')
# for i in name:
#     print(i)

# names=(('张三',19),('李四',20),('王五',30))
# for x,y in names:
#     print(x,':',y)

# enumerate--枚举
'''
(0, 11)
(1, 12)
(2, 13)
(3, 'a')
'''
# a=(11,12,13,'a')
# for x in enumerate(a):
#     print(x)

# a=(1,2,3,4,5,6,7,8,9,10,14)
# gs=0
# for x in a:
#     if x%7==0 or x%10==7:
#         gs+=1
#         print(x)
# print('共',gs,'个')

# a=(1,2,3,4,5,6,7,8,9,10,14)
# js=0
# os=0
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         os+=1
#     else:
#         js+=1
#     i+=1
# print('奇数有：',js,'个；偶数有：',os,'个')

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14)
# js=0
# os=0
# for x in a:
#     if x%2==0:
#         os+=1
#     else:
#         js+=1
# print('奇数有：',js,'个；偶数有：',os,'个')

# a=(3,2,5,1,4,9,7)
# max=a[0]
# min=a[0]
# x=0
# y=0
# for i in range(1,len(a)):
#     if max < a[i]:
#         max=a[i]
#         x=i
#     elif min > a[i]:
#         min=a[i]
#         y=i
# print('''
# 最大值：%d：%d
# 最小值：%d：%d''' % (x,max,y,min))

# 列表对应项相加，并给一个新列表
# big=[1,2,3,3,2,5]
# small=[11,22,8,7,5,9]
# s=[]
# for i in range(len(big)):
#     s.append(big[i]+small[i])
#     print('第', i + 1, '个月业绩：', s[i])
#     i+=1

# 传送站
# import time
# a=[1,2,3,4,5,6]
# while True:
#     t=a[0]
#     i=0
#     while i<len(a)-1:
#         a[i]=a[i+1]
#         i+=1
#     a[i]=t
#     time.sleep(1)
#     print(a)

# 倒序
# a=[1,2,3,4,5,6]
# i=0
# while i< len(a)//2:
#     # t=a[i]
#     # a[i]=a[len(a)-1-i]
#     # a[len(a)-1-i]=t
#     a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
#     i+=1
# print(a)

# a=[1,2,3,4,5,6]
# i=0
# j=len(a)-1
# while i<j:
#     # t=a[i]
#     # a[i]=a[j]
#     # a[j]=t
#     a[i],a[j]=a[j],a[i]
#     i+=1
#     j-=1
# print(a)

# a=[1,2,3,4,1,2,5,1,1,2]
# b=[1,2]
# n=0
# for i in range(len(a)-1):
#     # c=[]
#     #     # c.append(a[i])
#     #     # c.append(a[i+1])
#     #     # if c==b:
#     #     #     n+=1
#     if a[i]==b[0] and a[i+1]==b[1]:
#         n+=1
#     i+=1
# print(n)

#----------------------------------------------------------------------
#作业题
# 1.使用列表来保存商品
# lst=['手机','电脑','鼠标','平板']
# 2.展示所有的商品
# for ls in lst:
#     print(ls)
# 3.连续输出
# while True:
#     value=input('请输入要买的商品序号【输入q/Q退出】：')
#     if value.upper()=='Q':
#         print('程序结束了')
#         break
#     elif value.isdigit():
#         num=int(value)
#         if 0<num<=len(lst):
#             print(lst[num-1])
#         else:
#             print('输入的序号有误，请重新输入')
#     else:
#         print('输入的内容不正确，请重新输入')

# 猜水果系统
a = ['西瓜', '梨子', '香蕉', '核桃', '苹果', '桃子', '花生', '石榴', '西瓜', '梨子']
b = ['绿色的，红心', '配冰糖，暖到心', '弯弯的月儿小小的船,小小的船儿两头尖', '皱肉皱骨头， 骨头生在肉外头。', '乔布斯', '胖娃娃，没手脚，红尖嘴，一身毛，背上一道沟，肚里好味道。',
     '青藤藤，开黄花，地上开花不结果，地下结果不开。,', '小小红坛子，装满红饺子，吃掉红饺子，吐出白珠子。', '绿色的，红心', '配冰糖，暖到心']
print("欢迎来到猜水果小游戏！")
print("下面是游戏的规则，请认真阅读：")
print('*********************************')
print("1.猜题游戏一共有10个题，每个题10分，共一百分")
print("2.您在这个游戏中可以猜测10次，不管您答对还是答错，都会消耗猜测的次数")
print("3.每道题目开始时，系统都会提示是否使用锦囊，一共有三次的锦囊机会（锦囊一共有三种  ，并且可以重复选择！）。同时，锦囊不算在猜测的次数中。")
print("4.锦囊包括：1.提示水果第一个字。2.提示水果第二个字3.这个水果的字数")
print("5.游戏可以提前结束")
print("*********************************")
print("祝大家玩得愉快")
print("游戏开始选择1，游戏结束按任意键")
c = input("请选择开始：")  # 代表开始
if c=='1':
    print('游戏开始！')
    count=10
    cishu=3
    i=0
    fenshu=0
    while count >0:
        print('第',i+1,'题：',b[i])

        if cishu!=0:
            print('您也可以使用我们的锦囊（', cishu, '次机会）！选择请输入1，不使用输入任意键')
            f=input('请选择是否使用锦囊:')
            if f=='1':
                print('一共有三种锦囊供您选择')
                print('1.提示第一个字')
                print('2.提示第二个字')
                print('3.提示塔尔总字数')
                g=input('请选择您需要选择的锦囊类型：')
                if g=='1':
                    print('这个水果的第一个字是：',a[i][0])
                elif g=='2':
                    print('这个水果的第二个字是：',a[i][1])
                elif g=='3':
                    print('这个水果一共有',len(a[i]),'个字')
                else:
                    print('输入有误！默认放弃锦囊！')
                cishu-=1
            else:
                print('您的锦囊次数已经使用完，请用您自己的智慧解决吧!')

            d=input('请输入您所猜测的水果名：')
            if d==a[i]:
                fenshu+=10
                print('恭喜你，猜对了！是否继续？')
                print("继续玩游戏选择1,不继续选择任意键")
                o = input("请选择是否继续：")
                if o=='1':
                    print('好的！游戏继续！')
                    print('您还有',count-1,'次猜水果机会')
                    i+=1
                else:
                    print('您的总分为：',fenshu)
                    if fenshu>=60:
                        print('有点强呀')
                    elif 40<fenshu<60:
                        print('革命尚未成功，同志仍需努力！')
                    else:
                        print('菜是原罪')
                    print('您已提前结束游戏!')
                    break
            else:
                print('猜错了呦！')
                print('您还有',count-1,'次机会')
            count-=1
            if count==0:
                print('您的总分为：', fenshu)
                if fenshu >= 60:
                    print('有点强呀')
                elif 40 < fenshu < 60:
                    print('革命尚未成功，同志仍需努力！')
                else:
                    print('菜是原罪')
                print('您的次数已全部用完')
else:
    print('不玩？好吧')