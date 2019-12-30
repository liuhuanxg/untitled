'''
find()--从左往右找
rfind()--从右往左找
返回找到的，开头位置的索引
找不到时，返回-1
'''
# a='abcdef'
# b='cd'
# x=a.find(b)
# print(x)
# print(a.find('zz'))

# a='abcdefcdg'
# b='cd'
# x=a.find(b)
# print(x)

# a='abcdefcdg'
# b='cd'
# x=a.rfind(b)
# print(x)

'''
index()--功能与find()相同
rindex()--功能与rfind()相同
找不到报错
count()--寻找参数字符串存在的个数
'''
# a='abcdefcdg'
# b='cd'
# x=a.index(b)
# print(x)
# # b='cda'
# # print(a.index(b))
#
# a='abcdefcdg'
# b='cd'
# x=a.rindex(b)
# print(x)
# # b='cda'
# # print(a.rindex(b))

a='abcdefcdgcd'
b='cd'
print(a.count(b))