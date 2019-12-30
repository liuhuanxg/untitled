# 使用for循环取出生成器中所有的值
# def gen1():
#     for c in 'AB':
#         yield c
#     for i in range(3):
#         yield i
# for x in gen1():
#     print(x)

'''
yield from
'''
def g():
    yield from 'AB'
    yield from range(5)
for x in g():
    print(x)