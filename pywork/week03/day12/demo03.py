'''
生成器
yield起到了return的功能，但不会结束函数。保留当前函数的状态，等到下次进入继续使用。
'''
def shengchan(n):
    i=1
    while i<=n:
        yield i
        i+=1
x=shengchan(5)
print(x)
for y in x:
    print(y)
#
# print(x.__next__())
# print(x.__next__())
# print(next(x))
# print(next(x))
# print(x.__next__())

# def dee():
#     yield 1
#     yield 2
#     yield 3
# x=dee()
# print(x.__next__())
# print(next(x))
# print(next(x))