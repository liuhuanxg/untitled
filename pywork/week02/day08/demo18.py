import time
a='2019-07-24 17:04:00'
at=time.strptime(a,'%Y-%m-%d %H:%M:%S')
ac=time.mktime(at)
while True:
    bc=time.mktime(time.localtime())
    cc=bc-ac
    d=7*24*3600-cc
    days=int(d//(24*3600))
    hours=int(d%(24*3600)//3600)
    minutes=int(d%(3600)//60)
    seconds=int(d%60)
    print('\r','您还有{}天{}小时{}分钟{}秒解冻'.format(days,hours,minutes,seconds),end='')
    time.sleep(1)