# from multiprocessing import Process,Queue
# from threading import Thread
# import queue,time
# def aa(xcq):
#     a = [1, 2, 3]
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
# def bb(jcq,xcq):
#     for i in range(3):
#         xcq.put(jcq.get())
# def B(jcq):
#     xcq = queue.Queue()
#     t1=Thread(target=bb,args=(jcq,xcq))
#     t2=Thread(target=ba,args=(xcq,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# if __name__ == '__main__':
#     jcq=Queue()
#     p1=Process(target=A,args=(jcq,))
#     p2=Process(target=B,args=(jcq,))
#     p1.start()
#     p2.start()

# class A():
#     x=1
# class B(A):
#     pass
# class C(A):
#     pass
# print(A.x,B.x,C.x)
# B.x=2
# print(A.x,B.x,C.x)
# A.x=3
# print(A.x,B.x,C.x)

# a=[1,2,3,4,5,6,7,8,9,10]
# print(sum([i+3 for i in a[::2]]))

# 括号匹配--栈
# class Stack():
#     def __init__(self):
#         self.top=-1
#         self.sList=[]
#     def inStack(self,data):
#         self.top+=1
#         self.sList.append(data)
#     def outStack(self):
#         if self.top==-1:
#             return -1
#         else:
#             d=self.sList[self.top]
#             del self.sList[self.top]
#             self.top-=1
#             return d
#     def length(self):
#         return self.top+1
# zfc=input('请输入括号字符串：')
# s=Stack()
# pipei=True
# for zm in zfc:
#     if zm=='(' or zm=='[' or zm=='{':
#         s.inStack(zm)
#     elif zm==')':
#         d=s.outStack()
#         if d==-1:
#             print('缺少',zm,'匹配的左括号(')
#             pipei=False
#             break
#         elif d!='(':
#             print('括号不匹配',zm,d)
#             pipei=False
#             break
#     elif zm==']':
#         d=s.outStack()
#         if d==-1:
#             print('缺少',zm,'匹配的左括号[')
#             pipei=False
#             break
#         elif d!='[':
#             print('括号不匹配',zm,d)
#             pipei=False
#             break
#     elif zm=='}':
#         d=s.outStack()
#         if d==-1:
#             print('缺少',zm,'匹配的左括号{')
#             pipei=False
#             break
#         elif d!='{':
#             print('括号不匹配',zm,d)
#             pipei=False
#             break
# if pipei==True:
#     if s.length()!=0:
#         print('左括号多')
#     else:
#         print('匹配成功')