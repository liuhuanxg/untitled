'''题目：求一个3*3矩阵主对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''
'''#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(raw_input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print sum
'''
'''
input num:
78
input num:
34
input num:
23
input num:
34
input num:
56
input num:
33
input num:
12
input num:
21
input num:
2
136.0
'''