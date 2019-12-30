'''
dir()--可以列出字符串对象中所有的方法的名称
help()--可查看某个方法的具体介绍
'''
s='aa'
print(dir(s))
print(dir(str))

print(help(str.replace))