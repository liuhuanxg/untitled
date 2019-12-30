# Python 0715 吕佳
# 进程间传输，线程间传输
# from multiprocessing import Process,Queue
# from threading import Thread
# import queue,time
# def aa(xcq):
#     a=[1,2,3]
#     for x in a:
#         xcq.put(x)
#         time.sleep(1)
# def ab(xcq,jcq):
#     for i in range(3):
#         jcq.put(xcq.get())
# def A(jcq):
#     xcq=queue.Queue()
#     t1=Thread(target=aa,args=(xcq,))
#     t2=Thread(target=ab,args=(xcq,jcq))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# def ba(xcq):
#     for i in range(3):
#         print(xcq.get())
# def bb(xcq,jcq):
#     for i in range(3):
#         xcq.put(jcq.get())
# def B(jcq):
#     xcq=queue.Queue()
#     t1=Thread(target=bb,args=(xcq,jcq))
#     t2=Thread(target=ba,args=(xcq,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
# if __name__ == '__main__':
#     jcq=Queue()
#     p1=Process(target=A,args=(jcq,))
#     p2=Process(target=B,args=(jcq,))
#     p1.start()
#     p2.start()

'''
队列
'''
# a=[]
# while True:
#     bh=int(input('请输入编号：'))
#     # 入队
#     if bh==1:
#         data=input('请输入入队数据：')
#         a.append(data)
#     # 出队
#     elif bh==2:
#         if len(a)<1:
#             print('空队列')
#         else:
#             print(a.pop(0),'出队')
#     # 查看
#     elif bh==3:
#         print(a)
#     else:
#         break

'''
栈
'''
# class Stack():
#     def __init__(self):
#         self.top=-1
#         self.sList=[]
#     def inStack(self):
#         d=int(input('请输入入栈数据：'))
#         self.top+=1
#         self.sList.append(d)
#     def outStack(self):
#         if self.top==-1:
#             print('空栈')
#         else:
#             d=self.sList[self.top]
#             del self.sList[self.top]
#             print(d,'出栈')
#             self.top-=1
#     def printStack(self):
#         print(self.sList)
# s=Stack()
# while True:
#     bh=int(input('请输入操作编号：'))
#     if bh==1:
#         s.inStack()
#     elif bh==2:
#         s.outStack()
#     elif bh==3:
#         s.printStack()
#     else:
#         break

# 栈的应用--括号匹配
# dict={'(':')','[':']','{':'}'}
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
#             self.top-=1
#         else:
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
#         if self.top==-1:
#             print('匹配成功')
# kh=input('请输入：')
# s=Stack()
# s.pd(kh)

# 栈的应用--进制转换
# class Stack():
#     def __init__(self):
#         self.top=-1
#         self.sList=[]
#     def inStack(self,data):
#         self.top+=1
#         self.sList.append(data)
#     def outStack(self):
#         while self.top>-1:
#             data=self.sList[self.top]
#             del self.sList[self.top]
#             print(data,end='')
#             self.top-=1
# s=Stack()
# num=int(input('请输入一个十进制数：'))
# while num!=0:
#     s.inStack(num%2)
#     num//=2
# s.outStack()