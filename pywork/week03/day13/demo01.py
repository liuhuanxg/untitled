'''
文件操作
'''
# a叫做文件句柄（变量）用来操作文件
# 第一个参数是文件的路径
# 第二个参数mode=访问文件的模型，r表示读，默认就是r
# a=open('d:\\a.txt','r')
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
# a=open('d:\\a.txt','r')
# print(a.read(4))
# print(a.read(5))
# a.close()

# a=open('d:\\a.txt','r')
# b=a.readline()
# print(b)    # 空行--解析出了\n
# print(len(b))
# a.close()

# a=open('d:\\a.txt','r')
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