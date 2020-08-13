import  urllib3

with open('1.txt',mode='r+',encoding='utf-8') as f:
    file_read = f.read()

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
url = "http://httpbin.org/post"
pools = urllib3.PoolManager()
response = pools.request("POST",url=url,headers=headers,
                         fields={'mytxt':('1.txt',file_read,'text/plain')})
print(response.data.decode())