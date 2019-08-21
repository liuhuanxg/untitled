import  itertools

'''
排列和组合
'''
# 排列
# mylist=list(itertools.permutations([1,2,3,4],3))
# print(mylist)
# print(len(mylist))

#组合
# mylist=list(itertools.combinations([1,2,3,4,5],2))
# print(mylist)
# print(len(mylist))

#将列表中的数组成repeat长度的元组
mylist=list(itertools.product([0,1,2,],repeat=6))
print(mylist)
print(len(mylist))
l=[3,5,6,7,4]
print(sorted(l))