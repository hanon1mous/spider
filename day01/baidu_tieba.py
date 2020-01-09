import time
import random
import requests


class TiebaSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

    # 获取页面源代码
    def get_page(self, url, params):
        html = requests.get(url=url, params=params, headers=self.headers).content.decode('utf-8')
        return html

    # 解析页面,提取数据
    def parse_page(self):
        pass

    # 保存数据
    def write_page(self, filename, html):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)

    def main(self):
        name = input('请输入要搜索的贴吧名称:')
        start = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        for page in range(start, end+1):
            url = self.url
            params = {'kw': name,
                      'pn': str((page-1)*50)
                      }
            html = self.get_page(url=url,params=params)
            filename = '{}-第{}页.html'.format(name, page)
            self.write_page(filename=filename, html=html)
            time.sleep(random.randint(1, 3))
            print("第{}页爬取成功".format(page))


if __name__ == '__main__':
    tiebaSpider = TiebaSpider()
    tiebaSpider.main()