# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class FirstPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='zl_zhaopin', port=3306,
                               charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        #print(item)  # sql语句，插入数据库
        sql = "insert into t_details (position,salary,describe_str,addr,company,year,high_port_str,main_business_str,company_scale,net_site) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, [item['position'], item['salary'], item['describe_str'], item['addr'],
                                 item['company'], item['year'], item['high_port_str'], item['main_business_str'],
                                 item['company_scale'], item['net_site']]),
        self.conn.commit()
        return item
