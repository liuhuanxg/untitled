from sunckSql import  SunckSql

s=SunckSql('localhost','root','root','python0715')
res=s.get_all('select * from  student')
for i in  res:
    print(i)