# print('我叫{}，来自{}，今年{}岁'.format('刘欢','南阳方城',22))
# print('我叫{}，来自{}，我今年{}岁'.format('刘欢','河南省南阳市方城县',22))
# print('我叫{0},来自{1},我今年{2}岁,来北京{3}个月'.format('刘欢','河南省南阳市方城县',22,'一'))
# print('country:我在{city},{qu}区,{country}'.format(city='北京',country='中国',qu='朝阳'))
# x='身高：{height},体重:{weight}公斤，分数{score}'.format(height=177,weight=74.5,score=100)
# print(x)

# i=3
# while 0<i<=3:
#     user=input('请输入用户名:')
#     if user=='张三':
#         print('用户名输入正确')
#         break
#     else:
#         print('你还有%d次机会'%(i-1))
#     i-=1

# i=1
# while i<6:
#     age=int(input('请输入第%d个学生年龄：'%i))
#     if 16<age<20:
#         print('年龄输入有误')
#         continue
#     # 不再执行剩下的语句，但是不会跳出循环
#     i+=1

# a='ancd'
# print(a[len(a)-1])

a='asdsavcas'
# print(a[2:3])
# print(a[:-1])

# a='0123456789'
# print(a[7::3])
# print(a[::-1])
# print(a[len(a)::-1])

# 快速将一串数字反过来排列
# i=input('请输入一个数字：')
# j=str(i)
# k=j[::-1]
# print(k)

# 封装：将一串数字逆序排列
# def nixu(j):
#     k=str(j)[::-1]
#     return k
# j=input('请输入一个数字：')
# print(nixu(j))

# a='i love you beijing'
# wz=a.index('love')
# # 找第一个字符的下标
# print(wz)

# b='beijing'
# wz=b.index('jing')
# print(wz)

# index与find都是查找位置，find查找不到时返回-1，index查不到时报错
# c='nihao'
# wz=c.index('z')
# wz=c.find('z')
# print(wz)

# a='海燕，女，湖南人，本科'
# b=a.replace('海燕','小燕子')
# # replace进行替换，a的内容没有改变
# print(a)
# print(b)

# senteence='i love you beijing'
# split分割字符串，分割之后乙列表的形式存储
# x=senteence.split(' ')
# print(x)

# time='2018-9-23'
# print(time.split('-'))

# a='china xianggang'
# c=a.startswith('china')
# # startwith('a')检查字符串是不是以a开头，是的话返回true，不是返回false
# print(c)
# d=a.startswith('xianggang')
# print(d)
# b=a.startswith('zhongguo')
# print(b)
# e=a.startswith('h')
# print(e)

# x='QWER'
# # 大写字母转换成小写字母
# print(x.lower())

# a='qwert'
# # 前边空6-len(a)个空格
# print(a.rjust(6))
# print('1,2,3,4,5')
# c=a.center(10,'&')
# print(c)
# a='     12  3'
# # 去除字符串刚开始的空格
# b=a.strip()
# print(b)

# a='i love-love you'
# # 返回第二个v的下标
# b=a.rfind('v')
# print(b)
# # 把-两边用‘’分开,-仍然保留
# c=a.partition('-')
# d=a.split('-')
# print(c)
# print(d)

# a='DSAjkj'
# # 判断是否为英文，是返回true
# print(a.isalpha())
# b='99.9'
# # 判断参数是否为十进制，小数返回false
# print(b.isdigit())
# c='12asd12'
# print(c.isalnum())

# a=[1,2,7,5,7,6,9]
# # len(a)表示列表的长度
# b=sorted(a)
# print(b)
# print(len(a))
# print(a[::-1])

# a=[1,2,'a','b','c']
# i=0
# while i<len(a):
#     print(a[i],end=' ')
#     i+=1
# print('i=',i)

# a=[1,2,'a','b','c']
# # 在末尾添加一个元素
# a.append('你好')
# print(a)
# # 扩展列表，把每一个元素都分开
# a.extend('{name="张三"}')
# print(a)
# a.extend(('a','b','c'))
# print(a)

# a=[1,23,45]
# # insert插入，在2的位置上插入4
# a.insert(2,4)
# print(a)
# # 把1位置上的数改为10
# a[1]=10
# print(a)

# a=[1,2,3,4,56,7]
# for i in a :
#     if i%2==0:
#         print(i,end=' ')

# a=[1,2,3,4,56,7]
# # range前包后不包
# for i in range(len(a)):
#     print(a[i])
# print(a[1:3])

# a=[12,34,5,6]
# for i in a:
#     print(i+10)

# a=[1,2,4,5]
# # 判断一个元素在不在列表中
# x=2 in a
# print(x)
# y=3 in a
# print(y)

# a=[1,2,3,4,4]
# # 输出3的下标
# print(a.index(3))
# # 计算4的数量
# print(a.count(4))

# a=[1,2,3,4,5]
## 删除元素
# del a[0]
# del a[3]
# print(a)

# a=[1,2,3,4,5]
## 删除元素
# a.remove(3)
# print(a)

# a=[5,2,8,4]
# # 正序排列
# a.sort()
# print(a)
# print(sorted(a))

# a=[1,2,3,4,45,7,8]
# # 将元素逆序排列
# a.reverse()
# print(a)

# a=[4,56,2,3,6,8]
# # 先正序排列在逆序
# a.sort(reverse=True)
# print(a)

# l=[]
# for i in range(5):
#     for j in  range(5):
#         l.append('*'*(2*j-1))
#     print(' '*(4-i),l[i])

# i=1
# l=[]
# while i<6:
#     l.append('*'*(2*i-1))
#     print(' '*(5-i),l[i-1])
#     i+=1

# h=1
# # 先定义第一行
# while h<=5:
#     # 判断行数条件
#     k=1
#     # 定义空格
#     while k<=6-h:
#         # 判断空格个数
#         print(' ',end='')
#         # 输出空格
#         k+=1
#         # 行数加1
#     l=0
#     # 定义星号
#     while l<=8:
#         # 判断星号个数
#             print('*',end='')
#         # 输出星号
#             l+=1
#         # 换行
#     print()
#     h+=1

# a=[1,2,3,4,5]
# for i in  a:
#     print(i,end=' ')

# i=1
# while i<5:
#     print(i,end=' ')
#     i+=1
# else:print('i=',i-1)

# a=('a','b','c')
# for x in a :
#     print(x,end=' ')
# else:print('没数据了')
# print(a[0])

# a=1
# print(type(a))
# b=.0
# print(type(b))
# c=0
# print(c==b)

# b=(1)
# print(type(b))
# c=(1,2,3)
# print(type(c))

# tup=(1,'a','b','a','b','a',1,1,2,3,)
# # count计数
# print(tup.count(1))

# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(' ',end='')
#         j+=1
#     k=1
#     while k<=2*i-1:
#         print('*',end='')
#         k+=1
#     print()
#     i+=1

# for i in  range(3):
#     j=0
#     while j<3:
#         print(1, end=' ')
#         j+=1
#     k=0
#     while k<3:
#         print(2,end='')
#         k+=1

# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(' ',end='')
#         j+=1
#     k = 1
#     while k <= 2 * i - 1:
#             if k == 1 or k == 2 * i - 1 or i==5:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#             k += 1
#     print()
#     i+=1


# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print(' ',end='')
#         j+=1
#     k=1
#     while k<=2*i-1:
#         print('*',end='')
#         k+=1
#     print()
#     i+=1

# a=[[1,2,3],[2,3,4],[3,4,5]]
# for i in a:
#     for j in i:
#         print(j,end='')
#     print()


# a=[[1,2,3],[2,3,4],[3,4,5],[1,2,3,4,5,6,7]]
# # 遍历二维列表
# i=0
# while i<len(a):
#     j=a[i]
#     k = 0
#     while k<len(j):
#         print(j[k],end=' ')
#         k+=1
#     print()
#     i+=1


# a={'name':'张三','age':18,'address':'北京'}
# print(a['name'])
# a['name']='李四'
# print(a.keys())

# b=dict(name='张三',age=18,address='北京')
# # 字典的另一种格式
# # print(b)
# for i in b.keys():
#     # 遍历字典的key值
#     print(i)


# a={'name':'张三','address':'北京'}
# # items把每一组的键跟值用小括号分组,分完组之后是列表形式
# print(a.items())
# for x,y in a.items():
#     print(x,":",y)
# a['address']='上海'
# print(a)
# a['num']='001'
# # 向字典添加元素
# print(a)
# d='张三' in a
# # 测试键在不在字典中，不能测试键值
# print(d)


# c=[1,2,3,4]
# # 检查元素是否属于c中，'3'不在c中，3在
# print(3 in c)

# a={'001':{'name':'张三','age':18,'address':'北京市朝阳区'},
#    '002': {'name': '李四', 'age': 19, 'address': '山东朝阳区'},
#    '003': {'name': '王五', 'age': 20, 'address': '河北朝阳区'}
#    }
# for keys,values in a.items():
#     print(values['age'])
# print(a['001']['name'])


# a={'001':{'name':'张三','age':18,'address':'北京'},
#    '002': {'name': '李四', 'age': 19, 'address': '山东'},
#    '003': {'name': '王五', 'age': 20, 'address': '河北'},
#    '004': {'name': '王五', 'age': 20}
#    }
# for keys,value in a.items():
#    if 'address' in value and value['address']=='北京':
#       value['house']=1500
# print(a)


# a = {'001': {'name': '张三', 'age': 11, 'address': '北京'},
#      '002': {'name': '李四', 'age': 19, 'address': '山东朝阳区'},
#      '003': {'name': '王五', 'age': 20, },
#      '004': {'name': '王五', 'age': 20, 'address': '北京'}
#      }
# # 增、删、改、查、退出
# while True:
#    i = int(input('请输入要进行的操作：'))
#    if i==1:
#       id=input('请输入要添加的学生学号：')
#       if id in a:
#          print('学生已存在。')
#       else:
#          zd={}
#          zd['name']=input('请输入姓名：')
#          zd['age']=input('请输入年龄:')
#          zd['address']=input('请输入住址：')
#          a[id]=zd
#          print('学生已添加。')
#          print(a)
#    elif i==2:
#       id = str(input('请输入要删除的学生学号：'))
#       if id not in a:
#          print('学生不存在，请重新输入。')
#          continue
#       else:
#          del a[id]
#          print('学生已删除。')
#    elif i==3:
#       id = input('请输入要修改的学生学号：')
#       if id not in a:
#          print('学生不存在，请重新输入。')
#          continue
#       else:
#          a[id]['name'] = input('请输入姓名：')
#          a[id]['age'] = input('请输入年龄:')
#          a[id]['address'] = input('请输入住址：')
#    elif i==4:
#       id = str(input('请输入要查询的学生学号：'))
#       if id not in a:
#          print('学生不存在，请重新输入。')
#       else:
#          print(a[id])
#    elif i==0:
#       print('退出。')
#       break


# a = {'001': {'name': '张三', 'age': 11, 'address': '北京'},
#      '002': {'name': '李四', 'age': 19, 'address': '山东朝阳区'},
#      '003': {'name': '王五', 'age': 20, },
#      '004': {'name': '王五', 'age': 20, 'address': '北京'}
#      }
# while True:
#     i=int(input('请选择要进行的操作：1、增加。2、删除。3、修改。0、退出。:'))
#     if i==1:
#         id=input('请输入要添加的学号：')
#         if id in a :
#             print('学生已存在。')
#         else:
#             zd={}
#             zd['name']=input('请输入姓名:')
#             zd['age']=input('请输入年龄:')
#             zd['address']=input('请输入地址:')
#             a[id]=zd
#             print('a=',a)
#     elif i==2:
#         id = input('请输入要删除的学号：')
#         if  id not in a:
#             print('ID不存在。')
#             continue
#         else:
#             del a[id]
#             print(a)
#             print('学生已删除。')
#     elif i==3:
#         id = input('请输入要修改的学号：')
#         if id not in a:
#             print('ID不存在。')
#             continue
#         else:
#             a[id]['name']=input('请输入姓名:')
#             a[id]['age'] = input('请输入年龄:')
#             a[id]['address'] = input('请输入住址:')
#             print(a)
#     elif i == 0:
#         print('退出。')


# dic = {'剧情': 11, '犯罪': 10, '动作': 8, '爱情': 3, '喜剧': 2, '冒险': 2, '悬疑': 2, '惊悚': 2, '奇幻': 1}
# #通过list将字典中的keys和values转化为列表
# keys = dic.keys()
# values = list(dic.values())
# # 结果输出
# print(keys)
# print("values列表为：",end='')
# print(values)

# zd={}
# a={}
# zd['name']='张三'
# print(zd)
# zd['address']='西藏'
# print(zd)
# a['005']=zd
# print(a)

# a=[5,1,3,4,2]
# a.reverse()
# print(a)

# i=input('请输入一个数')
# b=input('请输入一个数：')
# # 交换两个数的数值
# # sum=i
# # i=b
# # b=sum
# i,b=b,i
# print(i,' ',b)

# a=[1,2,3,4,5,6,7,8]
# i=0
# j=len(a)-1
# while i<=j:
#     a[i],a[j]=a[j],a[i]
#     i+=1
#     j-=1
# # 交换位置值
# print(a)

# list=[1,6,2,5,8,3,9,4,7]
# i=1
# while i<=len(list):
#    j=0
#    while j<len(list)-i:
#       if list[j]>list[j+1]:
#          list[j],list[j+1]=list[j+1],list[j]
#       j+=1
#    i+=1
# print(list)