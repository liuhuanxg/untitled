import requests
#http://www.stat-nba.com/query.php?page=1&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_result
#&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_result

import requests
from lxml import etree
#
def NBA(url):
    response=requests.get(url)
    response.encoding='utf-8'
    with open('nba.html','w',encoding='utf-8')as fp:
        fp.write(response.text)
    tree=etree.HTML(response.text)
    tr_list=tree.xpath('//tr')
    print(tr_list)
    for tr in tr_list:
        try:
            name=tr.xpath('./td[2]/a/text()')
            lanban=tr.xpath('./td[15]/text()')
            zhugong=tr.xpath('./td[18]/text()')
            with open('nba.txt','a+',encoding='utf-8')as fp:
                fp.write(name[0]+'    '+lanban[0]+'     '+zhugong[0]+'\n')
        except:
            pass


if __name__ == '__main__':
    for i in range(60):
        base_url='http://www.stat-nba.com/query.php?&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_resultpage='+str(i)

        NBA(base_url)
