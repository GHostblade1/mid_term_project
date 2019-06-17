# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class StreetNetworkPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='zl_zhaopin', port=3306,
                               charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        #print(item)  # sql语句，插入数据库
        sql = "insert into t_sn (title, name, scripts, duty) values(%s, %s, %s, %s)"
        self.cursor.execute(sql, [item['title'], item['name'], item['scripts'], item['duty']]),
        self.conn.commit()
        return item
