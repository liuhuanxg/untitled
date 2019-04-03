import requests

url= 'https://book.douban.com/subject_search?search_text=python&cat=1001'
response=requests.get(url=url)
with open('douban.html','w',encoding='utf-8') as fp:
    fp.write(response.text)