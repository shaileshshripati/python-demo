import redis

redis_host = "demoredis924.redis.cache.windows.net"
redis_password = "t5tTSWS1sRxoUbZHRkYjyLMrEUnhaixGuAzCaPJFbS0="

r = redis.StrictRedis(host=redis_host, password=redis_password, ssl=True)

# Store data in the cache
r.set("example_key", "example_value")

# Retrieve data from the cache
value = r.get("example_key")
print(value)
