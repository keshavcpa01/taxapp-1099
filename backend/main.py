from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from . import auth, submissions, models
from .database import Base, engine
from .models import User
from .security import get_current_user

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(submissions.router)

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/users/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user
