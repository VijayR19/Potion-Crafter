from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from models.user_model import User
from schemas.user_schema import UserRead

def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()