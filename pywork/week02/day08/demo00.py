# a='1234'
# print(a.startswith('1'))
# print(a.endswith('4'))

# s='123'
# print(dir(s))
# print(dir(str))
#
# print(help(str.replace))
# print(help(s.replace))

def extendlist(val,lis=[]):
    lis.append(val)
    # print("lis:", lis)
    return lis
list1=extendlist(10)
list2=extendlist(123,[])
list3=extendlist('a')
print(list1)
print(list2)
print(list3)
list3.append(6666)
extendlist(999)
print(list3)