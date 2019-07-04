# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class EndItemWhjswPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.Connect(host='127.0.0.1', user='root', password='123456', db='end_project', port=3306,
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # print(item)  # sql语句，插入数据库
        sql = "insert into t_whjsw (name,sex,marry,age,academic,nation,politics,exper,addr,census,job_status,job_addr,job_p,job_ind,job_salary,edu,job_exp) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql,
                            [item['name'], item['sex'], item['marry'], item['age'], item['academic'], item['nation'],
                             item['politics'], item['exper'], item['addr'], item['census'], item['job_status'],
                             item['job_addr'], item['job_p'], item['job_ind'], item['job_salary'], item['edu'],
                             item['job_exp']]),
        self.conn.commit()
        return item