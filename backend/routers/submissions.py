from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from typing import List
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from backend import models, schemas
from backend.database import get_db
from backend.security import get_current_user

router = APIRouter(
    prefix="/submissions",
    tags=["Submissions"]
)

# 📝 Create a new 1099 submission
@router.post("/", response_model=schemas.SubmissionOut)
def create_submission(
    submission: schemas.SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    try:
        new_submission = models.Submission(
            **submission.dict(),
            user_id=current_user.id
        )
        db.add(new_submission)
        db.commit()
        db.refresh(new_submission)
        return new_submission
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Submission failed: {str(e)}"
        )

# 📥 Get all submissions for current user
@router.get("/", response_model=List[schemas.SubmissionOut])
def get_user_submissions(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    try:
        return db.query(models.Submission).filter_by(user_id=current_user.id).all()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Could not retrieve submissions: {str(e)}"
        )

# ✉️ Email a confirmation for a specific submission
@router.post("/{submission_id}/email")
def email_submission(
    submission_id: int = Path(..., title="Submission ID"),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    submission = db.query(models.Submission).filter_by(
        id=submission_id, user_id=current_user.id
    ).first()

    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    if not submission.payer_email:
        raise HTTPException(status_code=400, detail="Payer email is missing in the submission.")

    try:
        sg = SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
        message = Mail(
            from_email='noreply@yourdomain.com',
            to_emails=submission.payer_email,
            subject='1099-NEC Submission Confirmation',
            html_content=f"""
                <p>Hello,</p>
                <p>Your 1099-NEC submission was received successfully.</p>
                <p><strong>Submission ID:</strong> {submission.id}</p>
                <p><strong>Submitted on:</strong> {submission.created_at.strftime('%Y-%m-%d')}</p>
                <p>Thank you,<br>Your Company</p>
            """
        )
        response = sg.send(message)
        return {
            "message": "Email sent successfully",
            "status_code": response.status_code
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
