import pymysql
'''
参数1、mysql服务所在主机IP
参数2、用户名
参数3、密码
参数4、要链接的数据库名
'''
db=pymysql.connect('localhost','root','426425','python0723')

#创建一个cursor对象
content=db.cursor()
sql='select * from  student'

#执行语句
content.execute(sql)
#获取返回的信息
data=content.fetchone()
print(data)

#断开
db.close

