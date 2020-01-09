# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    # scrapy crawl 'name'
    name = 'maoyan1'
    allowed_domains = ['maoyan.com']
    # 引擎向爬虫程序所要第一个要爬取的url地址 交给调度器入队列，生成指纹，出队列，再给引擎，引擎
    # 通过下载器中间件后交给下载器去发请求，得到response
    start_urls = ['https://maoyan.com/board/4?offset=0']
    url = 'https://maoyan.com/board/4?offset={}'
    # 下载器得到response交给引擎，引擎通过蜘蛛中间件后交给了爬虫程序

    def parse(self, response):
        for page in range(0, 91, 10):
            yield scrapy.Request(
                url=self.url.format(page),
                callback=self.parse_html
            )

    def parse_html(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for film in dd_list:
            item = MaoyanItem()
            item['name'] = film.xpath('./a/@title').get().strip()
            item['stars'] = film.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = film.xpath('.//p[@class="releasetime"]/text()').get().strip()
            yield item
