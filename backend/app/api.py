from fastapi import FastAPI
from app.routers import router as api_router
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

origins = [
    'http://localhost:8080'
    , 'http://localhost:8081'
]


def init_app():
    app_config = FastAPI(title="Inventory Workshop")
    app_config.include_router(api_router)
    app_config.mount("/static", StaticFiles(directory="app/static"), name="static")
    app_config.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app_config


app = init_app()


@app.get("/")
async def root():
    return {"message": "Hello Welcome to Inventory Workshop"}


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['app.models.inventory', 'app.models.user']},
    generate_schemas=True,
    add_exception_handlers=True
)

