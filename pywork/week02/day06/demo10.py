# 字典和字典之间不能比较
# 可以根据name/age的值进行比较，返回商品信息
lst=[{'name':'Tom','age':19},{'name':'jerry','age':29},{'name':'mary','age':39}]
def getAge(x):
    return x['age']
b=max(lst,key=getAge)
print(b)

# a=[-1,-3,-2,-5,-4]
# # 升序排序
# a.sort()
# print(a)
# # 按照绝对值，升序排序
# a.sort(key=abs)
# print(a)