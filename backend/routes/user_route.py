from typing import List
from fastapi import APIRouter, status
from dependencies import db_dependency

from schemas.user_schema import UserRead
from crud import user_crud

router = APIRouter(prefix="/users", tags=["users"])
# Get '/'
@router.get("/", response_model=List[UserRead], status_code=status.HTTP_200_OK)
def read_users(db: db_dependency) -> List[UserRead]:
    return user_crud.get_all_users(db)