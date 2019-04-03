import re
import requests
import os

base_url='http://www.langlang2017.com/'
root_path='./langlang_site'
response=requests.get(url=base_url)
response.encoding='utf-8'
print(response.text)
with open(root_path+'/index.html','w',encoding='utf-8') as fp:
    fp.write(response.text)


partern=re.compile(r'<img.*?src="(.*?)">')
img_list=partern.findall(response.text)
for img_path in img_list:
    imgs_url=re.split(r'/',img_path)
    img_root = root_path
    for path in imgs_url:
        img_root+='/'+path
        print(img_root)
        if not os.path.exists(img_root) and path != imgs_url[-1]:
            os.mkdir(img_root)
        elif path == imgs_url[-1]:
            img_response = requests.get(url=base_url + img_path)
            # 保存图片
            with open(img_root, 'wb') as fp:
                fp.write(img_response.content)