import requests
import re

header={
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
}

base_url='http://maoyan.com/board'
response=requests.get(url=base_url,headers=header)

par=re.compile(r'<dd>(.*?)</dd>',re.S)
dd_list=par.findall(response.text)
print(dd_list[0])
for dd in dd_list:
  #爬取排名
  paiming_re=re.compile(r'<i class="board-index.*?">(\d+)</i>',re.S)
  paiming=paiming_re.findall(dd)

  #爬取电影名字
  name_re=re.compile(r'<a.*?>(.*?)</a>')
  move_name=name_re.findall(dd)

  # 爬取电影主演
  satr_re=re.compile(r'<p class="star">\s*(\S*)\s*</p>')
  satr_name=satr_re.findall(dd)

  #爬取上映时间
  time_re=re.compile(r'<p class="releasetime">(.*?)</p>')
  time=time_re.findall(dd)

  #爬取电影评分
  pingfen1_re=re.compile(r'<i class="integer">(.*?)</i>')
  pingfen1=pingfen1_re.findall(dd)
  pingfen2_re=re.compile(r'<i class="fraction">(.*?)</i>')
  pingfen2=pingfen2_re.findall(dd)
  pingfen=str(pingfen1[0])+str(pingfen2[0])

  #将电影信息写入文档
  with open('猫眼.txt','a+',encoding='utf-8') as fq:
      fq.write('排名：%s'%(paiming[0])+'\n'+''+'电影名字：%s'%(move_name[0])+'\n'+satr_name[0]+'\n'+'评分：%s'%pingfen+'\n'+time[0]+'\n')
  print('爬取成功！')

