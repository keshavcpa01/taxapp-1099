# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import auth, submissions  # adjust imports as needed
from .config import settings

app = FastAPI()

# Print to verify it's working (optional)
print("DB URL:", settings.DATABASE_URL)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(submissions.router)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/config-check")
def config_check():
    return {
        "database_url": settings.DATABASE_URL,
        "sender_email": settings.SENDER_EMAIL
    }
