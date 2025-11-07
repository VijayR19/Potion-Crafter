from typing import List
from fastapi import APIRouter, status
from dependencies import db_dependency

from models.discovery_model import Discovery
from schemas.discovery_schema import DiscoveryRead
from crud import discovery_crud

router = APIRouter(prefix="/discoveries", tags=["discoveries"])
# Get '/'
@router.get("/", response_model=List[DiscoveryRead], status_code=status.HTTP_200_OK)
def read_discoveries(db: db_dependency) -> List[DiscoveryRead]:
    return discovery_crud.get_all_discoveries(db)