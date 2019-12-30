#Python 0715 吕佳

# salary=int(input('请输入您的工资：'))
# if salary>=3000 and salary<10000:
#     print('电动72 35v 50迈，续航：90')
# elif salary>=10000 and salary<20000:
#     print("买辆迈腾")
# elif salary>=20000 and salary<30000:
#     print("买辆速腾")
# elif salary>=30000:
#     print('买辆A6')

# score=int(input('请输入四级成绩：'))
# if score<60:
#     print('下次加油')
# else:
#     print('恭喜获得四级证书')

# score=int(input('请输入学习成绩：'))
# if score>=90 and score <=100:
#     print('优秀')
# elif score>=80 and score<90:
#     print('良好')
# elif score>=70 and score<80:
#     print("一般")
# elif score>=60 and score<70:
#     print('及格')
# else:
#     print('不及格')

#大小写 数字 下划线 其他字符
# char=input('请输入一个字符：')
# n=ord(char)
# if n<=90 and n>=65:
#     print('这是个大写字母')
# elif n<=122 and n>=97:
#     print("这是个小写字母")
# elif char<='9' and char>='0':
#     print('这是一个数字')
# elif n==95:
#     print('这是一个下划线')
# else:
#     print('其他字符')

#连续比较
# char=input('请输入一个字符：')
# n=ord(char)
# if 65<=n<=90:
#     print('这是个大写字母')
# elif 97<=n<=122:
#     print("这是个小写字母")
# elif '0'<=char<='9':
#     print('这是一个数字')
# elif n==95:
#     print('这是一个下划线')
# else:
#     print('其他字符')

#西红柿会员
# price=float(input('请输入西红柿单价：'))
# num=float(input('请输入购买数量：'))
# total=price*num
# if total>=50:
#     level=int(input('请输入vip级别：'))
#     if level == 1:
#         total=total*0.8
#         print('享受八折优惠，金额为：%.2f'%total)
#     elif level==2:
#         total=int(total)
#         total=total-total%10
#         print('享受抹零优惠，金额为：%d' % total)
#     elif level==3:
#         print('享受抹小数优惠，金额为：%d' % total)
# else:
#     sex=input('请输入性别：')
#     if sex=='男':
#         print('赠送玩具劳斯莱斯一辆')
#     elif sex=='女':
#         print('赠送小猫一只')

#循环
'''
循环三大件：
1.初始值
2.控制条件
3.步长
'''

#吃西瓜
# money=int(input('请输入金额：'))
# while money>=10:
#     print('吃一块西瓜')
#     money-=10
#     print('剩余',money,'元')

#求1--10的和
# n=1
# sum=0
# while n<=10:
#     sum+=n
#     n+=1
# print(sum)

#求6--2之间所有整数的乘积
# a=6
# s=1
# while a>=2:
#     s*=a
#     a-=1
# print(s)

#输入十个数，计算这十个数的和
# i=1
# sum=0
# while i<=10:
#     n=int(input('请输入一个数字：'))
#     sum+=n
#     i+=1
# print(sum)

#1-2+3-4...+99
# n=1
# sum=0
# while n<100:
#     if n%2==0:
#         sum-=n
#     else:
#         sum+=n
#     n+=1
# print(sum)

#输入五个数，求最大值
# i=1
# max=int(input('请输入一个数字：'))
# while i<=4:
#     data=int(input('请输入一个数字：'))
#     if data>max:
#         max=data
#     i+=1
# print('最大值为：',max)

'''
*
**
***
****
*****
'''
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end='')
#         j+=1
#     print()
#     i+=1

#break--中断循环
# i=1
# while i<=5:
#     age=int(input('请输入年龄：'))
#     if age<0:
#         print('您输入的年龄有问题')
#         break
#     i+=1

#continue--退出本次循环，进入下一循环
#跳过3的倍数输出
# i=1
# while i<=10:
#     if i%3==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

'''
输入十个数
如果输入的<18,不参加运算
如果输入的>65，跳出循环
求输入的年龄的平均值
'''
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
#     print('无有效数据')
# else:
#     print('平均值为：',(sum//n))

#数字倒序
# num=int(input('请输入一个数字：'))
# y=0
# while num!=0:
#     y=y*10+num%10
#     num//=10
# print(y)

#-----------------------------------------------------------------------
#作业题
#00 用户登录
# while True:
#     userName=input('请输入用户名：')
#     passWord=input('请输入密码：')
#     if userName=='lvjia' and passWord=='123123':
#         print('登录成功！')
#         break
#     else:
#         print('用户名或密码错误，请重试！')

#Python 0715 吕佳

# 01 猜拳游戏
# import random
#
# num=1
# win=0
# fail=0
# while num<=3:
#     if fail==2 or win==2:
#         break
#     user=int(input('''
#     请出拳
#     0：拳头
#     1：剪刀
#     2：布'''))
#     if user>2:
#         print('不能大于2的值')
#     else:
#         data=['石头','剪刀','布']
#         com=random.randint(0,2)
#         print('您出的是{}，电脑出的是{}'.format(data[user],data[com]))
#         if user==com:
#             print('平局')
#             continue
#         elif (user==0 and com==1) or (user==1 and com==2) or (user==2 and com==0):
#             print('您赢了！')
#             win+=1
#         else:
#             print('您输了！')
#             fail+=1
#     num+=1
# if win==2:
#     print('游戏结束，您赢了！')
# else:
#     print('游戏结束，您输了！')

# 02 数字炸弹
import random,time

bomb=random.randint(0,99)
start=0
end=99
while True:
    people=int(input('请输入{}到{}之间的数字'.format(start,end)))
    if people>bomb:
        print('man--->大了')
        end=people-1
    elif people<bomb:
        print('man--->小了')
        start=people+1
    else:
        print('BOMING')
        break

    print('等待电脑输入{}到{}之间的数字'.format(start,end))
    time.sleep(2)
    computer=random.randint(start,end)
    print('电脑输入了{}'.format(computer))
    if computer>bomb:
        print('computer--->大了')
        end=computer-1
    elif computer<bomb:
        print('computer--->小了')
        start=computer+1
    else:
        print('boom!!')
        break
print('数字炸弹--->',bomb)