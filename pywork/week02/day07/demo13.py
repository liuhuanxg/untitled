# 判断是否完全由数字组成
# a='123d'
# b=a.isdigit()
# print(b)

# 判断是否完全由字母组成
# a='azAz_'
# print(a.isalpha())

# 判断是否完全由数字或字母组成
# a='123aZ'
# print(a.isalnum())

# 判断字符串中所有字母是否完全为小写
# a='ac123sd'
# print(a.islower())

# 判断字符串中所有字母是否完全为大写
# a='12JAKSa'
# print(a.isupper())

# 判断是否满足title格式
# a="What Is Your Name?"
# print(a.istitle())

# 判断是否完全由空格组成
# a='        '
# print(a.isspace())

# 判断字符串的开头字符，也可以截取判断
# 范围同样左闭右开
# a='aadsKJLA123'
# print(a.startswith('123'))
# print(a.startswith('123',8,11))

# 判断字符串的结尾字符，也可以截取判断
a='aadsKJLA'
print(a.endswith('L'))
print(a.endswith('L',0,7))