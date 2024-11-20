DATABASE_CONFIG = {
    "connections": {
        "default": "postgres://username:password@localhost:5432/fastapi_db"
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],  # Include Aerich for migrations
            "default_connection": "default",
        },
    },
}
