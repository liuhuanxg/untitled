# 求出a中每个元素的个数
a=[1,2,3,1,2,3,1,1,3,3,3,3]
b=set()
for i in set(a):
    b.add(i)
for n in b:
    print(n,'出现的次数为：',a.count(n))