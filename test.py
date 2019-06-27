c_list1=['十','百','千','万','亿']
#测试案例：1 10 11 111 1111
#-1 -10 11 111 1111
"""
注意事项：
1、零与十、百、千、万、连续存在时需去掉
2、分段处理的段长
"""

def str_to_cn(data):
   str = ""
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
   print(list3)
   if l <=5:
       for i in range(1,l+1):
           until=''
           if i-2>=0:
               until=c_list1[i - 2]
           str2 = list3[i-1] +until
           str = str2 +str
   if l > 1 and str[0] == "一" and str[1] =="十":
        str = str[1:]
   if str[-1] == "零":
       str = str[:-1]
   if flag:
       print(str)
   else:
       print("负"+str)


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
    return result


if __name__ == '__main__':
    data=input('请输入数字:')
    str_to_cn(data)
