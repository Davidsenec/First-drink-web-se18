import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.config.database import get_db, SessionLocal
from app.controllers.auth_route import router as auth_router
from app.controllers.user_route import router as user_router
from app.controllers.admin_route import router as admin_router
from app.init_db import seed_admin
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("ENV") == "development":
        db = SessionLocal()
        try:
            seed_admin(db)
        except Exception as e:
            print(f"Failed to auto-seed admin on startup: {e}")
        finally:
            db.close()
    yield


app = FastAPI(
    title="Party Check-In API",
    description="Backend API for First Drink party check-in management",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(admin_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
def health_check(db: Session = Depends(get_db)):
    """
    Health check endpoint to verify that the service is running
    and the database connection is alive.
    """
    health_status = {"status": "healthy", "version": "0.1.0", "database": "healthy"}

    try:
        # Run a simple, lightweight query to check connection health
        db.execute(text("SELECT 1"))
    except Exception as e:
        # If the database query fails, log the error and mark DB as unhealthy
        print(f"Database health check failed: {e}")
        health_status["status"] = "unhealthy"
        health_status["database"] = "unhealthy"
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=health_status
        )

    return health_status
