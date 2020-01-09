# 导入请求模块
from urllib import request
url = 'http://httpbin.org/get'
response = request.urlopen(url)
print(response.read().decode('utf-8'))
