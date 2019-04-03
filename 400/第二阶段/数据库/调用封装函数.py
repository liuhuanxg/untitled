from sunckSql import  SunckSql

s=SunckSql('localhost','root','426425','python0723')
res=s.get_all('select * from  student')
for i in  res:
    print(i)