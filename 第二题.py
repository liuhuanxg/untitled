c_list1=['十','百','千','万','亿']
dict1={'十':[2,6],'百':[3,7],'千':[4,8],'万':[5],'亿':[9]}
#测试案例：1 10 11 111 1111
#-1 -10 11 111 1111
"""
注意事项：
1、零与十、百、千、万、连续存在时需去掉
2、分段处理的段长
"""
def check(date):
    pass
def str_to_cn(data):
   list1= []
   flag = True
   list2 = []
   l=len(data)
   for i in data:
       r = change(i)
       list2.append(r)
   if list2[0] == '负':
       list2.remove(list2[0])
       flag=False
   l = len(list2)
   list3=list2[::-1]
   list4=[]
   print(list3)
   for i in list3:
       for key,val in dict1.items():
           if list3.index(i)+1 in val:
               list4.append(i+key)
   print(list4)
   # if l <=5:
   #     for i in range(1,l+1):
   #         until=''
   #         if i-2>=0:
   #             until=c_list1[i - 2]
   #         str2 = list3[i-1] +until
   #         list1.append(str2)
   # print(list1[::-1])
   # if 5<l<=8:
   #     pass
   # if l > 1 and list1[0].startswith("一十"):
   #      list1.remove(list1[0][0])
   # if list1[-1] == "零":
   #     list1.remove(list1[-1][-1])
   if flag:
       print(list1)
   else:
       print("负"+list1)


def change(i):
    if i == '0':
        result = '零'
    elif i == '1':
        result = '一'
    elif i == '2':
        result = '二'
    elif i == '3':
        result = '三'
    elif i == '4':
        result = '四'
    elif i == '5':
        result = '五'
    elif i == '6':
        result = '六'
    elif i == '7':
        result = '七'
    elif i == '8':
        result = '八'
    elif i == '9':
        result = '九'
    elif i=="-":
        result = '负'
    else:
        result=""
    return result


if __name__ == '__main__':
    data=input('请输入数字:')
    str_to_cn(data)
