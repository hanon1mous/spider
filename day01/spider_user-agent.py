# 导入请求模块
from urllib import request
# 定义常用变量
url = 'http://maoyan.com/films/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
# 创建请求对象(包装请求)
req = request.Request(url=url,headers=headers)
# 发请求,获取相应对象
response = request.urlopen(req)
# 读取内容
print(response.read().decode('utf-8'))