# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TencentrecruitItem


class TencentrecruitSpider(scrapy.Spider):
    name = 'tencentRecruit'
    allowed_domains = ['careers.tencent.com']

    def start_requests(self):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?' \
              'pageIndex={}&pageSize=10&language=zh-cn&area=tw'
        for pageIndex in range(1, 11):
            yield scrapy.Request(
                url=url.format(pageIndex),
                callback=self.parse
            )

    def parse(self, response):
        url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?' \
              'postId={}&language=zh-cn'
        html = json.loads(response.text)
        for position in html['Data']['Posts']:
            item = TencentrecruitItem()
            item['title'] = position['RecruitPostName']
            item['post_id'] = position['PostId']
            yield scrapy.Request(
                url=url.format(item['post_id']),
                meta={
                    'item': item,
                },
                callback=self.parse_two_html
            )

    def parse_two_html(self, response):
        item = response.meta['item']
        html = json.loads(response.text)
        item['responsibility'] = html['Data']['Responsibility']
        item['require'] = html['Data']['Requirement']
        yield item
