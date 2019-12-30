from lxml import etree
import requests


response=requests.get('http://www.langlang2017.com/')
response.encoding='utf-8'
print('response:',response.text)
with open('langlang.html','w',encoding='utf-8')  as fp:
    fp.write(response.text)

sele=etree.HTML(response.text)
print(type(sele))


#所有图片连接
img_list=sele.xpath('//img/@*')
print(img_list)


str_list=sele.xpath( '/html/body/div[@class="langlang"]/div/div[@class="haxiandao"]/div[@class="chi"]/div[@class="didaohaixian"]/text()')
print(str_list)

head_list = sele.xpath('//div[@class="zzdhaijingfang"]/*')
print(head_list)

title_list = sele.xpath('//script[@*]|//div[@class="nav"]/*')
print(title_list)

print('-'*200)

# # 所有img 存在@ 属性 // string() 运算符
# img_list = sele.xpath('//div[@class="haijingfang_center"]//img[@alt]/@src')
# print(img_list)
# all_content = sele.xpath('string(//div[@class="haijingfang_center"])')
# print(all_content)
#
# content2 = sele.xpath('//div[@class="haijingfang_center"]')
# print(content2)
# print(content2[0].xpath('string(..)'))
#
# print(sele.xpath('string(/html/body)'))
# content2 = sele.xpath('//div[@class="pinzhibaozhang_center"]')
# print(content2[0].xpath('string(..)'))
# # 获取子、孙标签内容


# 运算符

html_str = """    <div class="zzdhaijingfang">
    	<div class="zzd_title">真正的海景房</div>
        <p>来朗朗渔家，住真海景，出门10步到海边。距离海边实在太近了，在咱家的院里就可以看日出、日落。迎着海风，宁静、安然。</p>
        <img width='12' src="img/jingjifang.png"></img>
        <img width='15' src="img/kongtiaofang.png"></img>
        <img width='20' src="img/jingpinfang.png"></img>
        <img height='20' src="img/haijingfangicon.png"></img>
        <li>sss
    </div>"""

sele2 = etree.HTML(html_str)
print(etree.tostring(sele2))

print(sele2.xpath('//img[@width>7+8 or @height=20]/@src'))

# sele3 = etree.parse('./text.html')
# print(etree.tostring(sele3))
