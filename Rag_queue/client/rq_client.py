from redis import Redis 
from rq import Queue

queue = Queue(connection=Redis(
    host="http://localhost:3030",
    port="6379"
))

