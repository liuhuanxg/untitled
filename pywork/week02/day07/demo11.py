'''
字符串的装饰
center()--居中，可以指定填充内容，默认空格
ljust()--在指定长度左齐，可以指定填充内容，默认空格
rjust()--在指定长度右齐，可以指定填充内容，默认空格
zfill()--将字符串填充到指定长度，不足用0从左开始补充
strip()--去除空格，也可指定去除内容，可选左右
'''

# a='123'
# b=a.center(7,'*')
# print(b)
# print(a)

# a='123'
# b=a.ljust(10,'$')
# print(b)
# b=a.rjust(10,'$')
# print(b)

# a='123'
# print(a.zfill(10))

# a='     123     '
# print(a.lstrip(),end='$')    # 去左
# print()
# print(a.rstrip(),end='$')    # 去右
# print()
# print(a.strip(),end='$')    # 左右都去

# a='###123####'
# print(a.lstrip('#'))
# print(a.rstrip('#'))
# print(a.strip('#'))