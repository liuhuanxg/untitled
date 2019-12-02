import sqlalchemy
#1、导包

from sqlalchemy.ext.declarative import declarative_base
#类似pymysql中的游标

from sqlalchemy.orm import sessionmaker

#2、创建连接
#数据库类型+数据库的操作包://用户名:密码@IP地址/数据库
#有mysqlclient包时，mysql+pymysql可改为mysql

db = sqlalchemy.create_engine("mysql://root:root@localhost/sqlorm")

#3、创建基类
base = declarative_base(db)

#4、创建表--数据类型
class User(base):
    #表名
    __tablename__="user"
    #字段
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(32))
    age = sqlalchemy.Column(sqlalchemy.Integer)

class UserInfo(base):
    __tablename__="userinfo"
    id = sqlalchemy.Column(sqlalchemy.Interval,primary_key=True)
    phone = sqlalchemy.Column(sqlalchemy.String(20))

if __name__=="__main__":
    #执行数据库迁移（创建表）
    base.metadata.create_all(db)
    #绑定一个session实例
    s=sessionmaker(bind=db)
    #创建一个会话对象，类似于游标
    session=s()

    #数据库操作
    #添加
    #1.1 单条插入
    # user = User(name="hello",age=16)
    # session.add(user)
    # session.commit()

    #1.2、多条插入
    # session.add_all([
    #     User(name="world",age=20),
    #     User(name="python",age=28),
    #     User(name="PHP",age=34)
    # ])
    # session.commit()

    #2、查询
    #2.1、查询所有的数据，返回一个存放对象的列表
    # res = session.query(User).all()
    # for x in res:
    #     print(x.name,x.age)
    #2.2、通过主键值查询一条数据，返回一个对象
    # res = session.query(User).get(2)
    # print(res.name,res.age)

    #条件查询，返回的 是一个存放对象的列表
    # res = session.query(User).filter_by(name="python").all()
    # for x in res:
    #     print(x.name,x.age)

    #3、修改
    res = session.query(User).get(1)
    res.name='hh'
    session.commit()

    #4、删除
    res =session.query(User).get(1)
    session.delete(res)
    session.commit()

# pymysql与orm的对比
#pymysql—sql—>pymysql—sql—>mysql

#python—python—>ORM—sql—>mysql