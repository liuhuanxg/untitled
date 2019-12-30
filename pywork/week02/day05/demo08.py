'''
递归函数
递归三大件：
1.递归前进
2.递归后退
3.递归边界
当递归边界成立的时候，递归后退，不成立的时候递归前进
'''

# def jiecheng(n):
#     if n==1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# x=jiecheng(6)
# print(x)

# 斐波那契序列
# def tuzi(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return tuzi(n-1)+tuzi(n-2)
# n=int(input('请输入月份：'))
# # print(n,'的兔子数为：',tuzi(n))
# for i in range(1,n+1):
#     print('第',i,'个月的兔子数为：',tuzi(i))

def tuzi(n):
    a, b = 1, 1
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            print(1, end='\t')
        else:
            a, b = b, a + b
            print(b, end='\t')
n=int(input('请输入月份：'))
tuzi(n)


# def p_n(n):
#     print(n)
#     if n==1:
#         return
#     p_n(n-1)
#     print('--heihei')
# p_n(4)
'''
4
3
2
1
--heihei
--heihei
--heihei
'''