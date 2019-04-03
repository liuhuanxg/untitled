import copy


#浅拷贝只拷贝第一层数据，对于列表中嵌套的数据不能拷贝，映射的地址还在元地址中
#深拷贝会把所有层的数据都拷贝，没有内存地址相同的数据

'''
#深浅拷贝的原理
a=[1,2,['alex','asic'],5]
b=a.copy()

#浅拷贝只拷贝数值，对原始数据第一层进行更改时不改变已拷贝过的值如：
print('b:',b)
a[1]=-2
print('a:',a)
print('b:',b)

#两个数据的内存地址是不相同的
print(id(a)==id(b))             #False  
#但内层的一些数据内存还是相同的，还属于同一数据，更改时会相互影响
print(id(a[2])==id(b[2]))       #True

#对深层次的值进行更改时被拷贝的数据和原数据会相互影响
b[2][1]='我是被拷贝数据更改的'
print('a:',a)
print('b:',b)
a[2][0]='我是原数据更改的'
print(a)
print(b)
'''

'''
c=[1,2,['alex','asic'],5]
d=copy.deepcopy(c)
#深拷贝  两个数值的内容互不干扰，没有内存地址相同的值，更改不会相互影响

print(id(c)==id(d))             #False
print(id(c[2])==id(d[2]))       #False

#对原数据进行更改，不会影响被拷贝的数据
c[2][0]='我是原数据更改的'
print(c)
print(d)
d[2][0]='我是原数据更改的'
'''
'''
a={'姓名':[12,23],'age':19}
b=a.copy()
print(b)
print(id(b)==id(a))
print(id(b['姓名'])==id(a['姓名']))

a['姓名'][1]=2
print(a)
print(b)
'''

a=[12,3,4]
b=a
a[1]=8
print(b)   #[12, 8, 4]
#直接用=赋值时，第一层也会改变
c=8
d=c
c=9
print(d)   #8