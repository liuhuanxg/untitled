#python关键字列表
import keyword
print(keyword.kwlist)

#chr()函数--将一个整数转换为一个字符   ASCII
a=int(input('请输入一个整数：'))
print(chr(a))

#输入一个大写字母，判断这个大写字母是字母表中第几个字母
a=input('请输入一个大写字母：')
print(ord(a)-65+1)      #ord()函数--参数为字符，返回值为它对应的ASCII码值