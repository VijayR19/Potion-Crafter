from typing import List
from fastapi import APIRouter, status
from dependencies import db_dependency

from models.discovery_model import Discovery
from schemas.discovery_schema import DiscoveryRead, DiscoveryCreate
from crud import discovery_crud

router = APIRouter(prefix="/discoveries", tags=["discoveries"])
# Get '/'
@router.get("/", response_model=List[DiscoveryRead], status_code=status.HTTP_200_OK)
def read_discoveries(db: db_dependency) -> List[DiscoveryRead]:
    return discovery_crud.get_all_discoveries(db)

# Get '/{discovery_id}'
@router.get("/{discovery_id}", response_model=DiscoveryRead, status_code=status.HTTP_200_OK)
def read_discovery(discovery_id: int, db: db_dependency) -> DiscoveryRead:
    discovery = discovery_crud.get_discovery_by_id(db, discovery_id)
    if discovery is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discovery not found")
    return discovery        

# Post '/'
@router.post("/", response_model=DiscoveryRead, status_code=status.HTTP_201_CREATED)
def create_discovery(discovery_data: DiscoveryCreate, db: db_dependency) -> DiscoveryRead:
    return discovery_crud.create_discovery(db, discovery_data)

# Put '/{discovery_id}'
@router.put("/{discovery_id}", response_model=DiscoveryRead, status_code=status.HTTP_200_OK)    
def update_discovery(discovery_id: int, discovery_data: DiscoveryCreate, db: db_dependency) -> DiscoveryRead:
    discovery = discovery_crud.update_discovery(db, discovery_id, discovery_data)
    if discovery is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discovery not found")
    return discovery    

# Delete '/{discovery_id}'
@router.delete("/{discovery_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_discovery(discovery_id: int, db: db_dependency) -> None:
    success = discovery_crud.delete_discovery(db, discovery_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Discovery not found")
    return None       