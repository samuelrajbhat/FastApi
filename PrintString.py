from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get("/")
async def read_root():
    Rakesh = ["I am  Rakesh"]
    return {"Hello": Rakesh}

@app.get("/item/{item_id}")
async def read_item(item_id: int, q: Optional[str]= "hello"):
    return {"item_id= ": item_id, "q": q}
# It returns the simple string
