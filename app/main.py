from fastapi import FastAPI
from app.core.config import settings
from app.core.cors import add_cors_middleware
from app.db.init_db import init_db, close_db
from app.api.v1.endpoints import quiz


# Lifespan event handler
async def lifespan_event(app: FastAPI):
    # Called during startup
    await init_db()

    # Yield control back to FastAPI
    yield

    # Called during shutdown
    await close_db()


# Initialize the FastAPI app
app = FastAPI(title=settings.app_name, debug=settings.debug, lifespan=lifespan_event)

# Add CORS middleware
add_cors_middleware(app)

# Include routes
app.include_router(quiz.router, prefix="/api/v1")
