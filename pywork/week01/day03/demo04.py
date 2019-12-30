# 切片
# [2:5]--> [2,5),同range，前闭后开
# a=[10,20,30,40,50,60,70]
# b=a[2:5]
# print(b)

a=['a','b','c',1,2,3,4,5]
b=a[2:7:2]
print(b)
b=a[2:]
print(b)
b=a[:3]
print(b)
print(a)

a=['a','b','c']
for i in range(-1,-len(a)-1,-1):
    print(i,':',a[i])