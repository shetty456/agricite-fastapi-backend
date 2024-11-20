from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routes import router
from app.config import DATABASE_CONFIG

app = FastAPI()
app.include_router(router)

register_tortoise(
    app,
    config=DATABASE_CONFIG,
    generate_schemas=True,  # Automatically create tables (disable in production)
    add_exception_handlers=True,
)
