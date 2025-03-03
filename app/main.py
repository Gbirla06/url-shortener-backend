from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import db
from app.routes.shorturl import router as url_router
from app.routes.statics import router as statics_router

# Initialize the FastAPI application
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    """
    Home endpoint to check if the service is running.

    Returns:
        dict: A welcome message.
    """
    return {"Message" : "URL Shortener Service"}

@app.get("/db-health")
def db_health():
    """
    Endpoint to check the health of the MongoDB connection.

    Returns:
        dict: A status message indicating whether MongoDB is connected or not.
    """
    try:
        db.command("ping")
        return {"status": "connected", "message": "MongoDB is connected!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Include the URL shortening routes
app.include_router(url_router, prefix="/url", tags=["URL"])

# Include the statistics routes
app.include_router(statics_router, prefix="/statics", tags=["STATICS"])
