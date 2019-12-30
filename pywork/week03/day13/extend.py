# dict1=[{"name":"张三","age":16},{"name":"李四","age":18},{"name":"王五","age":19}]
# dict2=[]
# getAge=lambda x:x['age']
# def func(i):
#     d=max(dict1,key=getAge)
#     dict2.append(d)
#     dict1.remove(d)
# for i in range(3):
#     func(i)
# print(dict2)

# dict1=[{"name":"张三","age":16},{"name":"李四","age":18},{"name":"王五","age":19}]
# def sort_by_age(list1):
#     return sorted(dict1,key=lambda x:x['age'],reverse=True)
# print(sort_by_age(dict1))

# a=['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']
# s=set()
# for x in a:
#     s.add(x)
# for x in s:
#     print('单词{}有{}个'.format(x,a.count(x)))

# 用mkdir实现makedirs
# import os
# a=input("请输入想要创建的多层文件，以'/'分隔：")
# lst=a.split('/')
# for i in range(len(lst)):
#     if not os.path.exists(lst[i]):
#         os.mkdir(lst[i])
#     os.chdir(lst[i])

# import os
# a=input("请输入想要创建的多层文件，以'/'分隔：")
# lst=a.split('/')
# pd=''
# for p in lst:
#     pd+=p
#     if not os.path.exists(pd):
#         os.mkdir(pd)
#     pd+='/'

# 用rmdir实现removedirs
# import os
# a=input("请输入想要删除的多级文件，以'/'分隔：")
# lst=a.split('/')
# print(a)
# for i in range(len(lst)):
#     if os.path.exists(lst[i]):
#         os.chdir(lst[i])
#     else:
#         print('不存在路径{}'.format(os.path.abspath(lst[i])))
#         break
# for i in range(len(lst)-1,-1,-1):
#     os.rmdir(lst[i])
#     os.chdir(os.path.abspath(lst[i-1]))

'''
将E:\dict.txt的内容读取，形成一个二维字典
'''
# a={}
# fp=open('E:\\dict.txt','r')
# str=fp.readline()
# while len(str)>0:
#     lst1=str.split(',')
#     lst2=[]
#     for x in lst1:
#         lst2.append(x.split(':'))
#     d = {}
#     for i in range(len(lst2)-1):
#         d[lst2[i][0]]=lst2[i][1]
#     if lst2[len(lst2)-1][1][-1]=='\n':
#         a[lst2[len(lst2)-1][1][0:-1]]=d
#     else:
#         a[lst2[len(lst2) - 1][1]] = d
#     str = fp.readline()
# print(a)
# fp.close()

# class Student():
#     @staticmethod
#     def readFormFile():
#         dzd={}
#         with open('stu.txt','r',encoding='utf-8') as f:
#             line=f.readline()
#             while len(line)>0:
#                 xzd={}
#                 if line[-1]=='\n':
#                     line=line[:-1]
#                 items=line.split(',')
#                 for item in items:
#                     ite=item.split(':')
#                     if ite[0]=='num':
#                         dzd[ite[1]]=xzd
#                     else:
#                         xzd[ite[0]]=ite[1]
#                 line=f.readline()
#         return dzd
#     @staticmethod
#     def writeFile(dzd):
#         with open('b.txt','w') as f:
#             i=1
#             for k,v in dzd.items():    # 遍历双重字典第一层
#                 for k1,v1 in v.items():    # 遍历第二层字典
#                     # 把k，v以k：v的格式写入文件
#                     f.write(k1+':'+v1+',')
#                 # 最后写入学号，并且除最后一行都换行
#                 if i==len(dzd):
#                     f.write('num:' + k)
#                 else:
#                     f.write('num:' + k + '\n')
#                 i+=1
# dzd=Student.readFormFile()
# print(dzd)
# Student.writeFile(dzd)