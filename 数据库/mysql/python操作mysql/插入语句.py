import pymysql
import random

db=pymysql.connect('10.10.101.186','wangwu','123456','test')
content=db.cursor()
list1=["2","3","4","5","7","9"]
for i in range(10000):
    name=random.choice(list1)
    print(name)
    sql="insert into student values(null,'{}' ,20 ,1,130,'xiaomi','web')".format(name)
    print(sql)
    #执行语句
    try:
        content.execute(sql)
        db.commit()
    except Exception as e:
        #如果提交失败，回滚到上一次的数据
        print(e)
        # print(3)
        db.rollback()
content.close()
#断开
db.close

