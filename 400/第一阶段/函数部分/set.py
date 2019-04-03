# set无序无重复，重复元素自动过滤，最后结果用{}表示，set里边包含tuple或者list或者dict。（）
# s1=set([1,2,3,4,2,3,3])  自动删除重复字符，只留第一个
# print(s1)
# s3=set({1,2,3,4})
# print(s3)
# s3.add(5)#当添加重复时，无效果,不能添加列表，列表可变
# print(s3)
# # s3.add([7,8,9])#,不能插入列表，列表可变，也不能是字典，字典也可变
# print(s3)
# s3.add((5,6,7))#可以插元组
# print(s3)
# s3.update([8,9])  #插入整个list、tuple、字符串，打碎插入
# print(s3)
# s3.update('sunck')
# print(s3)

# s4=set([1,2,3,4,5])#删除，不能用下标删除
# s4.remove(4)
# print(s4)


# s7=set([1,2,3,4,5])
# for i in s7:
#     print(i)
# for index,data in enumerate(s7):
#     print(index,data)

# s8=set([1,2,3])
# s9=set([2,3,4])
# # a1=s8&s9    #交集
# # print(a1)
# a2=s8|s9    #并集
# print(a2)

s10=set({'name':'张三','address':'李四','姓名':'王五'})
print(list(s10))