# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    def start_requests(self):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?' \
              'pageIndex={}&pageSize=10&language=zh-cn&area=tw'
        for page in range(1, 31):
            yield scrapy.Request(
                url=url.format(page),
                callback=self.parse
            )

    def parse(self, response):
        html_dict = json.loads(response.text)
        for position in html_dict['Data']['Posts']:
            item = TencentItem()
            item['title'] = position['RecruitPostName']
            item['category'] = position['CategoryName']
            post_id = position['PostId']
            two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?' \
                      'postId={}&language=zh-cn'
            yield scrapy.Request(
                url=two_url.format(post_id),
                meta={
                    'item': item,
                },
                callback=self.parse_two_html
            )

    def parse_two_html(self, response):
         html_dict = json.loads(response.text)
         item = response.meta['item']
         item['duty'] = html_dict['Data']['Responsibility']
         item['required'] = html_dict['Data']['Requirement']
         yield item

