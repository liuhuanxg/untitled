import copy
# a=[1,2,3,4,5,1,2,3,4,7]
# b=[1,2,3]
# c=copy.copy(a)
# for x in c:
#     if x in b:
#         a.remove(x)
# print(a)

a=[1,2,3,4,5,1,1,2,3,2,3,1,1]
i=0
while i<len(a):
    j=i+1
    while j<len(a):
        if a[j]==a[i]:
            for k in range(j+1,len(a)):
                a[k-1]=a[k]
            del a[len(a)-1]
            j-=1
        j+=1
    i+=1
print(a)