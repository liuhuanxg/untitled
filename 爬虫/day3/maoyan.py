import requests
from requests.exceptions import RequestException
import re

def get_one_page(url):
    #获取网页html并返回
    header ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    }
    try:
        #获取网页html内容
        response=requests.get(url=url,headers=header)
        print(response)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

def parse_one_page(html):
    #解析html代码，提取有用信息并返回
    #用正则表达时进行解析
    pattern=re.compile('<dd>.*?board')

if __name__ == '__main__':
    main()