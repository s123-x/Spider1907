'''
百度产品列表
熟悉: requests 模拟相关方法
'''
import  requests

h ={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
resposne = requests.get('https://www.baidu.com/more',headers=h)

print(resposne.status_code) # 响应的状态码 200 表示请求网站成功
resposne.encoding='utf-8' # 设置相应的字符编码
print(resposne.text) # 获取响应文本
# print(resposne.json()) # 获取响应json数据
print(resposne.headers) # 获取响应的头资料!
print(resposne.content) #获取响应内容
