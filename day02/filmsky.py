import re
import requests
import time
import random
import csv
from headers_useragent import getheaders


class FilmSky(object):

    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
        self.pre_url = 'https://www.dytt8.net'
        self.one_pattern = re.compile('<b>.*?<a href="(.*?)".*?>(.*?)</a>', re.S)
        self.two_pattern = re.compile('<td style="WORD-WRAP:.*?<a href="(.*?)">', re.S)

    def get_page(self, url):
        res = requests.get(url=url, headers=getheaders())
        res.encoding = 'gbk'
        return res.text

    def parse_page(self, html):
        # [('地址', '名字'),()]
        one_list = self.one_pattern.findall(html)
        sufurl_list = []
        for t in one_list:
            sufurl_list.append(t[0])
        two_list = []
        for item in sufurl_list:
            url = self.pre_url + item
            two_html = self.get_page(url=url)
            two_list.append(self.two_pattern.findall(two_html)[0])
            time.sleep(random.randint(1, 3))
        result = []
        for item_name, item_url in zip(one_list, two_list):
            result.append((item_name[1], item_url))
        self.write_page(result)

    def write_page(self, result):
        with open('filmsky.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(result)

    def main(self):
        for page in range(1, 11):
            url = self.url.format(page)
            html = self.get_page(url)
            self.parse_page(html)
            print('第%d页写入完成' % page)

if __name__ == '__main__':
    start = time.time()
    spider = FilmSky()
    spider.main()
    end = time.time()
    print('程序运行时间为%.2f' % (end-start))