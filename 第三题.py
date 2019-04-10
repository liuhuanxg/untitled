import itertools

def compare(str1,str2):
    r1,flag1=check(str1)
    r2,flag2=check(str2)
    result=0
    if flag1 and flag2:
        if r1>r2:
            result=1
        elif r1<r2:
            result=-1
        elif r1==r2:
            result=0
    elif flag1 or flag2:
        if flag1:
            result=1
        elif flag2:
            result=-1
    else:
        for i in range(len(r1)):
            if r1[i]>r2[i]:
                result=1
                break
            elif r1[i]<r2[i]:
                result=-1
                break
    print(result)

def check(str):
    arr=[]
    for i in str:
        if i in first_list:
            i=10
        elif i in secon_list:
            i=1
        arr.append(int(i))
    arr=sorted(arr)
    mylist = list(itertools.permutations(arr, 3))
    for j in mylist:
        if (j[0]+j[1]+j[2])% 10 == 0:
            other_list=list(set(list(j)) & set(list(arr)))
            x=(other_list[0]+other_list[1])%10
            return x,True
    return arr,False

if __name__ == '__main__':
    first_list=['T','J','K','t','j','k','q','Q',]
    secon_list=['A','a']
    str1=input('请输入第一幅牌:')
    str2=input('请输入第一幅牌:')
    compare(str1,str2)