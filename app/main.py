from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import db
from app.routes.shorturl import router as url_router
from app.routes.statics import router as statics_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    return {"Message" : "URL Shortener Service"}

@app.get("/db-health")
def db_health():

    try:
        db.command("ping")
        return {"status": "connected", "message": "MongoDB is connected!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

app.include_router(url_router,prefix="/url", tags=["URL"])
app.include_router(statics_router,prefix="/statics", tags=["STATICS"])
