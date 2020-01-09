# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.xpath('/html/head/title/text()'))
        result = response.xpath('/html/head/title/text()').get()
        print(result)
