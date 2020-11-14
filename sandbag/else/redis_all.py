
import redis 
r=redis.Redis(host='hank-001.bwwxt6.0001.use1.cache.amazonaws.com', port=6379)

for key in r.scan_iter():
   key = str(key)
   value =str(r.get(key))
   print(key+" : " + value)