import requests
import execjs
import re


class BaiduFanyiSpider(object):

    def __init__(self):
        self.post_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
        self.get_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
            "cookie": "BAIDUID=8CFC882687FF7DE0E06CBA0BE47E402B:FG=1; PSTM=1561427303; BIDUPSID=01E1833B48818C2D9DA39D9EF1F75CFA; BDUSS=mVaQWotZkQwanhUTFZadjVDbTJzcDNYYUozcjkxWlJ1Z0FrS2tpVkFHMEZaanBkRVFBQUFBJCQAAAAAAAAAAAEAAADY7e7Ss8zQ8sDgyMvUswAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXZEl0F2RJdS; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22rom%22%2C%22text%22%3A%22%u7F57%u9A6C%u5C3C%u4E9A%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1577417326,1577439018,1577440330,1577440431; H_PS_PSSID=1469_21096_30210_18559_30284_30452_30482; delPer=0; PSINO=2; yjs_js_security_passport=06e0b12ad881b15f3cd6796452bcc98f8240e936_1577448405_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1577448710; __yjsv5_shitong=1.0_7_004c345908ff00a0185bae7f93f20dd95f36_300_1577448709877_123.112.14.132_2be60798",
            "referer": "https://fanyi.baidu.com/?aldtype=16047",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
        }
        self.headers1 = {
            "authority": "fanyi.baidu.com",
            "method": "POST",
            "path": "/v2transapi?from=en&to=zh",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
            "content-length": "120",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "BAIDUID=8CFC882687FF7DE0E06CBA0BE47E402B:FG=1; PSTM=1561427303; BIDUPSID=01E1833B48818C2D9DA39D9EF1F75CFA; BDUSS=mVaQWotZkQwanhUTFZadjVDbTJzcDNYYUozcjkxWlJ1Z0FrS2tpVkFHMEZaanBkRVFBQUFBJCQAAAAAAAAAAAEAAADY7e7Ss8zQ8sDgyMvUswAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXZEl0F2RJdS; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22rom%22%2C%22text%22%3A%22%u7F57%u9A6C%u5C3C%u4E9A%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1577417326,1577439018,1577440330,1577440431; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1577440431; yjs_js_security_passport=994bcf27f7471d0ffe88df36089abd6e38ba9fcb_1577440431_js; H_PS_PSSID=1469_21096_30210_18559_30284_30452_30482",
            "origin": "https://fanyi.baidu.com",
            "referer": "https://fanyi.baidu.com/?aldtype=16047",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }



    def get_token(self):
        html = requests.get(
            url=self.get_url,
            headers=self.headers
        ).content.decode('utf-8')
        print(html)
        pattern = re.compile("token: '(.*?)'", re.S)
        result = pattern.findall(html)[0]
        print(html)
        print(result)
        return result

    def get_sign(self, word):
        with open('node.js', 'r') as f:
            nodejs = f.read()
        execjs_obj = execjs.compile(nodejs)
        return execjs_obj.eval('e("{}")'.format(word))


    def get_result(self, word):
        sign = self.get_sign(word)
        token = self.get_token()
        print(sign, token)
        formdata = {
            "from": "en",
            "to": "zh",
            "query": word,
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": sign,
            "token": token,
        }
        html_json = requests.post(
            url=self.post_url,
            data=formdata,
            headers=self.headers1
        ).json()
        print(html_json)

if __name__ == '__main__':
    spider = BaiduFanyiSpider()
    spider.get_result('hello')