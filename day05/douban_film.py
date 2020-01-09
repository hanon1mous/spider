import requests
import time
import random
import pymysql


class DoubanFilmSpider(object):

    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit={}'
        self.headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': 'll="108288"; bid=FX6TWE8bWJ0; __yadk_uid=xttyVxzWU7OCyr1kPjWjPzwFwtt9nccd; _vwo_uuid_v2=D8A23ECAD77B1E28958716F2F1D2A8A49|ce944b613559f403ecff1d1e9e1f62af; douban-fav-remind=1; __gads=Test; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1577242499%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DN93TgDG1GtEPAiH1D6wwbZ5Zf0Lh6YZjdwnXRyH3wNdeNESJBeUCjcgj_K99vss4%26wd%3D%26eqid%3Dfb68f7af0000322a000000025e02cf7d%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.883956788.1566184019.1577181605.1577242499.12; __utmb=30149280.0.10.1577242499; __utmz=30149280.1577242499.12.12.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.973910011.1566184019.1577181605.1577242499.3; __utmz=223695111.1577242499.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; ap_v=0,6.0; _pk_id.100001.4cf6=8fa21eba0f9afd48.1566184019.3.1577242684.1577181612.; __utmb=223695111.13.10.1577242499',
            'Host': 'movie.douban.com',
            'Referer': 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.type_dict = {
            '科幻': 17,
            '喜剧': 24,
            '爱情': 13,
            '动作': 5
        }
        self.db = pymysql.connect('127.0.0.1', 'root', '546524lk', 'spiderdb', charset='utf8')
        self.cursor = self.db.cursor()


    def get_data(self, url):
        html_json = requests.get(url, headers=self.headers).json()
        print(html_json)
        all_film_list = []
        for film_dict in html_json:
            all_film_list.append([film_dict['title'], film_dict['score'], ",".join(film_dict['actors'])])
        self.write_data(all_film_list)
    def write_data(self, all_film_list):
        ins = 'insert into doubanfilm values (%s,%s,%s)'
        self.cursor.executemany(ins, all_film_list)
        self.db.commit()
        self.cursor.close()
        self.db.close()

    def main(self):
        pass

if __name__ == '__main__':
    film_type = str(input('请输入你要爬取的电影类型(科幻,喜剧,爱情,动作):'))
    start = int(input('请输入从第几个电影开始爬取:'))
    limit = int(input('请输入爬取电影数量:'))
    spider = DoubanFilmSpider()
    url = spider.url.format(spider.type_dict[film_type], start, limit)
    spider.get_data(url)
    print('写入数据库成功')