#0,1,1,2,3,5,8,13


def fab(max):
    if max==1:
        return 0
    elif max>1:
        a,b,n=0,1,1
        while n<max:
            s=b
            a,b=b,a+b
            n+=1
        return s
max=int(input('请输入一个整数：'))
print(fab(max))


'''
def fab(max):
    n ,a ,b=0,0,1
    while n<max:
        s=b
        a,b=b,a+b
        n=n+1
    print(b)
fab(20)
'''

'''
def fab(max):
    n,a,b=0,0,1
    L=[]
    while n<max:
        L.append(b)
        a,b=b,a+b
        n=n+1
    return  L
max=int(input('请输入一个数：'))
print(fab(max))
'''

# def fab(max):
#     n,a,b=0,0,1
#     while n<max:
#         yield b
#         a,b=b,a+b
#         n=n+1
# f=fab(5)
# print(next(f))

