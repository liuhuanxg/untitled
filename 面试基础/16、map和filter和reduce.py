def even(num):
    if num%2==0:
        return True
    return False
lis=[1,2,3,4,5,6,7,8]
result=filter(even,lis)  #filter只保留，返回为真的数据，过滤list的作用
print(list(result))
res=map(even,lis)
print(list(res))       #map帮助循环调用函数，这个函数返回什么就保存什么

print(5%2)    #取余
print(5//2)   #取整


#匿名函数：当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
print(list(map(lambda x:x*x,[1,2,3,4])))