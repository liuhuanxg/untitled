#加上global之后可以对全局变量进行修改
#列表、字典不需要加global就可以对全局变量进行修改

a=10
def sum(c):
    c+=10
    print(c)
    global a
    a=100
    print(a)
sum(a)
print(a)


