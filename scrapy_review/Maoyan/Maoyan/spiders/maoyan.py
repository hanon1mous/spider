# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    url = 'https://maoyan.com/board/4?offset={}'

    def start_requests(self):
        for page in range(0, 10):
            yield scrapy.Request(
                url=self.url.format(page),
                callback=self.parse
            )

    def parse(self, response):
        dd_list = response.xpath('//*[@id="app"]/div/div/div[1]/dl//dd')
        for film in dd_list:
            item = MaoyanItem()
            item['name'] = film.xpath('./a/@title').extract_first()
            item['stars'] = film.xpath('.//p[@class="star"]/text()').get().strip()[3:]
            item['time'] = film.xpath('.//p[@class="releasetime"]/text()').get().strip()[5:]
            yield item

