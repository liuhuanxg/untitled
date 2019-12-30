'''
只能用于有序的序列
折半查找
'''
# def zbcz(a,start,end,key):
#     if start>end:
#         return -1
#     middle=(start+end)//2
#     if key<a[middle]:
#         return zbcz(a,start,middle-1,key)
#     elif key>a[middle]:
#         return zbcz(a,middle+1,end,key)
#     else:
#         return middle
# a=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('请输入想要查找的数：'))
# x=zbcz(a,0,len(a)-1,k)
# if x>=0:
#     print(k, '的位置为：', x)
# else:
#     print('该序列中没有',k)

# 循环
# def zbcz(a,start,end,k):
#     while start<=end:
#         middle=(start+end)//2
#         if k>a[middle]:
#             start=middle+1
#         elif k<a[middle]:
#             end=middle-1
#         else:
#             return middle
#     return -1
# a=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('请输入想要查找的数：'))
# x=zbcz(a,0,len(a)-1,k)
# if x>=0:
#     print(k,'的位置为：',x)
# else:
#     print('该序列中没有',k)