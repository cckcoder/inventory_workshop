from fastapi import FastAPI
from routers import inventorys

app = FastAPI(title="Inventory Workshop")

app.include_router(inventorys.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
