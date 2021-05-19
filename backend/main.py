from fastapi import FastAPI
from routers import router as api_router

app = FastAPI(title="Inventory Workshop")

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
