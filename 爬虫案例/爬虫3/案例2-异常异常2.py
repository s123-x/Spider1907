import socket
import urllib.request

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    # 日常开发直接统一捕获,没有必要使用urllib.error
except Exception as e:
    print('错误:%s'%e)