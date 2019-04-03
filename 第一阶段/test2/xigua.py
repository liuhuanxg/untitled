# a=[1,2,3,4,5,6,7,8,9,10]
#
# i=0
# jbq=0
# gs0=0
# while True:
#     if a[i]!=0:
#         jbq+=1
#     if jbq==3:
#         a[i]=0
#         jbq=0
#         gs0+=1
#     if gs0==9:
#         break
#     i+=1
#     i=i%10
# i=0
# while i<len(a):
#     if a[i]!=0:
#         print('最后一个位置下标是%d'%i)
#         break
#     i+=1

a=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<5:
    t=a[0]
    j=0
    while j<9:
        a[j]=a[j+1]
        j+=1
    a[9]=t
    i+=1
print(a)