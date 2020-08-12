'''
urllib.reqeust模块中代理方法
Proxy: 代理
request.ProxyHandler(代理IP列表)

'''
from urllib import  request
url='http://httpbin.org/get'

# 创建代理
proxy_handler = request.ProxyHandler({
     'http':'113.194.29.4:9999',
})
# 创建代理打开器
opener = request.build_opener(proxy_handler)
# 打开
response = opener.open(url)
print(response.read())





