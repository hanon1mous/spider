import requests
import time

class TencentRecruitSpider(object):

    def __init__(self):
        self.url = 'https://careers.tencent.com/tencentcareer/api/post/Query?' \
                   'timestamp=1577192989244&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&' \
                   'pageIndex={}&pageSize={}&language=zh-cn&area=tw'
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'cookie': '_ga=GA1.2.1505315061.1571486392; pgv_pvi=553242624; _gcl_au=1.1.1006374975.1571486395; pgv_si=s5996028928; loading=agree',
            'referer': 'https://careers.tencent.com/search.html?index=2',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        }

    def get_data(self, url):
        try:
            html_json = requests.get(
                url=url,
                headers=self.headers
            ).json()
            recruit_list = []
            position = {}
            for recruit in html_json['Data']['Posts']:
                position['titie'] = recruit['RecruitPostName']
                position['time'] = recruit['LastUpdateTime']
                recruit_list.append(position.copy())
            print('*' * 50)
            print(recruit_list)
            for item in recruit_list:
                print(item)
        except Exception as e:
            pass


if __name__ == '__main__':
    page = int(input('请输入爬取的起始页:'))
    size = int(input('请输入爬取的数量:'))
    begin = time.time()
    spider = TencentRecruitSpider()
    url = spider.url.format(page, size)
    spider.get_data(spider.get_data(url))
    end = time.time()
    print('爬取页面共用%.2f秒' % (end-begin))