# def Panduan(a,t):
#     i=0
#     while i <len(a)-1:
#         j=i+1
#         while j<=len(a)-1:
#             if a[i]+a[j]==t:
#                 return True
#             j += 1
#         i+=1
#     else:return False


# def Chachong(str):
#     i=0
#     while i <len(str)-1:
#         j=i+1
#         while j<=len(str)-1:
#             if str[i]==str[j]:
#                 return j
#             j += 1
#         i+=1
#     else:return False

def sum(a):
    list1=[]
    i = 0
    while i<len(a)-3:
        j=i+1
        while j<len(a)-2:
            k = i + 2
            while k<=len(a)-1:
                if a[i]+a[j]+a[k]==0 :
                    tuple=(a[i],a[j],a[k])
                    if tuple not  in list1:
                        list1.append(tuple)
                k+=1
            j += 1
        i+=1
    return list1
if __name__ == '__main__':
#     # a=[1,3,2,9,6,]
    # t=10
    # print(Panduan(a,t))

    # str="abcd"
    # print(Chachong(str))

    list=[-1,0,1,2,-1,-4]
    list.sort()
    print(sum(list))