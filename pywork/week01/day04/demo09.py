# 集合 -- 无序，唯一，可修改

# 值唯一
# a={1,2,3,3,3,3,3}
# print(a)    # 自动去重，{1, 2, 3}

# 无序
# a={1,2,3,3,3,3,3}
# print(a[1])    # 报错，不支持索引，无序

'''
定义空集合只能用set()
'''
b={}    # 空字典
print(type(b))    # <class 'dict'>
b=set()
print(type(b))    # <class 'set'>