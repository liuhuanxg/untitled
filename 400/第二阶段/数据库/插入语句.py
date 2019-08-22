import pymysql

db=pymysql.connect('localhost','root','root','python0715')
content=db.cursor()
sql='insert into student values( null，xiaoming ,40 ,boy,Aiouniya,175,2,1978-04-30,18690307883,1)'
#执行语句
try:
    content.execute(sql)
    db.commit()
except:
    #如果提交失败，回滚到上一次的数据
    print(3)
    db.rollback()
content.close()
#断开
db.close

