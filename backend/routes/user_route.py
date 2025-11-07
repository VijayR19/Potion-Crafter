from typing import List
from fastapi import APIRouter, status
from dependencies import db_dependency
from fastapi import HTTPException

from schemas.user_schema import UserRead, UserCreate
from crud import user_crud

router = APIRouter(prefix="/users", tags=["users"])
# Get '/'
@router.get("/", response_model=List[UserRead], status_code=status.HTTP_200_OK)
def read_users(db: db_dependency) -> List[UserRead]:
    return user_crud.get_all_users(db)

# Get '/{user_id}'
@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: db_dependency) -> UserRead:
    user = user_crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user 

# Post '/'
@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreate, db: db_dependency) -> UserRead:
    return user_crud.create_user(db, user_create)
