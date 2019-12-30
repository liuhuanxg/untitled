'''
模块搜索路径
搜索顺序：
1.当前目录
2.搜索在shell变量pythonPATH下的每个目录，由sys模块的sys.path方法来规定
'''
import sys
print(sys.path)
sys.path.append('E:\\pywork\\day01')
print(sys.path)
import ex
print(ex.sum(1,2))