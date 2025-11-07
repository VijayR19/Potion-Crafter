from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from models.user_model import User
from schemas.user_schema import UserRead, UserCreate

def get_all_users(db: Session) -> List[User]:
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user_create: UserCreate) -> User:
    db_user = user_create.model_dump()
    new_user = User(**db_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user