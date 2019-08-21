#1、删除列表中的重复元素
l=[1,2,1,3,1,4,5]
print(list(set(l)))
d={}
for i in l:
    d[i]=1
print(list(d.keys()))


#2、tuple和list的转换
l=tuple([1,2,3,45,])
print(l)
print(list(l))


#3、创建字典的方式
d1={}
d1['key1']=4
print(d1)

d2={"key1":"v1","key2":"v2"}
print(d2)

dict3 = dict(key1="33",key2="44")
print(dict3)

dict4=dict()
print(type(dict4))