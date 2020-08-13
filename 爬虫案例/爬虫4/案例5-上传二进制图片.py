import  urllib3

# 模式:read bytes 读取二进制
with open('img2.jpg',mode='rb') as f:
    file_read = f.read()

url = "http://httpbin.org/post"
pools = urllib3.PoolManager()
response = pools.request("POST",url=url,body=file_read,headers={"Context-Type":"images/jpeg"})
print(response.data.decode())