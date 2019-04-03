import re
import requests
import os
from lxml import etree

base_url = 'http://www.langlang2017.com/'

response = requests.get(url=base_url)
response.encoding='utf-8'
