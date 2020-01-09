# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        print(item['volume'], item['chapter_num'], item['chapter_name'])
        filename = 'D:\\PycharmProjects\\daomubiji\\{}_{}_{}.txt'.format(item['volume'], item['chapter_num'], item['chapter_name'])
        with open(filename, 'w') as f:
            f.write(item['charter_content'])
        return item
