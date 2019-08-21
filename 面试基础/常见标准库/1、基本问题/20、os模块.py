import os

result=os.getcwd()   #获取当前工作目录
print(result)

# os.chdir(r'E:\PYTHON')
# result=os.getcwd()   #获取当前工作目录
# print(result)

# result=os.listdir(r'E:\PYTHON\untitled\面试基础')  #获取路径的所有文件列表
# print(result)

# os.mkdir('girls')   #创建空文件夹
os.mkdir('boys',0o777)
# os.makedirs('home/vc/ss')   #循环创建文件夹
# os.removedirs('home/vc/ss')  #循环删除空文件夹
# os.rename('home','HOME')     #文件夹重命名

# result=os.stat(r'E:\PYTHON\untitled\面试基础\10、装饰器.py')   #获取文件或文件夹信息
# print(result)

# result=os.system('ls -al')  #获取隐藏文件
# print(result)

# result=os.getenv('PATH')   #获取系统的环境变量
# print(result.split((';')))

#putenv() 将一个目录添加到环境变量中(临时增加仅对当前脚本有效)
#os.putenv('PATH','/home/sy/下载')
#os.system('syls')

print(os.curdir)  #表示当前os.pardir文件夹
print(os.pardir)  #表示上一层文件夹
print(os.name)    #获取操作系统的名字 nt代表windows，posix代表linux或者unix

print(os.sep)   #获取系统路径间隔符号  windows \,linux /

print(os.extsep)   #获取文件名称和后缀的间隔符号，test.txt的 .
print(repr(os.linesep))  #获取操作系统的换行符  windows -> \r\n，linux-> \n

print('-----------------os.path子模块的内容---------------------')

# path='/boys'
# result=os.path.abspath(path)   #将相对路径转换为绝对路径
# print(result)

result=os.getcwd()
result=os.path.dirname(result)   #E:\PYTHON\untitled 获取完整路径的目录部分
print(result)

result=os.path.basename(result)   #untitled  获取最后的目录部分
print(result)

path='/home/sy/boys'
result=os.path.split(path)  #('/home/sy', 'boys') 将一个完整路径切割成目录部分和主体部分
print(result)

var1=r'\home\sy'
var2='000.py'
result=os.path.join(var1,var2)   #将两个路径合并成一个
print(result)

path='/home/sy/000.py'
result=os.path.splitext(path)   #将一个路径切割成文件后缀和其他两个部分，只要用于获取文件的后缀名
print(result)

path=r'E:\PYTHON\untitled\面试基础\10、装饰器.py'
result=os.path.getsize(path)   #获取文件的字节数
print(result)

path=r'E:\PYTHON\untitled\面试基础\10、装饰器.py'
result=os.path.isfile(path)  #检测是否是文件
print(result)

result=os.path.isdir(path)  #检测是否是文件夹
print(result)

path = '/initrd.img.old'
result=os.path.islink(path)  #检测是否是链接
print(result)

import time

filepath = r'E:\PYTHON\untitled\面试基础\19、十大排序.py'

result = os.path.getctime(filepath)  #获取文件的创建时间
print(time.ctime(result))   #把秒时间转为日期

result=os.path.getmtime(filepath)   #获取文件的修改时间
print(time.ctime(result))

result=os.path.getatime(filepath)   #获取文件的访问时间
print(time.ctime(result))

filepath = '/home/sy/下载/chls'
result = os.path.exists(filepath)  #检测某个路径是否真实存在
print(result)

path='/boys'
result=os.path.isabs(path)   #检测一个路径是否是绝对路径
print(result)

path1 = r'E:\PYTHON\untitled\面试基础\19、十大排序.py'
path2 = r'19、十大排序.py'
result = os.path.samefile(path1,path2)    #判断2个路径是否是同一个文件
print(result)

