#1、列表的基础操作和函数
list=[1,3,5,4,9]
# print(dir(list))
list.append(10)
print(list)

list.insert(3,2)
print(list)

print(list.index(9))   #5  如果有多个会先返回第一个的下标
list.clear()   #清除
print(dir(list))

list1=[2,3,4,5,9,7,10]
# list1.reverse()
# print(list1)

i=list1.pop(2)
#     用pop删除的可以进行赋值操作，remove删除的不能进行赋值操作，pop写的是下标，remove删除的是内容
print(list1)   #    [2, 3, 5, 9, 7, 10]
list1.remove(2)
print(list1)   #  [3, 5, 9, 7, 10]
print(i)    #  4

list1.sort()
#sort是一种操作，对原列表进行操作，sorted可以对排完序的列表进行赋值  默认升序，reverse默认False，True时倒序
print(list1)    #[3, 5, 7, 9, 10]
list3=[3,5,4,7,10,13]
list2=sorted(list3,reverse=True)
print(list2)    #[13, 10, 7, 5, 4, 3]
print(list2.count(3))   #1

str1=''