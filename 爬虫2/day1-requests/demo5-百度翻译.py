#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo5-百度翻译.py
@Time: 2019/11/22 14:13
@user：python-刘欢
"""
import os
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
url = 'https://fanyi.baidu.com/langdetect'
data = {
    'query':'hello python'
}
path = os.path.join(os.getcwd(), 'download/demo5-百度翻译.html')
response = requests.post(url=url,data=data,headers=headers)
content = json.loads(response.content.decode('utf-8'))
fm = content['lan']
print(fm)

# with open(path,'w',encoding='utf-8') as fp:
#     fp.write(content)
# for i in content['data']:
#     for k,v in i.items():
#         print("k：",k,'\t',"v：",v)


headers = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'content-length': '128',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'cookie': 'BAIDUID=CAE3AE3F9D95FF764A4FEBFACAB8FA4D:FG=1; BIDUPSID=CAE3AE3F9D95FF764A4FEBFACAB8FA4D; PSTM=1563267654; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=dZMVBzfk8tYX5HSThoNmZrLXNMSUhMTXRNNHRncTlJaEtaY1c5VEc1dTlrcmRkRVFBQUFBJCQAAAAAAAAAAAEAAABEzF2Vvt5Ezve5zwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL0FkF29BZBdS3; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-131%3A; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; from_lang_often=%5B%7B%22value%22%3A%22spa%22%2C%22text%22%3A%22%u897F%u73ED%u7259%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; H_PS_PSSID=; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1574403513,1574403613,1574429537,1574429553; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1574429654; __yjsv5_shitong=1.0_7_c827b854e923b637a5c181ce9d6e1f68ddba_300_1574429683561_123.118.159.34_43197078; yjs_js_security_passport=43601082730fdb07f0df5a67fd9d42c995854ed7_1574429684_js',
'origin': 'https://fanyi.baidu.com',
'referer': 'https://fanyi.baidu.com/',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
}
base_url = 'https://fanyi.baidu.com/v2transapi?from={}&to=zh'.format(fm)
params = {
    'from':fm,
    'to':'zh'
}
data = {
    'from':'en',
    'to':'zh',
    'query':'hello python',
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '288018.34339',
    'token': 'cdb13b02c59f2dd4fd1d9ad22783c5f5',
}
import json
response = requests.post(url=base_url,data=data,headers=headers)
json_data = json.loads(response.content.decode('utf-8'))
print(json_data)
import hashlib
md = hashlib.md5()
md.update('288018.34339'.encode('utf-8'))
print(md.hexdigest())
