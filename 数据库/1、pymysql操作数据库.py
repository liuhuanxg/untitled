#1、导包
import pymysql

#2、连接数据库
#参数：host,user,password,database,port
db = pymysql.connect(host="10.10.101.243",user="root",password="root",database="test",port=3306)

#3、创建游标对象
#游标：游标是处理数据的一种方法，为了查看或者处理结果集中的数据，在结果集中一次一行或者多行前进或向后浏览数据的能力。可以把有表当作一个指针，它可以指定结果中的任何位置，然后允许用户对指定位置的数据进行处理
#通俗来说，操作数据和获取数据库结果都要通过游标来操作
cursor = db.cursor()

#4、定义sql语句
sql = "SELECT database()"

#5、执行sql语句
cursor.execute(sql)

#获取返回值 fetchone()  获取一条数据
print(cursor.fetchone())

#6、关闭数据库连接
cursor.close()
db.close()
