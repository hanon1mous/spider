# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from .settings import *
import pymysql

class TencentPipeline(object):
    def process_item(self, item, spider):
        return item

class TencentMysqlPipeline(object):

    def open_spider(self, spider):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQL_CHARSET
        )
        self.cursor = self.db.cursor()
        print('open_spider')

    def process_item(self, item, spider):
        ins = 'insert into tencentrecruit values(%s,%s,%s,%s)'
        self.cursor.execute(ins, [item['title'], item['category'], item['duty'], item['required']])
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
        print('close_spider')
