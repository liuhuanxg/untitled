'''
判断变量是不是什么类型
1.type(a)!=tuple或type(a)==tuple
2.isinstance(2,int)  形如：isinstance(变量，类型)
返回值皆为False或True
'''
a=(1,2,3)
print(type(a)==tuple)

print(isinstance(2,int))