from  lxml import etree
import requests
base_url='https://www.qiushibaike.com/'

header={
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
}

response=requests.get(url=base_url,headers=header)
print(type(response.text))
# print(response.text)

#利用etree.HTML将字符串解析为HTML文档
html=etree.HTML(response.text)
print(type(html))

zuozhe=html.xpath('//div[@class="author clearfix"]/a/h2/text()')
for i in zuozhe:
 print(i)
contents=html.xpath('//div[@class="content"]/span[1]/text()')
for content in contents:
 print(content)
dianzan=html.xpath('//span[@class="stats-vote"]/i/text()')
print(dianzan)
pinglun=html.xpath('//span[@class="stats-comments"]/a/i/text()')
print(pinglun)
