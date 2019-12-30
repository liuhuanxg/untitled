# 链式存储表示
class Node():
    i=0
    def __init__(self,data):
        self.data=data
        self.next=None
        Node.i+=1
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)

a.next=b
b.next=c
c.next=d
d.next=e


# 删除最后一个
# p=a
# q=a.next
# while True:
#     if q.next==None:
#         p.next=None
#         break
#     p=p.next
#     q=q.next
# x=a
# while x!=None:
#     print(x.data)
#     x=x.next

# 删除指定位置
# while Node.i!=0:
#     n=int(input('请输入您要删除的位置：'))
#     if n==1:
#         a=a.next
#         Node.i-=1
#     elif n==Node.i:
#         p = a
#         q = a.next
#         while True:
#             if q.next == None:
#                 p.next = None
#                 break
#             p = p.next
#             q = q.next
#         Node.i -= 1
#     elif 1<n<=Node.i:
#         p=a
#         i=1
#         while i<n-1:
#             p=p.next
#             i+=1
#         q=p.next.next
#         p.next=q
#         Node.i -= 1
#     else:
#         print('超出范围，错误')
#     x=a
#     while x!=None:
#         print(x.data)
#         x=x.next

# 插入指定位置
# while True:
#     num=int(input('请输入想要插入的值：'))
#     f=Node(num)
#     n=int(input('请输入您要插入的位置：'))
#     if n==1:
#         f.next=a
#         a=f
#     elif n==Node.i+1:
#         x = a
#         while x.next!=None:
#             x=x.next
#         x.next=f
#     elif 1<n<=Node.i:
#         p=a
#         i=1
#         while i<n-1:
#             p=p.next
#             i+=1
#         q=p.next
#         f.next=q
#         p.next=f
#     else:
#         print('超出范围，错误')
#     x=a
#     while x!=None:
#         print(x.data)
#         x=x.next

# 倒序
# p=a
# q=a.next
# while q!=None:
#     r = q.next
#     q.next = p
#     p = q
#     q = r
# a.next=None
# x=p
# while x!=None:
#     print(x.data)
#     x=x.next