'''
os模块
rename()--重命名
remove()--删除文件
mkdir()--创建目录
rmdir()--删除目录，目录必须为空
makedirs()--创建多级目录
removedirs()--删除多级目录。若目录为空则删除，递归到上一级，若也空，删除...
getcwd()--获取当前所在目录
listdir(path)--获取目录列表
chdir(path)--切换所在目录,切换当前脚本工作目录
path.exits(path)--判断文件或文件夹是否存在
path.isfile(path)--判断是否是文件
path.isdir(path)--判断是否是目录
path.abspath(path)--获取绝对路径
path.isabs(path)--判断是否为绝对路径
path.basename(path)--获取路径中的最后部分
path.dirname(path)--获取路径中的父 目录 部分，不管最后是文件还是文件夹
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

# b=os.path.exists('E:\pywork\day13')
# print(b)

# print(os.path.isfile('extend.py'))

# print(os.path.isdir('E:\pywork\day13'))

# print(os.path.abspath('extend.py'))

# print(os.path.isabs(os.getcwd()))

# print(os.path.basename(os.getcwd()))

# print(os.path.dirname('E:\\pywork\\day08\\p1\\demox.py'))
# print(os.path.dirname('E:\\pywork\\day08\\p1\\p'))