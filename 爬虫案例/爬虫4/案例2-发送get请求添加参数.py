import urllib3

'''
发送请求传参数
'''
pools = urllib3.PoolManager(num_pools=10)
url = "http://httpbin.org/post"
fields={'name':'admin'}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
response = pools.request("POST",url=url,fields=fields,headers=headers)
print(response.status)
print(response.data.decode())