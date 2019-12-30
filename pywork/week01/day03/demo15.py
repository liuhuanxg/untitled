# a=(1,2,3,4,5,6,7,8,9,10,14)
# gs=0
# for x in a:
#     if x%7==0 or x%10==7:
#         gs+=1
#         print(x)
# print('共',gs,'个')

# a=(1,2,3,4,5,6,7,8,9,10,14)
# js=0
# os=0
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         os+=1
#     else:
#         js+=1
#     i+=1
# print('奇数有：',js,'个；偶数有：',os,'个')

a=(1,2,3,4,5,6,7,8,9,10,14)
js=0
os=0
for x in a:
    if x%2==0:
        os+=1
    else:
        js+=1
print('奇数有：',js,'个；偶数有：',os,'个')