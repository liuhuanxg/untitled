# num=int(input('请输入一个正整数：'))
# x=num%10
# num//=10
# max=x
# while num!=0:
#     x=num%10
#     num//=10
#     if max<x:
#         max=x
# print('最大数为：',max)

# num=int(input('请输入一个数：'))
# max=0
# while num>0:
#     x=num%10
#     if x>max:
#         max=x
#     num//=10
# print(max)

# i = 1
# a = 0
# b = 0
# char = input('请输入一个字符：')
# if '0' <= char <= '9':
#     a += 1
# elif 'A' <= char <= 'Z':
#     b += 1
# n = ord(char)
# max = n
# min = n
# while i <= 9:
#     char = input('请输入一个字符：')
#     n = ord(char)
#     if max < n:
#         max = n
#     if min > n:
#         min = n
#     if '0' <= char <= '9':
#         a += 1
#     elif 'A' <= char <= 'Z':
#         b += 1
#     i += 1
# print('数字个数为：%d，大写字母个数为：%d' % (a, b))
# print('ASCII码最大值为：%d，最小值为：%d' % (max, min))

# i = 1
# a = 0
# b = 0
# max = 0
# min = 127
# while i <= 10:
#     char = input('请输入一个字符：')
#     n = ord(char)
#     if max < n:
#         max = n
#     if min > n:
#         min = n
#     if '0' <= char <= '9':
#         a += 1
#     elif 'A' <= char <= 'Z':
#         b += 1
#     i += 1
# print('数字个数为：%d，大写字母个数为：%d' % (a, b))
# print('ASCII码最大值为：%d，最小值为：%d' % (max, min))


#10--20之间，遇到7的倍数跳过，遇到位数为7的结束
# i=10
# while i<=20:
#     if i%7==0:
#         i+=1
#         continue
#     elif i%10==7:
#         break
#     else:
#         print(i)
#     i+=1