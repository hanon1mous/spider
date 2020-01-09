# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class Picture360Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['img_link']
        )

class Picture360CommonPipeline(object):

    def process_item(self, item, spider):
        print(12345)
        filename = 'D:\\PycharmProjects\\360so\\{}'.format(item['name'])
        with open(filename, 'wb') as f:
            f.write(item['content'])
        return item

