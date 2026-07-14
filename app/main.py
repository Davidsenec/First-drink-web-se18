from fastapi import FastAPI
from app.config.database import engine, Base
from app.controllers.AuthRoute import router as auth_router
from app.controllers.UserRoute import router as user_router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    print("shutting down")


app = FastAPI(
    title="Party Check-In API",
    description="Backend API for First Drink party check-in management",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(user_router)


@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify that the service is running correctly.
    """
    return {"status": "healthy", "version": "0.1.0"}
