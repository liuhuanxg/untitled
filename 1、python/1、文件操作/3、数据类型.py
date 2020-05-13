#将字典按照value值排序
"""
d= {'a':24,'g':52,'i':12,'k':33}
print(d.items())
d1=sorted(d.items(),key=lambda x:x[1])
print(d1)
dict={}
for i in d1:
    dict[i[0]]=i[1]
print(dict)
"""

#字典推导式
# 8.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
str1 = "k:1|k1:2|k2:3|k3:4"
def str2dict(str1):
    dict1 = {}
    for iterms in str1.split('|'):
        key,value = iterms.split(':')
        dict1[key] = value
    return dict1

d = {k:int(v) for t in str1.split("|") for k, v in (t.split(":"), )}
print(d)


#9.请按alist中元素的age由大到小排序
alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
def sort_by_age(list1):
    return sorted(alist,key=lambda x:x['age'],reverse=True)
print(sort_by_age(alist))


# 13.请写出一段python代码实现删除list里面的重复元素？
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
print(l2)

l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)