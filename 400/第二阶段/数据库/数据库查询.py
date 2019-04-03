import pymysql
'''
参数1、mysql服务所在主机IP
参数2、用户名
参数3、密码
参数4、要链接的数据库名
'''
'''
fetchone()：获取下一个查询结果集，结果集是一个对象
fetchall():接受全部返回的行
rowcount:是一个只读属性，返回execute()方法
'''
db=pymysql.connect('localhost','root','426425','python0723')

#创建一个cursor对象
content=db.cursor()
sql='select * from  student'
#执行语句
content.execute(sql)
#获取返回的信息
data=content.fetchall()
for i in data:
    print(i)
content.close()
#断开
db.close

