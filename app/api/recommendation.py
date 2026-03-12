from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.core.auth import get_current_user
from app.services.recommender import get_recommendation
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.get(\/recommendations/\)
def get_daily_recommendation(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_recommendation(current_user.id, db, current_user.level)
