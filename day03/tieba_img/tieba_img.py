import requests
from lxml import etree
import random
import time

class TiebaImgSpider(object):

    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
        self.preUrl = 'http://tieba.baidu.com'

    def get_Tlink(self, url):
        html = requests.get(url, headers=self.headers).content.decode('utf-8')
        parse_html = etree.HTML(html)
        link_list = parse_html.xpath('//*[@id="thread_list"]//div[@class="t_con cleafix"]/div/div/div/a/@href')
        link_list = link_list[0:50]
        for link in link_list:
            url = self.preUrl + link
            self.write_img(url)
            time.sleep(random.uniform(1, 3))

    def write_img(self, url):
        print(url)
        html = requests.get(url, headers=self.headers).content.decode('utf-8')
        parse_html = etree.HTML(html)
        img_link_list = parse_html.xpath('//div[@class="d_post_content_main d_post_content_firstfloor"]//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src')
        print(img_link_list)
        for img_link in img_link_list:
            content = requests.get(img_link, headers=self.headers).content
            filename = img_link[-20:]
            with open(filename, 'wb') as f:
                f.write(content)
            print('%s下载完成' % filename)
if __name__ == '__main__':
    spider = TiebaImgSpider()
    url = 'http://tieba.baidu.com/f?kw=%D5%D4%C0%F6%D3%B1&pn=0'
    spider.get_Tlink(url)
