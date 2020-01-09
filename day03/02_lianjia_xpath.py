import requests
from lxml import etree
import time
from headers_useragent import getheaders
import random
import pymysql


class LianjiaSpider(object):

    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/pg{}/'
        self.db = pymysql.connect('127.0.0.1', 'root', '546524lk', 'spiderdb', charset='utf8')
        self.cursor = self.db.cursor()

    def get_page(self, url):
        res = requests.get(
        url=url,
        headers=getheaders()
    )
        res.encoding = 'utf-8'
        self.parse_page(res.text)

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        li_list = parse_html.xpath('//ul[@class="sellListContent"]//li[@class = "clear LOGVIEWDATA LOGCLICKDATA"]|//ul[@class="sellListContent"]//li[@class = "clear LOGCLICKDATA"]')
        r_list = []
        for li in li_list:
            title = li.xpath('.//div[@class="title"]/a/text()')[0]
            total_price = float(li.xpath('.//div[@class="totalPrice"]/span/text()')[0])
            total_price = total_price * 10000
            unit_price = li.xpath('.//div[@class="unitPrice"]/@data-price')[0]
            r_list.append([title, total_price, unit_price])
        self.write_page(r_list)

    def write_page(self, r_list):
        # [[],[]]
        ins = 'insert into lianjia values (%s, %s, %s)'
        self.cursor.executemany(ins, r_list)
        self.db.commit()

    def main(self):
        for page in range(1, 11):
            url = self.url.format(page)
            self.get_page(url)
            print('第%d页爬取完成' % page)
            time.sleep(random.uniform(1, 4))


if __name__ == '__main__':
    start = time.time()
    spider = LianjiaSpider()
    spider.main()
    spider.cursor.close()
    spider.db.close()
    end = time.time()
    print('执行时间:%.2f' % (end-start))