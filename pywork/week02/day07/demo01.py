'''
字符串
以引号包围的，不可修改的有序序列
'''
# a='123abc'
# print(a[0])
# print(a[3])
# i=0
# while i<len(a):
#     print(a[i],end='')
#     i+=1

# a='123abc'
# for i in range(len(a)):
#     print(a[i])

# a='123abc'
# a[2]=6    # 报错，不可修改

a='123abc'
for i in range(-1,-len(a)-1,-1):
    print(a[i],end='')
print()
a='123abc'
i=-1
while i>=-len(a):
    print(a[i],end='')
    i-=1