from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from backend.routers import auth, submissions
from backend.config import settings
from dotenv import load_dotenv
load_dotenv()


# ✅ Basic token URL for FastAPI's built-in Swagger Auth
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Routers
app.include_router(auth.router)
app.include_router(submissions.router)

# ✅ Health check
@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/config-check")
def config_check():
    return {
        "database_url": settings.DATABASE_URL,
        "sender_email": settings.SENDER_EMAIL,
    }
