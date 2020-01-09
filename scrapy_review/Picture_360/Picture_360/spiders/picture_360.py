# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import Picture360Item

class Picture360Spider(scrapy.Spider):
    name = 'picture_360'
    allowed_domains = ['so.com']
    def start_requests(self):
        url = 'https://image.so.com/zjl?ch=car&sn={}&listtype=new&temp=1'
        for sn in range(0, 5):
            page = sn * 30
            yield scrapy.Request(
                url=url.format(page),
                callback=self.parse
            )

    def parse_second_method(self, response):
        html_dict = json.loads(response.text)
        for car in html_dict['list']:
            item = Picture360Item()
            item['name'] = car['qhimg_url'].split('/')[-1]
            yield scrapy.Request(
                url=car['qhimg_url'],
                meta={
                    'item': item,
                },
                dont_filter=True,
                callback=self.parse_img
            )

    def parse_img(self, response):
        item = response.meta['item']
        item['content'] = response.body
        yield item

    def parse(self, response):
        html_dict = json.loads(response.text)
        for car in html_dict['list']:
            item = Picture360Item()
            item['img_link'] = car['qhimg_url']
            yield item

