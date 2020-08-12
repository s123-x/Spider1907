'''
使用urllib发起请求
请求模块request
百度:返回的结果只有页面结构,无内容!
因为:百度检测到不是通过浏览器访问的!
'''
from urllib import request
url ='https://www.baidu.com'
# urllib中的reqeust模块的urlopen方法可以打开页面,页面的数据格式bytes类型,需要decode解码转化为字符串
response =request.urlopen(url=url,data=None,timeout=10) # 超时时间10s
#读取,解码
print(type(response.read()))
res = response.read().decode('utf-8')
print(type(res))
