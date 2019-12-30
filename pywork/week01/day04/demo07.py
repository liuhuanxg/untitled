# 修改
'''
update()--以字典形式更新指定字典的内容
如果键不存在，创建
如果存在，覆盖
'''
# a={'name':'张三','age':19,'sex':'男'}
# b={'name':'李四','score':89}
# a.update(b)
# print(a)

'''
in a/not in a--判断指定的键是否存在字典当中
与值无关
in a功能与in a.keys()相同，但不可完全划等号
要判断值是否存在可用in a.values()
'''
a={'name':'张三','age':19,'sex':'男'}
if 'name' in a:
    print('有姓名')
if 'score' not in a:
    print('没有成绩')
if '张三' in a:    # 不成立
    print('张三在里面')