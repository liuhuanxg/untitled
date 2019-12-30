# char=input('请输入一个字符：')
# n=ord(char)
# if n<=90 and n>=65:
#     print('这是一个大写字母')
# elif n<=122 and n>=97:
#     print('这是一个小写字母')
# # elif n<=57 and n>=48:
# #     print('这是一个数字')
# elif char >= '0' and char <= '9':
#     print('这是一个数字')
# elif n == 95:
#     print('这是一个下划线')
# else:
#     print('其他字符')


# 连续比较
char=input('请输入一个字符：')
n=ord(char)
if 65 <= n <=90:
    print('这是一个大写字母')
elif 97 <= n <= 122:
    print('这是一个小写字母')
elif '0' <= char <= '9':
    print('这是一个数字')
elif n == 95:
    print('这是一个下划线')
else:
    print('其他字符')