# 列表 有序 可修改

# a=[]
# b=[1,2]
# print(a,type(a))
# print(b,type(b))

a=[1,'a','b','c']
# print(a[0],a[1],a[2])
i=0
while i<len(a):
    print('第',i+1,'个值为：',a[i])
    i+=1
# for i in a:
#     print('第',i,'个值为：',a[i])
for i in range(len(a)):
    print('第', i, '个值为：', a[i])