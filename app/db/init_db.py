from tortoise import Tortoise
from app.core.config import settings


async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        # db_url=settings.database_url,
        modules={"models": ["app.db.models"]},
    )
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
