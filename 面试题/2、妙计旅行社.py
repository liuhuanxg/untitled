# print(dir('a'))

'''
a=[1,2,23,43,4]
b=[2,32,43,4,]
for i in a:
    for j in b:
        if i==j:
            print(i)
'''
'''
a='abddasfd'
print(a[::-1])
b=list(a)
b.reverse()
print(''.join(b))
print(dir(['a']))
a=[1,2,3,]
print(a.pop())
a.remove(2)
print(a)
'''


def cc(li):
    for i in li:
        if type(i)==list:
            return cc(i)
        else:print(i)
if __name__ == '__main__':
    A = [1, 2, [3, 4, ["434", [4, 5, 6]]]]
    cc(A)
print(type([1,2]))
print(type(1.2))

# a=[1,2,23,43,4]
# b=[2,32,43,4,]
# print(set(b))
# c=set(a)&set(b)
# print(c)
# print(type(c))

# def add(a,list=[]):
#     print(id(list))
#     list.append(a)
#     return list
# print(add(1))
# print(add(2))

def num(a,b=4):
    b=a+4
    return b
print(num(1))
print(num(2,3))

a=map(lambda x:x*2,[1,2,3])
print('a:',a)  #a: <map object at 0x000001FC24712358>
print(list(a)) #[2, 4, 6]
a={}
a['name']='zjhansgn'
print(a)
b={'name':'张三','age':19}
print(b)
cc=[1,2,3,4,4,4]
l=set(cc)
print(list(l))

dict1 = {'Name': 'Manni', 'Age': 7, 'Name': 'cc'}
print(dict1)
c=dict()
print(type(c))


# 异常函数
'''
a={'name':'张三'}
try:
    result = a['age']
    print(result)
except:
    print('aaa')
'''
# string='{1},{0}'
# print(string.format('hello','python'))

# A=[1,2,3,4]
# result=[i*i for i in A]
# print(result)

# L1=[1,2,3,4]
# L2=[5,6,7,8]
# L3=L1+L2
# print(L3)

# D = {'Adam': 95, 'Lisa': 85,'Bart': 59}
# # del D['Adam']
# # print(D)
# for key,value in D.items():
#     print(key,':',value)

# x=5
# print(x%3)   #2  取余
# print(x//3)   #整除


# list1 = [2, 3, 8, 4, 9, 5, 6]
# list2 = [5, 6, 10, 17, 11, 2]
# list=sorted(list(set(list1+list2)))
# print(list)

# a=1
# b=2
# a=a^b
# b=a^b
# a=a^b
# print(a,b)

# appium  和selenium

# a=[1,2,3]
# b=a
# print(b is a )
# a[0]=100
# print(b)
