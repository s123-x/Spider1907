'''
爬百度翻译
'''
import  requests
# 1. 地址
url ='https://fanyi.baidu.com/sug'
# 2. 发请求加请求头
h ={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 请求加参数
print('万能英译汉:')
kw =input('请输入一个单词:')
mydata = {'kw':kw}
# get方法表示get请求, post表示post请求
response = requests.post(url,headers=h,data=mydata) # url参数,headers请求头,data参数
print(response.json()) #获取json数据



