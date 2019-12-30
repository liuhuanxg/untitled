# 括号匹配
# dict={'(':')','{':'}','[':']'}
# class Stack():
#     def __init__(self):
#         self.top=-1
#         self.sList=[]
#     def inStack(self,z):
#         self.top+=1
#         self.sList.append(z)
#     def outStack(self,y):
#         if dict[self.sList[self.top]]==y:
#             del self.sList[self.top]
#             self.top -= 1
#         elif dict[self.sList[self.top]]!=y:
#             print('括号不匹配')
#             exit()
#     def pd(self,kh):
#         if len(kh)%2==1:
#             print('匹配失败')
#             exit()
#         for i in range(len(kh)):
#             if kh[i] in dict.keys():
#                 self.inStack(kh[i])
#             else:
#                 self.outStack(kh[i])
#         if self.top == -1:
#             print('匹配成功')
# kh=(input('请输入：'))
# s=Stack()
# s.pd(kh)

# 进制转换
class Stack():
    def __init__(self):
        self.top=-1
        self.sList=[]
    def inStack(self,data):
        self.top += 1
        self.sList.append(data)
    def outStack(self):
        while self.top>-1:
            data=self.sList[self.top]
            del self.sList[self.top]
            print(data,end='')
            self.top -= 1
s=Stack()
num=int(input('请输入一个十进制数：'))
while num!=0:
    s.inStack(num%2)
    num//=2
s.outStack()