# 列表修改
a=[3,1,2,4,3,6,7]
# a[3]=99
# print(a)

# reverse -- 倒置
# a.reverse()
# print(a)

# sort -- 升序排序
# a.sort()
# print(a)
# 降序排序
# reverse=True -- 表示降序
# a.sort(reverse=True)
# print(a)
# a=['ab','Ab','Bc']
# a.sort()
# print(a)     #['Ab', 'Bc', 'ab']
# key=str.lower -- 按照小写进行比较
# a=['ab','Ab','Bc']
# a.sort(reverse=True,key=str.lower)
# print(a)     #['ab', 'Ab', 'Bc']

# sorted -- 对列表进行排序，并写入新的列表(不改变原列表)
# b=sorted(a)
# print(b)
# print(a)

a=[1,2,3,4,1,1,3,4]
# b=a.count(3)     #元素'3'的个数
# print(b)

x=a.index(4)     #返回第一次出现元素'4'的索引值
print(x)
x=a.index(4,4,7)
print(x)