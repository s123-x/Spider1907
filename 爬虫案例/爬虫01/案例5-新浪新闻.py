import  requests

url ='https://https://search.sina.com.cn/?'
h ={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
key = input('请输入要找的新闻关键字:')
params = {'q': key,'range': 'all','c':'news','sort':'time'}
response = requests.get(url=url,headers=h,params=params) #get的参数
print(response.content)

