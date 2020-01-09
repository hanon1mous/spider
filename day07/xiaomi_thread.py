from threading import Thread
from queue import Queue
import requests
import time
import json

class XiaomiSpider(object):

    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        self.headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        self.url_que = Queue()
        self.count = 1

    def url_in_queue(self):
        for page in range(67):
            self.url_que.put(self.url.format(page))

    def get_data(self):
        while True:
            if self.url_que.empty():
                break
            else:
                html = requests.get(
                    url=self.url_que.get(),
                    headers=self.headers
                ).json()
                # html = json.loads(html)
                app_dict = {}
                for app in html['data']:
                    app_dict['应用名称'] = app['displayName']
                    app_dict['应用链接'] = app['packageName']
                    print(app_dict)
                    print(app)
                    self.count += 1

    def main(self):
        self.url_in_queue()
        t_list = []
        for i in range(5):
            t = Thread(target=self.get_data)
            t.start()
            t_list.append(t)
        for t in t_list:
            t.join()

if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print(spider.count)
    print('程序运行时间为%.2f' % (end-start))