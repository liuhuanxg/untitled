from urllib import  request
from bs4 import  BeautifulSoup

#网络请求
base_url="http://www.langlang2017.com/route.html"
response=request.urlopen(base_url)
content=response.read()

#正常取文本内容需要修改编码格式
# content=content.decode('utf-8')
# print(content)


#数据提取
#1、创建Beautiful Soup  对象
#方法一：读取文本内容
soup=BeautifulSoup(content,'lxml')

#方法二：打开本地HTML文件的方式创建对象
# soup=BeautifulSoup(open('index.html'))


#2、格式化输出soup对象的内容，本身自带转码，不需要转码操作
#全部内容：
content=soup.prettify()
# print(content)

#1、Tag获取,只能查第一个符合的
'''
title=soup.title
print(title)

meta=soup.meta
print(meta)

link=soup.link
print(link)

img=soup.img
print(img)
'''
#name属性，对象本身为[document]
'''
print(soup.name)            #[document]
print(soup.title.name)      #title
print(soup.meta.name)       #meta
print(soup.link.name)       #link
print(soup.img.name)        #img
'''

#attrs  将标签中的属性以字典的方式输出
'''
print(soup.title.attrs)
print(soup.meta.attrs)
print(soup.link.attrs)
print(soup.img.attrs)
'''

'''
#获取属性值
img=soup.img.attrs
print(img)
#字典有两种方式获取属性
print(img['src'])
print(img.get('src'))

# 修改属性
img['src']="http://www.langlang2017/img/logo.png"
print(img['src'])

#删除属性
del img['alt']
print(img)
'''

#获取标签中的文本
'''
print(soup.title)           #<title>大连哈仙岛旅游--来岛路线</title>
print(soup.title.name)      #title
print(soup.title.attrs)     #{}
print(soup.title.string)    #大连哈仙岛旅游--来岛路线

print(soup.a)
'''

#四、遍历文档树
'''
#1、直接子节点：.contents    .children  属性
#.contents将tag的子节点以列表的方式输出   换行符也可能成为单独元素
# print(soup.head.contents)
# print(soup.head.contents[1])
# print(soup.head.contents[3])


#children    是一个list生成器对象
print(type(soup.head.children))
#换行符也会输出
for tag in soup.head.children:
     print(tag)
'''

#.descendants 属性可以对包含的所有 tag
# print(soup.div)
# for tag in soup.div.descendants:
#     print(tag)
#     print('--'*100)

#soup.find_all
'''
for meta in soup.find_all('meta'):
    print(meta)
print('--'* 100)
import re   #可导入正则使用
for tag in soup.find_all(re.compile('^m')):
    print(tag)
print('--'* 100)

#传入列表将列表中所有内容返回
print(soup.find_all(['h1','h2','h3','h4','h5']))
'''

'''
print(soup.find_all(id='weixin'))
print(soup.find_all(id='taobao'))

print(soup.find_all(text='预定'))
print(soup.find_all(text=['预定','大连哈仙岛旅游--来岛路线']))
'''

#CSS选择器   查找出来是一个列表
#标签名查找
print(soup.select('title'))
print(soup.select('link'))

#类名查找
print(soup.select('.logo'))

#id查找
print(soup.select('#banner01'))
#后代查找
print(soup.select('div #taobao'))
#直接子标签查找
print("title",soup.select("head > title"))
#属性查找
print("img",soup.select('div img[class="weixin"]'))

#获取内容
print("h2",soup.select('h2')[0].get_text())

for h2 in soup.select('h2'):
    print(h2.get_text())