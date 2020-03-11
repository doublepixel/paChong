import redis
import json
import pymongo

clinet = redis.StrictRedis('118.190.201.248', 6379)
mclient = pymongo.MongoClient("localhost", 27017)
db = mclient.test4  # 库
data = clinet.lrange('nc:items', 0, -1)
for d in data:
    db.news.insert(json.loads(d.decode('utf8')))
