# 集合数学运算
'''
交集
&或intersection()--取公共部分
'''
# a={1,2,3,4}
# b={3,4,5,6}
# c=a.intersection(b)
# print(c)
# d=a&b
# print(d)

'''
差集
-或difference
'''
# a={1,2,3,4}
# b={3,4,5,6}
# c=a-b
# print(c)
# c=b-a
# print(c)

'''
反交集
^或symmetric_difference()
'''
a={1,2,3,4}
b={3,4,5,6}
c=a^b
print(c)
c=a.symmetric_difference(b)
print(c)