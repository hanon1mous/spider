import requests
url = 'http://www.baidu.com/'
headers = {'Use-Agent': 'xxxxxx'}

res = requests.get(url, headers=headers)
res.encoding = 'utf-8'
# print(res.text)
print(res.status_code)
print(res.url)

