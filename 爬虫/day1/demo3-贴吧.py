from urllib import request,parse

def get_tieba(name,page=1):
    data={
        'pw':name,
        'pn':(page-1)*50,
        'ie':'utf-8'
    }
    header={
        'User-Agent':'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.106Safari / 537.36'
    }
    base_url='http://tieba.baidu.com/f?'
    par_url=parse.urlencode(data)
    url=base_url+par_url
    reg=request.Request(url=url,headers=header)
    html=request.urlopen(reg).read().decode('utf-8')
    with open('%s-百度贴吧.html'%name,'w',encoding='utf-8') as fp:
        fp.write(html)

if __name__ == '__main__':
    name=input('请输入贴吧名称：')
    get_tieba(name)