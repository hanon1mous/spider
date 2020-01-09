import requests
from headers_useragent import getheaders
import time
import re
import random
from lxml import etree

class LianjiaSpider(object):

    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'
        self.pattern = re.compile('<div class="item_list">.*?alt="">(.*?)</div>.*?>(.*?)</div>.*?<em>(.*?)</em>', re.S)

    def get_page(self, url):

        res = requests.get(url, headers=getheaders())
        print(res.text)
        self.parse_page(res.text)

    def parse_page(self, html):
        # [('', '' ,'' ,'')]
        r_list = self.pattern.findall(html)
        print(r_list)
        one_house_dict = {}
        for rt in r_list:
            one_house_dict['标题'] = rt[0].strip()
            one_house_dict['介绍'] = rt[1]
            one_house_dict['价格'] = '%s万' % rt[2]
            print(one_house_dict)


    def write_page(self):
        pass

    def main(self):
        self.get_page('https://bj.lianjia.com/ershoufang/pg9')


if __name__ == '__main__':
    start = time.time()
    spider = LianjiaSpider()
    spider.main()
    end = time.time()
    print('程序运行总时间%.2f' % (end-start))