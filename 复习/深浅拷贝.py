import copy




#生成器，减少内存占用，不需要的数据先存储，需要时再调用

'''
def cc.txt():
    b={}
    for i in range(3):
        b['name']=i
        yield b
c=cc.txt()
print(type(c))
j=0
for i in c:
    if j==0:
        print(i)
    j+=1
'''