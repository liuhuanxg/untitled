'''
异常
当python脚本发生异常时，我们需要捕获处理它，否则程序会终止执行。
如果发生的异常类型和捕获的异常类型不相同，还是不能捕捉异常，程序还是会结束。
'''
# while True:
#     try:
#         a=eval(input('请输入表达式：'))
#         print(a)
#     except ZeroDivisionError as e:
#         print('除数为零，错误！')
#         print(e)
#         break

# 使用多分支结构，捕获多个异常
# try:
#     a=[1,2,3]
#     print(a[3])
#     print(3/0)
# except IndexError as i:
#     print(i)
# except ZeroDivisionError as e:
#     print(e)
# print('结束')

# 元祖格式捕获多个异常
# try:
#     a = [1, 2, 3]
#     print(a[3])
#     print(3 / 0)
# except (IndexError,ZeroDivisionError) as e:
#     print('有异常',e)
# print('结束')

# else格式
# 无异常正常结束则执行else中代码
# 注意，一定要有except
# try:
#     a=[1,2,3]
#     print(a[1])
# except IndexError as i:
#     print(i)
# else:
#     print('无异常')
# print('结束')

# 捕捉全部异常except/except Exception
# try:
#     a = [1, 2, 3]
#     print(a[1])
#     print(1/0)
# except Exception as f:
#     print(f)
# print('结束')

# try...finally格式
# try:
#     a=[1,2,3]
#     print(a[3])
# except IndexError as f:
#     print(f)
# else:
#     print('无异常')
# finally:
#     print('无论有没有错误，我都会执行')