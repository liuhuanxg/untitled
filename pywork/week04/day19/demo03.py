'''
队列
'''
# a=[]
# while True:
#     bh=int(input('请输入编号：'))
#     # 入队
#     if bh == 1:
#         data=input('请输入入队数据：')
#         a.append(data)
#     # 出队
#     elif bh==2:
#         if len(a)<1:
#             print('空队列')
#         else:
#             # data=a[0]
#             # del a[0]
#             # print(data,'出队')
#             print(a.pop(0),'出队')
#     # 查看
#     elif bh==3:
#         print(a)
#     else:
#         break

'''
栈
'''
class Stack():
    def __init__(self):
        self.top=-1
        self.sList=[]
    def inStack(self):
        d=int(input('请输入入栈数据：'))
        self.top+=1
        self.sList.append(d)
    def outStack(self):
        if self.top==-1:
            print('空栈')
        else:
            d=self.sList[self.top]
            del self.sList[self.top]
            print(d,'出栈')
            self.top-=1
    def printStack(self):
        print(self.sList)
s=Stack()
while True:
    bh=int(input('请输入操作编号：'))
    if bh==1:
        s.inStack()
    elif bh==2:
        s.outStack()
    elif bh==3:
        s.printStack()
    else:
        break