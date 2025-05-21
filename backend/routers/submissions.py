from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from .security import get_current_user
from typing import List

router = APIRouter()

@router.post("/submissions", response_model=schemas.SubmissionOut)
def create_submission(
    submission: schemas.SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_submission = models.Submission(
        **submission.dict(),
        user_id=current_user.id
    )
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)
    return new_submission

@router.get("/submissions", response_model=List[schemas.SubmissionOut])
def get_user_submissions(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.Submission).filter_by(user_id=current_user.id).all()
