# from math import sqrt
# print(sqrt(-1))    # 错误
# 在某些平台上，结果为nan--非数值

# cmath--专门用于处理复数的模块
# import cmath
# print(cmath.sqrt(-1))    # 复数1j
# 复数都以j或J结尾

'''
模块名存在冲突，就像队列一样
因此除非必须使用from...import...，否则应坚持使用import...
'''

# Python没有专门表示虚数的类型，而将虚数视为实部为零的复数。