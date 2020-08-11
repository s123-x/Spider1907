'''
知乎
https://www.zhihu.com
'''
import  requests
# 1.url
#url = 'https://www.zhihu.com'
url = 'https://blog.csdn.net/qq_30242609/article/details/53788228#commentBox'
# 指定请求头,记性UA伪装(伪装为浏览器)
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
#2.请求(知乎加反扒,返回就错误页面或空页面)
respone =  requests.get(url,headers=headers)
# 3. 获取返回文本
#print(respone.text)
with open('博文2.html',mode='w',encoding='utf8') as f:
    f.write(respone.text)

