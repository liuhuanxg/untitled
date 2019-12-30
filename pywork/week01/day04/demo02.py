'''
嵌套循环
'''
# 矩形
# j=1
# while j<=5:
#     i=1
#     while i<=5:
#         print('*',end='')
#         i+=1
#     print()
#     j+=1

# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end='')
#     print()

# 正三角
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end='')
#         j+=1
#     i+=1
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# 倒三角
# i=1
# while i<6:
#     j=1
#     while j<i:
#         print(' ',end='')
#         j+=1
#     j=1
#     while j<=6-i:
#         print('*',end='')
#         j+=1
#     print()
#     i+=1

# for i in range(1,6):
#     for j in range(i):
#         print('',end=' ')
#     for j in range(1,6-i+1):
#         print('*',end='')
#     print()

# 99乘法表
# for j in range(1,10):
#     for i in range(1,j+1):
#         print(i,'*',j,'=',i*j,end='\t')
#     print()

# j=1
# while j<10:
#     i=1
#     while i<=j:
#         print(i,'*',j,'=',i*j,end='\t')
#         i+=1
#     print()
#     j+=1

# for j in range(1,10):
#     i=1
#     while i<=j:
#         print(i, '*', j, '=', i * j, end='\t')
#         i+=1
#     print()

# j=1
# while j<10:
#     for i in range(1,j+1):
#         print(i, '*', j, '=', i * j, end='\t')
#     print()
#     j+=1