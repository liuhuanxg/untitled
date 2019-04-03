# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
import pymongo

class BaiduPipeline(object):
    def process_item(self, item, spider):
        return item

class TencentPipeline(object):
    # def __init__(self):
    #     #在初始化方法中完成数据库的打开操作
    #     self.conn=pymysql.connect('127.0.0.1','root','426425','tencent',charset='utf8')
    #     self.cursor=self.conn.cursor()
    #
    # def process_item(self, item, spider):
    #     #在该方法中完成对数据库的操作
    #
    #     # data=json.dumps(dict(item),ensure_ascii=False)
    #     # with open('tencent.json','a',encoding='utf-8') as fp:
    #     #     fp.write(data+'\n')
    #
    #     #1、写sql语句
    #     sql="insert into jobs(title,job_type,num,job_local,realtime) VALUES(%s,%s,%s,%s,%s,)"
    #     #2、准备好数据
    #     data=(item['title'],item['job_type'],item['num'],item['job_local'],item['realtime'])
    #
    #     try:
    #         #3、执行sql
    #         self.cursor.execute(sql,data)
    #         #4、提交事务
    #         self.conn.commit()
    #     except Exception as e:
    #         self.conn.rollback()
    #         print('1111')
    #
    #     return item
    #
    # def close_spider(self,spider):
    #     #在该方法中完成数据库的关闭操作
    #     self.cursor.close()
    #     self.conn.close()


    #使用MongoDB实现
    def __init__(self):
        self.client=pymongo.MongoClient('localhost')
        self.db=self.client['tencent']

    def process_item(self, item, spider):
        #在该方法中插入数据
        self.db['work'].insert(dict(item))

        #最后需要返回item
        return item
