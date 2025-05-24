# backend/config.py

import os
from dotenv import load_dotenv
from pathlib import Path

# ✅ This line loads .env from the current backend/ folder
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "")
    SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY", "")
    SENDER_EMAIL: str = os.getenv("SENDER_EMAIL", "")

settings = Settings()
