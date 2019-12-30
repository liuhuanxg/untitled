# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# bs = 0  # 报数
# i = 0  # 下标
# count_0=0
# while True:
#     if a[i] != 0:
#         bs += 1
#         if bs == 3:
#             a[i] = 0
#             bs = 0
#             count_0+=1
#     i += 1
#     if i == len(a):
#         i = 0
#     if count_0==9:
#         break
# print(a.index(max(a,key=abs)))

# n=int(input('想要输出的行数：'))
# for i in range(1,n+1):
#     for j in range((2*n)//2-i):
#         print(' ',end='')
#     for j in range(2*i-1):
#         print('*',end='')
#     print()

n=int(input('想要输出的行数：'))
for i in range(1,n):
    for j in range((2*n)//2-i):
        print(' ',end='')
    print('*',end='')
    for j in range(2*(i-1)-1):
            print(' ',end='')
    if i != 1:
        print('*',end='')
    print()
for j in range(2*n-1):
    print('*',end='')