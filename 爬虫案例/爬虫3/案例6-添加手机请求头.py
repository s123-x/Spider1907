'''
添加手机请求头,模拟手机浏览器

'''
from urllib import  request,parse

url = 'http://httpbin.org/post'
dict = {'name': 'admin'}
# 参数转化为byte
data = bytes(parse.urlencode(dict), encoding='utf8')
headers={
    'User-Agent': 'Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5',
}
# 自己组装的请求
req  =request.Request(url=url,data=data,headers=headers)
response = request.urlopen(req)
print(response.status)
print(response.read().decode('utf-8'))