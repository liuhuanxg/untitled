# #判断一个数是不是质数
# while True:
#     i=int(input('请输入一个数：'))
#     if i>=2:
#         j=2
#         while j<=i//2:
#             if i%j==0:
#                 print('不是质数。')
#                 break
#             j += 1
#         else:
#              print('是质数')
#     elif i==0 or i==1:
#         print('既不是质数也不是合数。')

# i=233
# count=0
# while i<899:
#      j = 2
#      while j<i:
#          if i%j==0:
#           # print(i,'不是素数')
#             break
#          j += 1
#      else:
#         print(i,'是素数')
#         count+=1
#      i += 1
# print(count,'个素数')

# i=1
# while i<=9:
#     if i<=5:
#         j=1
#         while j<=5-i:
#             print(' ',end='')
#             j+=1
#         k=1
#         while k<=2*i-1:
#             print('*',end='')
#             k+=1
#         print()
#     else:
#         j = 1
#         while j <=i-5:
#             print(' ', end='')
#             j+= 1
#         k = 9
#         while k >2*(i-5):
#             print('*', end='')
#             k -= 1
#         print()
#     i+=1


# a=[1,2,3,4,5,6,7,8,9,10,11,12]
# b=[11,22,33,44,55,66,77,88,99,110,111,112]
# i=0
# c=[]
# while i<=11:
#       c .append(a[i] + b[i])
#       # append扩展列表
#       i+=1
# print(c)

# a=int(input('请输入一个整数:'))
# b=0
# while a>0:
#     b=b*10+a%10
#     a=a//10
#     # 进行循环除10操作
# print(b)

# a=int(input('请输入一个整数：'))
# print(str(a)[::-1])

# a=[1,2,3,4,5,6,7,8,9,10]
# i=2
# while i<=4:
#     a[i],a[9 -i]=a[9-i],a[i]
#     i+=1
# print(a)
# for i in range(len(a)//2):
#     a[i], a[9 - i] = a[9 - i], a[i]
# print(a)

a=set((1,2,4,5,6,5,6,7))
# 删除指定字符，不存在时报错
# a.remove(8)
# print(a)
# 删除指定字符，不存在时不报错
a.discard(8)
print(type(a))
#add添加一个元素
a.add('wo')
print(a)
# update可以添加多个元素
a.update((11,22))
print(a)

