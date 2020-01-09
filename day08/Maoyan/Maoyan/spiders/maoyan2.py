# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    # scrapy crawl 'name'
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    url = 'https://maoyan.com/board/4?offset={}'

    def start_requests(self):
        for page in range(0, 91, 10):
            yield scrapy.Request(
                url=self.url.format(page),
                callback=self.parse
            )

    def parse(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for film in dd_list:
            item = MaoyanItem()
            item['name'] = film.xpath('./a/@title').get().strip()
            item['stars'] = film.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = film.xpath('.//p[@class="releasetime"]/text()').get().strip()
            yield item
