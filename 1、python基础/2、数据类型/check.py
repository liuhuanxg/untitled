#[1,2,3,4]
# def check(list1):
#     j=0
#     k=0
#     m=0
#     for i in range(len(list1)-1):
#         if list1[i]+1 == list1[i+1]:
#             j += 1
#             if i==len(list1)-2 and list1[i+1] <1000:
#                 j-=1
#             if i==len(list1)-2:
#                 if j>k:
#                     j,k=0,j
#         else:
#             if j>k:
#                 j,k=0,j
#
#     return k
#
# if __name__ == '__main__':
#     list1=[1,3,5,7,8,998,999,1000]
#     k=check(list1)
#     print(k)
import datetime
print(datetime.datetime.now())