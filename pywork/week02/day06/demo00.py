# 传送站
# import time
# a=[1,2,3,4,5,6]
# def csd():
#     t=a[len(a)-1]
#     i=len(a)-2
#     while i>=0:
#         a[i+1]=a[i]
#         i-=1
#     a[0]=t
#     for i in range(0,len(a)):
#         print(a[i],end='\t')
#     print()
#     time.sleep(1)
#     csd()
# csd()

# import time
# a=[1,2,3,4,5,6]
# while True:
#     t=a[len(a)-1]
#     i=len(a)-2
#     while i>=0:
#         a[i+1]=a[i]
#         i-=1
#     a[0]=t
#     for i in range(0,len(a)):
#         print(a[i],end='\t')
#     print()
#     time.sleep(1)

# 判断a中有多少个b
# a=[1,1,2,3,4,5,6,1,1,1,2,3]
# b=[1,1]
# count=0
# i=0
# while i<=len(a)-len(b):
#     if a[i]==b[0] and a[i+1]==b[1]:
#         count+=1
# print(count)

# 若匹配成功的不参加下次比较
# a = [1, 1, 2, 3, 4, 5, 6, 1, 1, 1, 2, 3]
# b = [1, 1]
# count = 0
# i = 0
# while i <= len(a) - len(b):
#     if a[i] == b[0] and a[i + 1] == b[1]:
#         count += 1
#         i += len(b)
#     else:
#         i += 1
# print(count)

# b不定长
a = [1, 1, 2, 3, 4, 5, 6, 1, 1, 1, 2, 3]
b=eval(input('请输入请输入想要搜索的列表：'))
print(b)
