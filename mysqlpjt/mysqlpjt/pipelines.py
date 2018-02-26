# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MysqlpjtPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1",user="root",passwd="jhy",db="mypydb")

    def process_item(self, item, spider):
        name = item["name"][0]
        key = item["keywd"][0]

        sql = "insert into mytb(title,keywd) VALUES ('"+name+"','"+key+"')"
        self.conn.query(sql)
        return item
    def close_spider(self,spider):
        self.conn.close()
