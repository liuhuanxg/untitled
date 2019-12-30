'''
字符串的替换
replace()--从左到右替换指定的元素
可以选用第三个参数指定替换的个数，默认全部替换
原字符串不变
'''
# a='123abc456abc'
# b=a.replace('abc','xy')
# print(b)
# b=a.replace('abc','xy',1)
# print(b)
# print(a)

'''
translate()--按照对应关系来替代内容
maketrans()--用于创建字符映射的转换表
第一个参数是字符串，第二个参数也是字符串，表示转换的目标
两个字符串的长度必须相同，为一一对应的关系
'''
s='12345678901111'
# a,b长度必须相同
a='1234567'
b='abcdefg'
table=str.maketrans(a,b)
c=s.translate(table)
print(c)