
'''
urllib  不如 request方便
request 需要依赖urllib

urllib依靠参数data来区分get和post请求
有data参数,表示post, 参数书格式必须为bytes
'''
from urllib import request # 请求模块
from urllib import  parse  # 解析模块

data = bytes(parse.urlencode({'uname':'admin','pwd':'123'}),encoding='utf8')
response = request.urlopen('http://httpbin.org/post',data=data)
print(response.read().decode('utf8'))


