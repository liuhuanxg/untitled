# a='abcABC12'
# print(a.upper())    # 转换为大写
# print(a.lower())    # 转换为小写
# print(a.swapcase())    # 大小写互换

'''
title()--将字符串中每个单词的首字母大写，以非字母划分
'''
# a='what is your name?'
# print(a.title())

'''
capitalize()--只有字符串的首字母大写
'''
# a='what is your name?'
# print(a.capitalize())

'''
expandtabs()--将tab或\t转换为空格
空格数=8-字符数
'''
a='234123\t45\t78'
print(a.expandtabs())