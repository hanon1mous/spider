import requests

url = 'http://code.tarena.com.cn/AIDCode/aid1911/00-xunlianying/day05/day05.zip'
auth = ('tarenacode', 'code_2013')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
res = requests.get(url=url, auth=auth, headers=headers)
filename = url.split('/')[-1]
with open(filename, 'wb') as f:
    f.write(res.content)