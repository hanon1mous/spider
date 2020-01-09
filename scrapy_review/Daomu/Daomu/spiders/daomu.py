# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://daomubiji.com/']

    def parse(self, response):
        href_list = response.xpath('//ul[@class="sub-menu"]/li/a/@href|//ul/li[2]/a/@href|//ul/li[3]/a/@href').extract()
        for href in href_list:
            print(href)
            yield scrapy.Request(
                url=href,
                callback=self.parse_two_html
            )

    def parse_two_html(self, response):
        article_list = response.xpath('//article')
        for article in article_list:
            title = article.xpath('./a/text()').get()
            one_list = title.split()
            if len(one_list) < 3:
                one_list.append('填补空白')
            item = DaomuItem()
            item['volume'] = one_list[0]
            item['chapter_num'] = one_list[1]
            item['chapter_name'] = one_list[2]
            link = article.xpath('./a/@href').get()
            yield scrapy.Request(
                url=link,
                meta={
                    'item': item,
                },
                callback=self.parse_three_html
            )

    def parse_three_html(self, response):
        p_list = response.xpath('//article/p/text()').extract()
        item = response.meta['item']
        item['charter_content'] = '\n'.join(p_list)
        yield item