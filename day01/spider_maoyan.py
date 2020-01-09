from urllib import request
import time
import random
import re


class MaoyanSpider:

    #定义常用变量
    def __init__(self):
        self.url = 'http://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    # 获取页面源代码
    def get_page(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # 解析页面源代码,获取数据
    def parse_page(self, html, pattern):
        r_list = pattern.findall(html)
        return r_list

    # 保存数据
    def write_page(self, filename, r_list):
        with open(filename, 'a', encoding='utf-8') as f:
            for item in r_list:
                for i in item:
                    f.write(i.strip())
                    f.write(' ')
                f.write('\n')

    # 主函数
    def main(self):
        pattern = re.compile('<dd>.*?title="(.*?)" class="image-link".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>', re.S)
        for item in range(1, 11):
            url = self.url.format((item-1)*10)
            html = self.get_page(url=url)
            r_list = self.parse_page(html=html, pattern=pattern)
            filename = '猫眼电影榜单top100'
            self.write_page(filename=filename, r_list=r_list)
            time.sleep(random.randint(1, 3))
            print('下载猫眼电影榜单top100-第{}页'.format(item))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.main()
