'''
partiton()--分隔
参数为一个字符串，以参数分隔长字符串
只能分割为三部分，包括自身，且以第一次出现的为准
返回值为一个元组
'''
# x='123ab456ab789'
# print(x.partition('ab'))    # ('123', 'ab', '456ab789')

'''
split()--分隔
参数为一个字符串，以参数分隔长字符串，不包括自身
若出现多次，可选用第二个参数maxsplit，设置分隔几次
返回值为一个列表
'''
# a='123a456a789a0'
# print(a.split('a'))    # ['123', '456', '789', '0']
#
# a='2019-07-24'
# print(a.split('-'))
#
# a='123ab456ab789ab000'
# print(a.split('ab',maxsplit=1))
# print(a.split('ab',maxsplit=2))
# print(a.split('ab',maxsplit=3))

'''
splitlines()--按照行分隔
返回值为列表
'''
# a='abc\n123\n45'
# print(a.splitlines())

'''
用split()实现splitlines()
'''
# a='abc\n123\n45'
# print(a.split('\n'))

a='abc\n123\n45'
i=0
while i<len(a):
    if a[i]=='\n':
        print()
    else:
        print(a[i],end='')
    i+=1