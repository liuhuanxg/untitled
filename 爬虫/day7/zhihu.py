
import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://www.zhihu.com/search?q=%E4%B9%B3%E8%85%BA%E7%99%8C&utm_content=search_history&type=content',
    # 'cookie': '_zap=a3003bee-d252-4ae0-8806-944eda29ac91; d_c0="AMDlTKq8jBCPTnUAedYXpoedMrZc4JzIu8g=|1577102605"; _xsrf=cfd6f794-3fd0-46bc-a225-5c3971505bb2; l_n_c=1; n_c=1; tst=r; q_c1=c1fa8f749ab84c808448d4e937df6a0d|1577699863000|1577699863000; capsion_ticket="2|1:0|10:1577703176|14:capsion_ticket|44:YmRhZGNlYmYyODE0NGUwNThlNzNjNjY1YTRiYjdlMjE=|c2c7b2f04e7d68776c49bf96aebce73acc4a2b5520b64a438ea6acdc01c83d52"; r_cap_id="ZGY2YjU0ZTg3NjE1NGQ3YWJlNjJkNmQ0MmYyYzY4NTA=|1577703187|1bf878854bbadb2e9a542a274eb0562eb15e4c12"; cap_id="YTA0ZTBkYmVmNjZlNDY5OWI1MDE2NjM4YThjYTM0MGM=|1577703186|3a4be52015fff006c2009e4f9b5b5bf9f515476e"; l_cap_id="NDY4YzAxMDY2MGIwNDMzYWI3YjU3OTk2YWEzMzYxYTA=|1577703187|3d338b077d881fb1874524a9c65b933fbb214e84"; z_c0=Mi4xSFJFV0F3QUFBQUFBd09WTXFyeU1FQmNBQUFCaEFsVk5GeVgzWGdDaUl5WEprR0UyUEtLMHMzRUhWY3I2N2ZnN0hB|1577703191|0738562764f6a8e8a67e06e34d280b9c1633e502; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1577932237,1577942273,1577942321,1577942433; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1577944307|1577941881; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1577944307'
}
params = {
    't': 'general',
    'q': '乳腺癌',
    'correction': '1',
    'offset': '20',
    'limit': '20',
    'lc_idx': '26',
    'show_all_topics': '0',
    'search_hash_id': '6003b8b9b3ed959a582483e70b9f4cc5',
    'vertical_info': '0,1,0,0,0,0,0,0,0,1',
}
response = requests.get('https://www.zhihu.com/api/v4/search_v3?',headers=headers,params=params)

# response.content.decode("utf-8")
with open("1.txt","a+",encoding='utf-8') as p:
    p.write(response.text)