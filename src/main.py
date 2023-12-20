from typing import Union
import redis

from fastapi import FastAPI

app = FastAPI()
r = redis.Redis(host="redis", port=6379)

@app.get("/")
async def read_root():
    r.incr('hits')
    return {"number of clicks", r.get("hits")}
    

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": "q"}