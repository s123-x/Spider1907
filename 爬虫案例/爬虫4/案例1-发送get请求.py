import  urllib3

# 创建连接池(可以同时打开N个请求通道)
pools = urllib3.PoolManager()
# 通过连接池对象发送请求
respone = pools.request('GET','https://cuiqingcai.com/')
print(respone.status) #获取状态
print(respone.data.decode())
