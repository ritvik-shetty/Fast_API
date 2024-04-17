from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"Message":"Hello World"}


@app.post('/')
async def post():
    return {"Message":"Hello from Post"}


@app.put('/')
async def put():
    return {"Message":"Hello from Put"}


@app.get('/items/')
async def list_items():
    return {"Message":"List of items route"}

@app.get('/items/{item_id}')
async def list_items(item_id:int):  
    return {"List of items:":item_id}  # For string we can change the type cast to str 
