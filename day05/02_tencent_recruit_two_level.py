import requests
import time
import random

class TecentRecruitTwoLevelSpider(object):
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?' \
                       'timestamp=1577275211114&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&' \
                       'pageIndex={}&pageSize=10&language=zh-cn&area=tw'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?' \
                       'timestamp=1577274965440&postId={}'
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
        html_json = requests.get(
            url=url,
            headers = self.headers
        ).json()
        recruit_list = []
        for post in html_json['Data']['Posts']:
            post_id = post['PostId']
            r_list = self.get_twolevelpage_data(post_id, post['RecruitPostName'])
            recruit_list.append(r_list)
        print(recruit_list)

    def get_twolevelpage_data(self, post_id, name):
        html_json = requests.get(
            url=self.two_url.format(post_id),
            headers=self.headers
        ).json()
        return [name, html_json['Data']['Responsibility'].strip().replace('\n', ''), html_json['Data']['Requirement'].strip().replace('\n', '')]

if __name__ == '__main__':
    spider = TecentRecruitTwoLevelSpider()

    for pageIndex in range(1, 11):
        url = spider.one_url.format(pageIndex)
        spider.get_data(url)
        print('第%d页爬取完成' % pageIndex)
        time.sleep(random.randint(1, 3))
