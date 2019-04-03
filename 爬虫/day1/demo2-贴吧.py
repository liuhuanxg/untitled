from urllib import  request,parse

def tieba(kw,num):
    header={
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.106Safari / 537.36'
    }
    base_url='http://tieba.baidu.com/f?kw=%s&fr=ala0&tpl=5pn=%d'%(kw,num)
    req=request.Request(url=base_url,headers=header)
    content=request.urlopen(req).read()
    html=content.decode('utf-8')
    with open('%s-贴吧.html'%kw,'w+',encoding='utf-8') as fb:
        fb.write(html)
        print('爬取完成')
if __name__ == '__main__':
    kw=input('请输入要爬取的贴吧名：')
    num = int(input('请输入要爬取的页码：'))
    tieba(kw,num)