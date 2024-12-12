from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Uvicorn": "I'm alive"}


@app.get('/hello')
async def method_name():
    return {"hola mundo"}

@app.get('/ok')
async def method_name():
    return {"ok vamos"}