import pymysql

db=pymysql.connect('localhost','root','426425','python0723')
content=db.cursor()
sql='delete from student  where id=1'
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

