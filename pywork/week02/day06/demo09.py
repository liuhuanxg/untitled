'''
abs()--绝对值
'''
# a=-1
# b=2
# print(abs(a))
# print(abs(b))

'''
max()--求最大值
注意变量名不要叫max！否则调用max()会出错
'''
# a=[1,3,2,5,4]
# x=max(a)
# print(x)
#
# a=[-1,-3,-2,-5,-4]
# b=max(a)
# print(b)    # -1

'''
key=函数名称--指定求最大值的规则
'''
# 绝对值最大的那个
# a=[-1,-3,-2,-5,-4]
# b=max(a,key=abs)
# print(b)    # -5

def hanshu(x):
    print('---')
    return abs(x)
a=[-1,-3,-2,-5,-4]
# 把函数名作为一个参数换地给了max()，max()内部执行了hanshu()
b=max(a,key=hanshu)
print(b)