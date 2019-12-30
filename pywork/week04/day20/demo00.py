# k={}
# a='k:1|k1:2|k2:3|k3:4'
# b=a.split('|')
# for i in b:
#     s=i.split(':')
#
#     k[s[0]]=s[1]
# print(k)

# 在指定文件夹查找文件
import os
def find_file_by_name(file_name,file_path):
    if not os.path.isdir(file_path):
        print('不是目录')
    else:
        file_list=os.listdir(file_path)
        for each_file in file_list:
            d=file_path+'\\'+each_file
            if each_file==file_name:
                print(d)
            elif os.path.isdir(d):
                temp=find_file_by_name(file_name,d)
                if temp:
                    return temp
find_file_by_name('aa.txt','E:\\')