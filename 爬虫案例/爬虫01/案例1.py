'''
爬搜狗
1. 定义url https://www.sougou.com
2. 发起请求
3. 获取相应的页面数据
4. 存储
'''
import  requests

# 1. url (CSDN加反扒了!)
# url = 'http://www.sougou.com'
url = 'https://blog.csdn.net/qq_30242609/article/details/53788228#commentBox'
# 2. 发送请求
res = requests.get(url=url)
# 3. 获取页面数据
res_text = res.text
print(res_text)

# 4.存储(保存到数据,txt.csv.表格...)
with open('博文.html',mode='w',encoding='utf8') as f:
    f.write(res_text)
