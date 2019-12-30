'''
字符串的切片：
从字符串复制出一份指定的内容，存储在另一个变量中
不会对原字符串有影响
前闭后开 步长默认为1
'''
# a='123abc'
# print(a[0:5])
# for i in range(5):
#     print(a[i],end='')
# print()
# print(a[0:5:2])
# for i in range(0,5,2):
#     print(a[i],end='')

# a = '123abcd'
# print(a[0:])
# print(a[3:])
# print(a[:5])
# print(a[:])
# print(a[::3])

# # 输出ad
# print(a[3::3])
# for i in range(3,len(a),3):
#     print(a[i],end='')
# print()
# print(a[::3][1:])
#
# # 输出1a
# print(a[0:4:3])
#
# print(a[0:5:-1])    # 无结果
# print(a[::-1])
# print(a[-1:-5:-2])

# a='123456789'
# print(a[-8:5])
# print(a[0:-7])
# print(a[-7:0])    # 无结果
# print(a[-7:0:-1])
# print(a[-1:-5])    # 无结果
# print(a[-1:-5:-1])