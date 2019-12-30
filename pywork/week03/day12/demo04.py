'''
send()
获取下一个值的效果和next()基本一致，只是在获取下一个值的时候，给上一个yield的位置传递一个数据。
注意事项：
1.第一次使用生成器时，是用next获取下一个值
2.最后一个yield不能接收外部的值
'''
# def g():
#     print('a')
#     x = yield 10
#     print('接收到数据', x)
#     yield x + 5    # 最后一个yield不能赋值
# x = g()
# print(next(x))    # 第一次使用生成器要用next()
# b = x.send(999)
# print(b)

'''
应用：
计算平均值，送n个，算n个
'''
# def g():
#     count=1
#     get_num=0
#     avg=0
#     total=0
#     while True:
#         get_num=yield avg
#         total=total+get_num
#         avg=total/count
#         count+=1
# x=g()
# next(x)
# print(x.send(10))
# print(x.send(20))
# print(x.send(30))

# def fib(n):
#     a,b=1,1
#     i=1
#     while i<=n:
#         yield a
#         a,b=b,a+b
#         i+=1
# for x in fib(10):
#     print(x)