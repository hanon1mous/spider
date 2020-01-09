# 在百度中输入要搜索的内容，把响应内容保存到本地文件
from urllib import request
from urllib import parse
# 定义常用变量
word = input('请输入搜索名称:')
url = 'http://www.baidu.com/s?'
headers = {'Cookie': 'BAIDUID=8CFC882687FF7DE0E06CBA0BE47E402B:FG=1; PSTM=1561427303; BIDUPSID=01E1833B48818C2D9DA39D9EF1F75CFA; BDUSS=mVaQWotZkQwanhUTFZadjVDbTJzcDNYYUozcjkxWlJ1Z0FrS2tpVkFHMEZaanBkRVFBQUFBJCQAAAAAAAAAAAEAAADY7e7Ss8zQ8sDgyMvUswAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXZEl0F2RJdS; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1469_21096_30210_18559_30284; BDSFRCVID=TGDOJeC62Cizoa5wp-i0EHtYoI0HMxOTH6aoGmoTDlPL44TuU_w4EG0Pfx8g0KubtobAogKK0mOTHvstVeAMSjTl8qrZSkgJmnNYtf8g0M5; H_BDCLCKID_SF=tJ4f_D0ytKD3qR5gMJ5q-n3HKUrL5t_XbI6y3JjOHJOoDDv2QUOcy4LdjG5maRTyKRTfQT6Vtp51fMTvyj31XJkg3-Aq54RxaCOnKnRxBI-MS-5aBntMQfbQ0MjOqP-jW5TaLn7t0R7JOpkxhfnxybKy5bj-3xrg2HnQVPj-yfOOepczhxTZ5-5bbN3ut6T2-DA_oD-XJIOP; delPer=0; BD_CK_SAM=1; PSINO=2; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; COOKIE_SESSION=6_1_7_7_0_6_0_0_7_3_2_1_0_0_0_0_0_1576812942_1576827522%7C9%231381209_255_1576812939%7C9; BDSVRTM=368; H_PS_645EC=7123lcQFlquSOoc2XBZG4IzAZSnohwG3cznM%2F%2FqoRwOoYId9npYSJyupT7I'}
query_string_dict = {'wd': word}
# 编码
query_string_dict = parse.urlencode(query_string_dict)
url = url + '{}'.format(query_string_dict)
# 包装请求头
req = request.Request(url=url,headers=headers)
# 发送请求,获得响应体
res = request.urlopen(req)
# 解析响应体
html = res.read().decode('utf-8')
filename = '{}.html'.format(word)
with open(filename, 'w', encoding='utf-8') as f:
    f.write(html)
