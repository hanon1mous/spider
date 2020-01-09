import requests
import time
import random
from hashlib import md5
import json


class YoudaoSpider(object):

    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
            'Connection': 'keep-alive',
            'Content-Length': '237',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1441207149@10.168.8.64; OUTFOX_SEARCH_USER_ID_NCOO=140106721.61887646; _ntes_nnid=bed6684d3717126ab59e128a4edf7a2d,1571478054861; NTES_SESS=JQmkzA__GuAiME_cFaixkChmhK.4912E_6W6ZKNqEu2PzSAkzfcxNL7ZCyz.K4Z_j9wBq1gFleNFgjUTrmQ5tJ7uekQg_NUrDr_UQD6FLFxHczDdRcxWan0uU2mIH2rolmj8y9.N7iPh1OafecezswQN7yLki9cQbmuLDCEhHY1_G_PVSU.HGuXS4AoyDtApD4ImkIIA22u09ITMQcfjtoHm2FfKsh2Ur; ANTICSRF=0170d2523778f7a33aa7d52c91d04bd6; S_INFO=1577180096|0|#3&80#|chengxiangcourse@126.com; P_INFO=chengxiangcourse@126.com|1577180096|0|other|00&99|bej&1577179649&mail_client#bej&null#10#0#0|&0|urs&mail126|chengxiangcourse@126.com; JSESSIONID=aaaHiBxoQFb43_0_M568w; ___rl__test__cookies=1577332570770',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        self.md5 = md5()

    def get_result(self, word, dataform):
        html_json = requests.post(
            url=self.url,
            data=dataform,
            headers=self.headers
        ).json()
        return html_json
    # ("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj"
    def get_formdata(self, word):
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0, 9))
        ming = 'fanyideskweb{}{}n%A-rKaT5fb[Gy?;N5@Tj'.format(word, salt)
        self.md5.update(ming.encode())
        sign = self.md5.hexdigest()
        formdata = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': '75551116684a442e8625ebfc9e5af1ba',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        return formdata
    def main(self):
        word = input('请输入你要翻译的单词:')
        dataform = self.get_formdata(word)
        result = self.get_result(word, dataform)
        print(result)

if __name__ == '__main__':
    start = time.time()
    spider = YoudaoSpider()
    spider.main()
    end = time.time()
    print('程序运行时间%.2f' % (end-start))