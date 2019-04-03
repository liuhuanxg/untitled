#字符串常见操作和函数
str1='kkJHGse'
print(dir(str1))
print(str1)    #KkJHGse
print(str.capitalize(str1))
#Kkjhgse    将第一个字符转换为大写（如果第一个字符不是字母则不转化），其余字母转化为小写

print(str1.center(9))      #位于15个字符中间，两端用空格补充
print(str1.count('k'))     #2
print(str1.encode())       #b'kkJHGse'
print(str1.endswith('e'))  #True
print(str1.find('k'))      #返回第一个k的下标   找不到会返回-1
print(str1.index('k'))     #index找不到会报错
print(str1.rfind('k'))     #从右向左查，返回第一个k的下标   找不到会返回-1
print(str1.rindex('k'))    #从右向左查，index找不到会报错

print(str1.isalnum())  #True  至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
print(str1.isdigit())  #False  只包含数字则返回 True 否则返回 False
print(str1.isalpha())  #True  至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
str2='00Flase'
print(str1.islower())      #False   所有字符都为英文且小写为True，否则为False
print(str2.isupper())      #False   所有字符都为英文且大写为True，否则为False
print(str2.isnumeric())    #False   所有字符都为数字字符True，否则为False
print(str2.istitle())      #True   第一个字母为（T或F）则返回 True，否则返回 False
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')


str3='  123,qqq'
str4=','.join(str3)
print(str4)         # , ,1,2,3,,,q,q,q   join拼接字符串
print(str3.lstrip())  #123,qqq删除左边的空格
print(str3.maketrans({'q':'c'}))   #{113: 'c'}
print(max(str3))    #q    返回字符串中ascii码最大的字符

