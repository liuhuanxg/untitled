'''
三引号定义的同值字符串占用的内存空间与单双引号的不同
!!!但前提是两个三引号中间有空格或换行
这时为了保留格式，会为它开辟新的存储空间
#
'''
# a='abc'
# b="abc"
# c='''
# abc
# '''
# print(a)
# print(b)
# print(c)    # 有换行
#
# print(a == b)    # True
# print(a is b)    # True
# print(b == c)    # False
# print(b is c)    # False

'''
从键盘获取的同值字符串，内存地址不同
因为input是底层封装好的函数，经过了函数的处理，内存地址就不一样了
'''
# a=input('请输入字符串：')
# b=input('请输入字符串：')
# print(a == b)    # True
# print(id(a))    # 39789992
# print(id(b))    # 39790384
# print(a is b)    # False

'''
字符串的运算符：
'+'--连接
'*'--重复
in/not in--判断字符串（任意长度）是否在里面，返回值是bool类型
'%'--字符串的格式化，与占位符搭配使用(%s %d %f)
'r'--保留原格式，针对转义字符
[5]--索引
[::]--切片
'''
# name='steven'
# result='st' in name
# print(result)    # True
# name='steven'
# result='a' not in name
# print(result)    # True

# name='steven'
# print('%s说：大家都要好好学习！' % name)
# print('%s说：%s' % (name,'大家都要好好学习！'))

# print('tom说：\'哈哈哈\'')
# print(r'tom说：\'哈哈哈\' ')    # '\'--转义字符

# a='hello world'
# # 逆序输出world，正向输出hello
# print(a[0:5],a[-1:5:-1])
# # 逆序输出整个hello world
# print(a[::-1])
# # 打印oll
# print(a[-7:-10:-1])
# # 打印llo wo
# print(a[2:8])

# a='hello world'
# print(a.index('l'))    # 从左向右
# print(a.rindex('l'))    # 从右向左