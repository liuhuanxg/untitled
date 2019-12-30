'''
列表推导式
'''
# a=[1,2,3,4,5,6]
# b=[i*i for i in a]
# print(b)

# a=[1,2,3,4,5,6]
# x=map(lambda c:c*c,a)
# print(list(x))

# a=[1,2,3,4,5,6]
# def qiupf(x):
#     return x*x
# b=[qiupf(i) for i in a]
# print(b)

# a=[1,2,3,4,5,6]
# b=[i for i in a if i%2==1]
# print(b)

# a=[1,2,3,4,5,6]
# b=[i**2 for i in a if i%2==0 if i>2]
# print(b)
# b=[i**2 for i in a if i%2==0 and i>2]
# print(b)

# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j],end=' ')
#         j+=1
#     print()
#     i+=1

# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[y for x in a for y in x]
# print(b)

# 输出1 4 7
# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[a[i][0] for i in range(len(a))]
# print(b)

# 输出1 5 9
# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[a[i][i] for i in range(len(a))]
# print(b)

# 输出3 5 7
# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[a[i][len(a)-1-i] for i in range(len(a))]
# print(b)

# 生成a=[[1,2,3],[4,5,6],[7,8,9]]
# a=[]
# for i in range(3):
#     b = []
#     for j in range(3):
#         x=3*i+1+j
#         b.append(x)
#     a.append(b)
# print(a)

# a=[[3*i+j+1 for j in range(3)] for i in range(3)]
# print(a)

a=[lambda x:x*i for i in range(3)]
print(a[0](2))    # 4
print(a[1](2))    # 4
print(a[2](2))    # 4