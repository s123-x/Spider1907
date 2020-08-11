'''
爬取json数据
url  http://httpbin.org/get
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
'''
import  requests
url = 'http://httpbin.org/get'
headers ={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 发送请求
response = requests.get(url=url,headers=headers)
# 获取结果
print(response.text)
# 解析为json
res2 = response.json()
print(res2)
print('我的IP%s'%res2.get('origin'))

# 保存
with open('a1.txt',mode='w',encoding='utf8') as f:
    f.write(response.text)
