import requests
from lxml import etree
import json


# 获取页面内容


def job_search(name, number):
    base_url = 'https://hr.tencent.com/position.php'
    data = {
        'keywords': name,
        'lid': 0,
        'tid': 0,
        'start': number
    }

    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=lgaje93fiam2uedapi9ivr3qd4; pgv_pvi=6216335360; pgv_si=s5234728960',
        'Host': 'hr.tencent.com',
        'Referer': 'https://hr.tencent.com/position.php?keywords=python&lid=33',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    }
    response = requests.get(base_url, headers=header, params=data)

    with open('tengxun.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)

    sel = etree.HTML(response.text)

    tr_list = sel.xpath('//table[@class="tablelist"]//tr[@class !="h" and @class!="f"]')

    data_list = []
    for tr in tr_list:
        # print(tr.xpath('string(./td)'))
        data = {}
        data['name'] = tr.xpath('./td[1]//text()')[0]
        data['type'] = tr.xpath('./td[2]/text()')[0]
        data['number'] = tr.xpath('./td[3]/text()')[0]
        data['address'] = tr.xpath('./td[4]/text()')[0]
        data['date'] = tr.xpath('./td[5]/text()')[0]
        data_list.append(data)

    with open(name + '职位信息.txt', 'w', encoding='utf-8') as fp:
        fp.write(json.dumps(data_list))


if __name__ == '__main__':
    name = input('请输入要检索的职位名称：')
    for i in range(1, 11):
        job_search(name, (i - 1) * 10)
