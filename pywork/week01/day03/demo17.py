# 列表对应项相加，并给一个新列表
# big=[1,2,3,3,2,5]
# small=[11,22,8,7,5,9]
# s=[]
# for i in range(len(big)):
#     s.append(big[i]+small[i])
#     print('第', i + 1, '个月业绩：', s[i])
#     i+=1

# 传送站
# import time
# a=[1,2,3,4,5,6]
# while True:
#     t = a[0]
#     i = 0
#     while i < len(a) - 1:
#         a[i] = a[i + 1]
#         i += 1
#     a[i] = t
#     time.sleep(1)
#     print(a)

# 倒序
# a=[1,2,3,4,5,6]
# i=0
# while i<len(a)//2:
#     # t=a[i]
#     # a[i]=a[len(a)-i-1]
#     # a[len(a)-i-1]=t
#     a[i],a[len(a)-1-i]=a[len(a)-1-i],a[i]
#     i+=1
# print(a)

# a=[1,2,3,4,5,6]
# i=0
# j=len(a)-1
# while i<j:
#     # t=a[i]
#     # a[i]=a[j]
#     # a[j]=t
#     a[i],a[j]=a[j],a[i]
#     i+=1
#     j-=1
# print(a)

a=[1,2,3,4,1,2,5,1,1,2]
b=[1,2]
n=0
for i in range(len(a)-1):
    # c=[]
    # c.append(a[i])
    # c.append(a[i+1])
    # if c==b:
    #     n+=1
    if a[i]==b[0] and a[i+1]==b[1]:
        n+=1
    i+=1
print(n)