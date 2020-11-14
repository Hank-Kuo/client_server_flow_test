import redis

r = redis.Redis(host='hank-001.bwwxt6.0001.use1.cache.amazonaws.com', port=6379)

r.rpush('alan_user','ec2-3-84-146-137.compute-1.amazonaws.com','','false')
# # user , endpoint , error , boolean 
r.zadd("score",{'alan':0})

# #print(r.zincrby(name=score,value=hank,amount=10))
for key in r.scan_iter():
    r.delete(k)