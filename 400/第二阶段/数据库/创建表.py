import pymysql

db=pymysql.connect('localhost','root','root','python0715')
content=db.cursor()
sql='create table d(id int not null auto_increment PRIMARY KEY,name VARCHAR(20) not null DEFAULT  "" );'
#执行语句
content.execute(sql)
#获取返回的信息

content.close()
#断开
db.close

