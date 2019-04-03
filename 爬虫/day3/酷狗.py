import requests
from bs4 import BeautifulSoup
import time

header={
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
}

def get_info(url):
     wb_data=requests.get(url,headers=header)   #get方法加入请求头
