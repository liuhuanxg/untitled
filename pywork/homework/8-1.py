# Python 0715 吕佳
'''
文件操作
'''
# a叫做文件句柄（变量）用来操作文件
# 第一个惨呼是文件的路径
# 第二个参数mode=访问文件的模型，r表示读，默认就是r
# a=open('D:\\a.txt','r')
# b=a.read()
# print(b)
# a.close()

'''
读操作
read()--会一次性读取文件的全部内容。可加size参数，规定一次最多读取的size个字节。
readline()--每次读取一行，并且自带换行功能，每一行末尾会读到\n。也可加size参数。
readlines()--一次性以行的形式读取文件的所有内容，并返回一个list（包括\n），需要遍历读出。
循环读取--file句柄是一个可迭代的对象，因此可以循环读取文件中的内容，每次读一行。
'''
# a=open('D:\\a.txt','r')
# print(a.read(4))
# print(a.read(5))
# a.close()

# a=open('D:\\a.txt','r')
# b=a.readline()
# print(b)
# print(len(b))
# a.close()

# a=open('D:\\a.txt','r')
# b=a.readline()
# while len(b)>0:
#     print(b)
#     b=a.readline()
# a.close()

# a=open('d:\\a.txt','r')
# b=a.readlines()
# print(b)
# for x in b:
#     print(x)
# a.close()

# for x in open('d:\\a.txt','r'):
#     print(x)

'''
写操作
write()--打开一个问价用于写入。若文件存在，打开，并删除原内容，从头进行编辑；若不存在，创建新文件。
writelines()--把参数中的内容全部写入文件中（多行一次性写入）。
'''
# a=open('d:\\a.txt','w')
# a.write('我爱北京天安门')
# a.close()

# ls=['aa','b\n','cc']
# a=open('d:\\a.txt','w')
# a.writelines(ls)
# a.close()

'''
with--使用with方式操作文件，可以不用关闭文件，会自动关闭
'''
# with open('d:\\a.txt','r')as f:
#     b=f.read()
#     print(b)

'''
指定文件格式
向文件中保存内容
'''
# with open('a.txt','w',encoding='utf-8') as p:
#     p.write('你好呀')

'''
os模块
'''
import os
# os.rename('a.txt','b.txt')

# os.remove('b.txt')

# os.mkdir('x')

# os.rmdir('x')

# os.makedirs('a/a/a')

# os.removedirs('a/a/a')

# print(os.getcwd())

# print(os.listdir(os.getcwd()))

# os.chdir('E:\\')
# print(os.getcwd())

# b=os.path.exists('E:\\pywork\\day13')
# print(b)

# print(os.path.isfile('7-31.py'))

# print(os.path.isdir('E:\\pywork\\day13'))

# print(os.path.abspath('7-31.py'))

# print(os.path.isabs(os.getcwd()))

# print(os.path.basename(os.getcwd()))

# print(os.path.dirname('E:\\pywork\\day08\\p1\\demox.py'))
# print(os.path.dirname('E:\\pywork\\day08\\p1\\p'))

'''
异常
'''
# while True:
#     try:
#         a=eval(input('请输入表达式：'))
#         print(a)
#     except ZeroDivisionError as e:
#         print('除数为0，错误！')
#         print(e)
#         break

# try:
#     a=[1,2,3]
#     print(a[3])
#     print(3/0)
# except IndexError as i:
#     print(i)
# except ZeroDivisionError as e:
#     print(e)
# print('结束')

# try:
#     a=[1,2,3]
#     print(a[2])
#     print(3/0)
# except (IndexError,ZeroDivisionError) as e:
#     print(e)
# print('结束')

# try:
#     a=[1,2,3]
#     print(a[1])
# except Exception as i:
#     print(i)
# else:
#     print('异常')
# print('结束')

# try:
#     a=[1,2,3]
#     print(a[1])
#     print(1/0)
# except Exception as f:
#     print(f)
# print('结束')

# try:
#     a=[1,2,3]
#     print(a[3])
# except Exception as f:
#     print(f)
# else:
#     print('无异常')
# finally:
#     print('无论有没有错误，我都会执行')

# while True:
#     name=input('请输入姓名：')
#     try:
#         if len(name)<2:
#             raise Exception('错误')
#     except Exception as f:
#         print(f)
#         break

# class MyExcept(Exception):
#     def __init__(self,xx):
#         self.xx=xx
#     def __str__(self):
#         return self.xx
# try:
#     raise MyExcept('天上下雨了')
# except MyExcept as f:
#     print(f)

# class ShortException(Exception):
#     def __init__(self,length,at_least_len):
#         self.length=length
#         self.at_least_len=at_least_len
#     def __str__(self):
#         return '您输入了{}个字符，最少需要{}个字符'.format(self.length,self.at_least_len)
# t=input('请输入字符串：')
# try:
#     if len(t)<15:
#         raise ShortException(len(t),15)
# except ShortException as f:
#     print(f)

# class A():
#     pass
# A.x=99
# print(A.x)
# a=A()
# print(a.x)
# print(id(a.x))
# print(id(A.x))

# class A():
#     def __new__(cls, *args, **kwargs):
#         cls.xIns=object.__new__(cls)
#         return cls.xIns
#     def __init__(self,name):
#         self.name=name
# zs=A('张三')
# print(zs.name)
# print(A.xIns.name)
# ls=A('李四')
# print(A.xIns.name)
# print(zs.name)
# print(zs is ls)

# class A():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'xIns'):
#             cls.xIns=object.__new__(cls)
#         return cls.xIns
#     def __init__(self,name):
#         self.name=name
# zs=A('张三')
# print(A.xIns.name)
# ls=A('李四')
# print(A.xIns.name)
# print(zs.name)
# print(zs is ls)

# class Bwm():
#     def run(self):
#         print('宝马在跑')
# class Benc():
#     def run(self):
#         print('奔驰在跑')
# class Audi():
#     def run(self):
#         print('奥迪在跑')
# class Factory():
#     @staticmethod
#     def makeCar(name):
#         if name=='宝马':
#             return Bwm()
#         elif name=='奔驰':
#             return Benc()
#         elif name=='奥迪':
#             return Audi()
# a=Factory.makeCar('宝马')
# b=Factory.makeCar('奔驰')
# c=Factory.makeCar('奥迪')
# a.run()
# b.run()
# c.run()

# class Boss():
#     def __init__(self):
#         self.obsevers=[]
#         self.status=''
#     def attach(self,ob):
#         self.obsevers.append(ob)
#     def notify(self):
#         for ob in self.obsevers:
#             ob.update()
# class Employee():
#     def __init__(self,name,boss):
#         self.name=name
#         self.boss=boss
#     def update(self):
#         print('{}，{}赶快工作'.format(self.boss.status,self.name))
# if __name__=='__main__':
#     ljc=Boss()
#     zs=Employee('张三',ljc)
#     ls=Employee('李四',ljc)
#     ljc.attach(zs)
#     ljc.attach(ls)
#
#     ljc.status='李嘉诚回来了'
#     ljc.notify()

# class CashNorm():
#     def accept_money(self,money):
#         return money
# class Cash_rate():
#     def __init__(self,rate):
#         self.rate=rate
#     def accept_money(self,money):
#         return self.rate*money
# class Cash_condition():
#     def __init__(self,condition,ret):
#         self.condition=condition
#         self.ret=ret
#     def accept_money(self,money):
#         if money<self.condition:
#             return money
#         else:
#             return money-money//self.condition*self.ret
# class Context():
#     def __init__(self,style):
#         self.style=style
#     def getResult(self,money):
#         return self.style.accept_money(money)
# if __name__=='__main__':
#     a={}
#     a[0]=Context(CashNorm())
#     a[1]=Context(Cash_rate(0.8))
#     a[2]=Context(Cash_condition(300,50))
#     style=int(input('请输入优惠方式：'))
#     if style>2:
#         style=0
#     money=float(input('请输入金额：'))
#     print(a[style].getResult(money))

# ---------------------------------------------------
# 作业题
# 魔术方法 __del__练习
# class ReadFile():
#     def __init__(self,filename):
#         self.fp=open(filename,'r')
#     def read(self):
#         return self.fp.read()
#     def __del__(self):
#         print('关闭文件操作')
#         self.fp.close()
# import os
# one=ReadFile(os.getcwd()+'\\aa.txt')
# txt=one.read()
# print(txt)

# 生成器练习
# def read_file(fpath):
#     BLOCK_SIZE=6
#     with open(fpath,'r') as f:
#         while True:
#             block=f.read(BLOCK_SIZE)
#             if block:
#                 yield block
#             else:
#                 return
# import os
# g=read_file(os.getcwd()+'\\aa.txt')
# for content in g:
#     print(content)

# 自定义创建目录方法
# import os
# def mkdirs(path):
#     file_lst=path.split('/')
#     for file in file_lst:
#         if not os.path.exists(file):
#             os.mkdir(file)
#         os.chdir(file)
# if __name__=='__main__':
#     path=input('请输入路径：')
#     mkdirs(path)

# 练习递归
# 用户输入文件名以及开始搜索的路径，搜索该文件是否存在，如遇到文件夹，则进入文件夹继续搜索
# import os
# import sys
# sys.setrecursionlimit(1000)
# def file_find(file_path,file_name):
#     if os.path.isdir(file_path):
#         file_list=os.listdir(file_path)
#         for each in file_list:
#             temp_dir=file_path+os.sep+each
#             if os.path.isdir(temp_dir):
#                 temp=file_find(temp_dir,file_name)
#                 if temp==True:
#                     return True
#             elif os.path.isfile(temp_dir) and each==file_name:
#                 return True
#         return False
#     else:
#         print('{}不是一个目录'.format(file_path))
# print(file_find(os.getcwd(),'aa.txt'))

# 练习递归

# 通过给定的文件夹, 列举出这个文件夹当中, 所有的文件,以及文件夹, 子文件夹当中的所有文件
# def listFilesToTxt(dir,file):
#     file_list=os.listdir(dir)
#     for file_name in file_list:
#         new_filename=dir+'/'+file_name
#         if os.path.isdir(new_filename):
#             file.write(new_filename+'\n')
#             listFilesToTxt(new_filename,file)
#         else:
#             file.write('\t'+file_name+'\n')
#     file.write('\n')
# f=open(os.getcwd()+'\\list.txt','a',encoding='utf-8')
# listFilesToTxt(os.getcwd()+'\\dir',f)

"""
1、定义一个函数func(filename) filename:文件的路径，
  函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。
"""
# import os
# def func1(filename):
#     try:
#         fil=open(filename)
#     except Exception as err:
#         print(err)
#     else:
#         print(fil.read())
#         fil.close()
# func1(os.getcwd()+'\\aa.txt')

# 2、编写一个计算减法的方法，当第一个数小于第二个数时，抛出“被减数不能小于减数"的异常
# def jianfa(a,b):
#     if a<b:
#         raise BaseException('被减数不能小于减数')
#     else:
#         return a-b
# print(jianfa(1,3))

# 3、定义一个函数func(listinfo) listinfo:为列表，listinfo = [133, 88, 24, 33, 232, 44, 11, 44]，
# 返回列表小于100，且为偶数的数
def func(listinfo):
    for x in listinfo:
        try:
            result=list(filter(lambda k:k<100 and k%2==0,listinfo))
        except Exception as a:
            return a
        else:
            return result
print(func([133,88,24,33,232,44,11,44]))