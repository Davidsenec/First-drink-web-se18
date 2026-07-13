from fastapi import FastAPI

app = FastAPI(
    title="Party Check-In API",
    description="Backend API for First Drink party check-in management",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    """
    Health check endpoint to verify that the service is running correctly.
    """
    return {"status": "healthy", "version": "0.1.0"}
