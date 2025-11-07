from typing import List
from fastapi import APIRouter, status
from dependencies import db_dependency
from fastapi import HTTPException

from schemas.potion_schema import PotionRead, PotionCreate, PotionUpdate
from crud import potion_crud

router = APIRouter(prefix="/potions", tags=["potions"])
# Get '/'
@router.get("/", response_model=List[PotionRead], status_code=status.HTTP_200_OK)
def read_potions(db: db_dependency) -> List[PotionRead]:
    return potion_crud.get_all_potions(db)

# Get '/{potion_id}'
@router.get("/{potion_id}", response_model=PotionRead, status_code=status.HTTP_200_OK)
def read_potion(potion_id: int, db: db_dependency) -> PotionRead:
    potion = potion_crud.get_potion_by_id(db, potion_id)
    if potion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Potion not found")
    return potion

# Post '/{potion_id}'
@router.post("/", response_model=PotionRead, status_code=status.HTTP_201_CREATED)
def post_potion(create_db: PotionCreate, db: db_dependency) -> PotionRead:
    return potion_crud.create_potion(db, create_db)

# Put '/{potion_id}'
@router.put("/{potion_id}", response_model=PotionRead, status_code=status.HTTP_200_OK)
def put_potion(potion_id: int, update_data: PotionUpdate, db: db_dependency) -> PotionRead:
    potion = potion_crud.update_potion(db, potion_id, update_data)
    if potion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Potion not found")
    return potion   

# Delete '/{potion_id}'
@router.delete("/{potion_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_potion(potion_id: int, db: db_dependency) -> None:
    success = potion_crud.delete_potion(db, potion_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Potion not found")
    return None