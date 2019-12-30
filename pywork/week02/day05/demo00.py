# 求1--100以内，能被7整除或者能被3整除，但不能同时被这两个数整除的数的个数
# n=0
# for i in range(1,101):
#     if i%7==0 and i%3==0:
#         continue
#     if i%7==0 or i%3==0:
#         n+=1
# print(n)

# 将字典的键和值交换
# dct1={'name':'张三','age':19}
# a={}
# for k,v in dct1.items():
#     a[v]=k
# print(a)

# dct1={'name':'张三','age':19}
# a={}
# for k in dct1.keys():
#     a[dct1[k]]=k
# print(a)