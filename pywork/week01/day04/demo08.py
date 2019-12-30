'''
字典-->内含元组的列表
内含元组的列表-->字典
'''
# a={'name':'张三','age':19,'sex':'男'}
# b=[]
# c={}
# for k,v in a.items():
#     b.append((k,v))
# print(b)
# for x in b:
#     y,z=x
#     c[y]=z
# print(c)

'''
键重复时，后面的会覆盖前面的
'''
# a={'name':'张三','age':19,'sex':'男','age':99}
# print(a)    # {'name': '张三', 'age': 99, 'sex': '男'}

'''
以num:001,name=张三,age:18,sex:男格式打印
'''
a={
    '001':{'name':'张三','age':18,'sex':'男'},
    '002':{'name':'李四','age':28,'sex':'男'},
    '003':{'name':'王五','age':38,'sex':'女'},
    '004':{'name':'赵四','age':48,'sex':'男'},
}
# for x,y in a.items():
#     print('num:%s'%x,end=' ')
#     for k,v in y.items():
#         print('%s:%s'%(k,v),end=' ')
#     print()

# for k1 in a.keys():
#     print('num:%s'%k1,end=' ')
#     for k2 in a[k1].keys():
#         print('%s:%s' % (k2, a[k1][k2]), end=' ')
#     print()

'''
给所有性别为男的添加1000元工资
'''
# for k,v in a.items():
#     if v['sex']=='男':
#         v['salary']=1000
#     print(k,':',v)
