import  urllib3
import  json #导入python自带的json模块

# 紧用于爬后台接口!!!
# JSON发起请求时,需要把数据转化为json字符串格式, 在请求头中需要指定内容类型为application/json
data = {'uname':'zhangsan'}
url = "http://httpbin.org/post"
encode_data = json.dumps(data).encode() # 数据编码

pools = urllib3.PoolManager()

response =pools.request('POST',url=url,body=encode_data,headers={'Context-Type':'application/json'})
print(response.data.decode())




