'''
python 自1.5以后增加了re模块，提供了正则表达式
re模块使python拥有了正则的全部表达式
pip   包管理工具
'''
import re

'''
re.match()函数    
原型：match(patten,string,flags=0)
参数：
    patten:匹配的正则表达式
    string：要匹配的字符串
    flags：标志位，用于控制正则表达式的匹配方式   值如下：
flags:
    *re.I   忽略大小写
    re.L   做本地用户识别
    *re.M   多行匹配，影响^和$
    *re.S   使.匹配包括换行符在内的所有字符
    re.U   根据Unicode字符集解析字符，影响\w  \W  \b  \B
    re.X   使我们以更灵活的格式理解正则表达式
功能：尝试从字符串的起始位置匹配、如果不是起始位置匹配成功的话，返回None

'''

str='www.baidu.com'
s=re.match('wwW',str,re.I)
print(s.group())
print('-'* 20+'我是换行符'+'_' * 100)
'''
str='www.baidu.com'
s=re.match('wwW',str,re.I)
print(s.group())

print(s.span())
#可以得到该字符串的位置
'''

'''
re.search()函数
原型：search(patten,string,flags=0)
patten:匹配的正则表达式
string：要匹配的字符串
功能：扫描整个字符串，并返回第一个成功的匹配
'''
str='good man is whisky !whisky is nice'
s=re.search('whisky',str)
print(s.group())
print('-'* 20+'我是换行符'+'_' * 100)
'''
re.findall()函数
原型：findall(patten,string,flags=0)
patten:匹配的正则表达式
string：要匹配的字符串
功能：扫描整个字符串，并返回结果列表

'''
str='good man is whisky !Whisky is nice'
print(re.findall('whisky',str,re.I))
print('-'* 20+'我是换行符'+'_' * 100)


'''
.               匹配除换行符以外的任意字符
[1234]          []是字符集合，表示匹配方括号中所包含的任意一个字符,只能匹配一个字符
[a-z]           匹配任意一个小写字符
[A-Z]           匹配任意大写字母
[0-9]           匹配任意数字  等价于  \d
[0-9a-zA-Z_]    匹配任意一个小写字母、大写字母、数字、下划线
^               称为脱字符，表示不匹配集合中的字符
[^0-9]          匹配除了0-9以外的所有字符
\d              匹配所有的数字，效果同[0-9]
\D              匹配非数字字符，效果同[^0-9]
\w              匹配数字、字母、下划线、汉字   效果同[0-9a-zA-Z]
\W              匹配数字、字母、下划线、汉字之外的字符
\s              匹配任意的空白字符（空格、换行、换页、制表、回车），效果同[[空白符]\f\n\r\t]
\S              匹配任意的非空白符，效果同[^[空白符]\f\n\r\t]

'''
print(re.findall('\d','whisky is a good man 6   3   4'))
s='张三'
print(re.match(r'\w+',s).group())
print('-'* 20+'我是换行符'+'_' * 100)
'''
^               行首匹配，和在[]中不是一个意思
$               行尾匹配
\A              匹配字符串开始  它和^的区别是,  \A只匹配整个字符串的开头，即使在re.M模式下，也不会匹配别的行首
\Z              匹配字符串末尾  它和$的区别是,  \Z只匹配整个字符串的末尾，在re.M模式下，只会匹配最后一行行尾
\b              匹配一个单词的边界，也就是指单词和空格间的位置
                r'er\b'可以匹配never   但是不能匹配nerve 
\B              匹配非单词边界       r'er\b'可以匹配nerve   但是不能匹配never 

'''

print(re.search('.*?4$','whisky is a good man 6   3   4',re.S))
print(re.search('^whisky','whisky is a good man 6   3   4'))
print(re.search('\Awhisky','whisky is a good man 6   3   4'))
print(re.findall('\Awhisky','whisky is a good man 6   3   4\nwhisky is a good man 6   3   4',re.M))
print(re.findall('^whisky','whisky is a good man 6   3   4\nwhisky is a good man 6   3   4',re.M))
print(re.findall('Man\Z','whisky is a good man\nwhisky is a good Man',re.M))
print(re.findall('man$','whisky is a good man\nwhisky is a good man',re.M))

print(re.search(r'er\b','never'),'b用法1')
print(re.search(r'er\b','nerve'),'b用法2')
print(re.search(r'er\B','never'),'b用法3')
print(re.search(r'er\B','nerve'),'b用法4')


'''
()          匹配时候作为一个整体去匹配
x？         匹配0个或者1个x：匹配之前的字符0个或者1个
x*          匹配0个或者任意多个x
x+          匹配至少一个x   
x{m}        正好匹配m个x   （m为非负整数）
x{m,}       匹配至少m个x
x{,n}       匹配最多n个x
x{m,n}      匹配最少m个x，最多n个x
x|y         匹配x或者y
'''
'''
print(re.findall(r'(whisky)','whisky is a good man,whisky is a nice man'))
print(re.findall(r'a?','aaa'))         #非贪婪匹配（尽可能少的匹配）
print(re.findall(r'a*','aaabaaa'))    #贪婪匹配（尽可能多的匹配）
print(re.findall(r'a+','aaabaaa'))    #贪婪匹配（尽可能多的匹配）
print(re.findall(r'a{3}','aaabaaa'))
print(re.findall(r'a{2,}','aaabaa'))
print(re.findall(r'a{,4}','aaabaa'))
print(re.findall(r'a{3,6}','aaabaaa'))
print(re.findall(r'((s|S)unck)','whisky--Whisky'))
'''

'''
特殊匹配
*?    +?   x?    （非贪婪匹配）最小匹配，通常都是尽可能多的匹配，可以使用这种解决贪婪匹配

（？：x）类似（xyz）但是不表示一个组
'''
#判断电话号
'''
def check(str):
    s=re.match(r'1[345678]\d{9}',str)
    print(s)
str=input('请输入电话号：')
check(str)
'''

# 判断qq号
'''
def check(str):
     s=re.match(r'\d{6,10}',str)
     print(s.group())
str=input('请输入QQ号：')
check(str)
'''


'''
re 模块深入

字符串切割
'''
str='whisky   is a good man'
print(str.split(' '))
s=re.split(r' +',str)
print(s)


content = '{name:"zhangsan",age:"10",hobby:["basktball","football","read"]}'
pattern = re.compile(r'.*?"(.*?)".*?"(.*?)".*?')
match = pattern.search(content)
print(match)
print(match.group(1))
print(match.group(2))


# finditer()：全文匹配，多次匹配，返回一个包含匹配结果的迭代器。

# pattern.finditer(
# 	'待匹配的字符串'（必须指定）,
# 	start（匹配的开始位置）,
# 	end（匹配的结束位置）
# )
# 返回值为迭代器iterator

import re

pattern = re.compile(r'\d+')
content1 = 'hello 123456 789'
content2 = 'one1two2three3four4'
result_iter1 = pattern.finditer(content1)
result_iter2 = pattern.finditer(content2,0,7)
print(type(result_iter1))
print(type(result_iter2))
for m1 in result_iter1:
    print('matching string:{},position:{}'.format(m1.group(),m1.span()))
print('-----------------------------------------')
for m2 in result_iter2:
    print('matching string:{},position:{}'.format(m2.group(), m2.span()))

# sub()：用指定的字符串，替换正则表达式匹配到的目标字符串的内容。

# pattern.sub(
#     repl（替换成什么）,
#     content（待替换内容）,
#     count（替换次数，可不指定，默认替换所有）
# )

# repl可以是字符串也可以是函数。
#
# repl是字符串时，局限性是只能替换为固定的内容，不灵活。

import re

p = re.compile(r'(\w+) (\w+)')
s = 'hello 123,hello 456'

print(p.sub('ssss',s))
print(p.sub(r'\2 \1',s))    # 引用分组

# repl是函数时，就很灵活了。
#
# 当repl是函数的时候，这个函数必须满足以下要求：
#
# 函数必须携带一个参数，这个参数是一个match对象。

def func(match):
    '''
    对match对象的操作。
    '''
    print(match.group())

# 当在sub方法中传入这个参数时，这个match对象其实就是用正则匹配到的每一个match对象。
#
# 这个函数是有返回值的，返回值必须是一个字符串，将来是用这个字符串进行替换目标字符串的。

import re

p = re.compile(r'(\w+) (\w+)')
s = 'hello 123,hello 456'
def func(m):
    return 'hi' + ' ' + m.group(2)
print(p.sub(func,s))
print(p.sub(func,s,1))

# p = re.compile(r'\d+')
# content = 'zhangsan:3000,lisi:4000'
# def add(match):
#     return str(int(match.group())+2000)
# print(p.sub(add,content))

str1 = 'abbbcc'
parttent = re.compile(r'(ab).*(c)')
print(parttent.findall(str1))