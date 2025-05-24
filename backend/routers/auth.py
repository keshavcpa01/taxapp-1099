from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from backend import models, schemas
from backend.database import get_db
from backend.utils import auth as auth_utils
from backend.security import get_current_user

router = APIRouter(
    prefix="",
    tags=["Auth"]
)

# 🔐 Register a new user
@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )

    hashed_password = auth_utils.hash_password(user.password)
    new_user = models.User(
        username=user.username,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# 🔑 Login user and return JWT token
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not db_user or not auth_utils.verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = auth_utils.create_access_token(db_user.id)
    return {"access_token": token, "token_type": "bearer"}
