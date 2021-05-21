import uvicorn
from fastapi import FastAPI
from routers import router as api_router
from tortoise.contrib.fastapi import register_tortoise


def init_app():
    app = FastAPI(title="Inventory Workshop")
    app.include_router(api_router)
    return app

app = init_app()


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models.inventory']},
    generate_schemas=True,
    add_exception_handlers=True
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
