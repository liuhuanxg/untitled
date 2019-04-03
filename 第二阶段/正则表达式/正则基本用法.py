import re

'''
\d    匹配一个数字；等价于  [0-9]
\D    匹配除数字以外的任何一个字符；等价于[^0-9]
\w    匹配一个英文字母、数字、下划线或汉字；等价于[0-9a-zA-z汉字]
\W    匹配除英文字母、数字、下划线或汉字之外的字符；等价于[^0-9a-zA-z汉字]
\s    匹配一个空白字符（可以为空格）：等价于[\f\n\r\t\v]
\S    匹配一个非空白字符（可以为空格）：等价于[^\f\n\r\t\v]
\f    匹配一个换页符等价于  \x0c或\cL
\n    匹配一个换行符；等价于  \x0a或\cJ
\r    匹配一个回车字符等价于\x0d 或cM（只有Windows中有\r）
\t    匹配一个制表符：等价于\x09或 \cl
\v    匹配一个垂直制表符；等价于\x0b或\ck

'''
# ret = re.match('si','sichuan')
# print(ret.group())
# ret = re.match('\d','0sichuan')
# print(ret.group())
# ret = re.match('\D','sichuan')
# print(ret.group())
# ret = re.match('\w','sichuan')
# print(ret.group())
# ret = re.match('\W','%sichuan')
# print(ret.group())
# ret = re.match('\s',' sichuan')
# print(ret.group())
# ret = re.match('\S','sichuan')
# print(ret.group())
# ret = re.match('\f','\fsichuan')
# print(ret.group())
# ret = re.match('\n','\nsichuan')
# print(ret.group())
# ret = re.match('\r','\rsichuan')
# print(ret.group())
# ret = re.match('\t','\tsichuan')
# print(ret.group())
# ret = re.match('\v','\vsichuan')
# print(ret.group())
# ^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/)
# string='https://baidu.com'
# ret=re.match(r'((http://)|(https://))?([a-zA-Z0-9]){0,61}\.[a-zA-Z]{2,6}',string)
# print(ret.group())
# https://[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z].com
'''
s=re.findall(r'12',str)
j=re.search(r'3',str)
l=re.split(r':|;',str)
print(s)
print(j.group())
print(l)
'''

str='1222223ADsda@!@#a'
s=re.search(r'\d*A',str)
print(s.group())