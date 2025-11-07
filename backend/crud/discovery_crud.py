from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from models.discovery_model import Discovery
from schemas.discovery_schema import DiscoveryRead, DiscoveryCreate

def get_all_discoveries(db: Session) -> List[Discovery]:
    return db.query(Discovery).all()

def get_discovery_by_id(db: Session, discovery_id: int) -> Discovery:
    return db.query(Discovery).filter(Discovery.id == discovery_id).first()

def create_discovery(db: Session, discovery_data: DiscoveryCreate) -> Discovery:
    new_discovery = discovery_data.model_dump()
    new_discovery = Discovery(**new_discovery)
    db.add(new_discovery)
    db.commit()
    db.refresh(new_discovery)
    return new_discovery

def update_discovery(db: Session, discovery_id: int, discovery_data: DiscoveryCreate) -> Discovery:
    discovery = db.query(Discovery).filter(Discovery.id == discovery_id).first()
    if discovery:
        for key, value in discovery_data.model_dump().items():
            setattr(discovery, key, value)
        db.commit()
        db.refresh(discovery)
    return discovery    

def delete_discovery(db: Session, discovery_id: int) -> bool:
    discovery = db.query(Discovery).filter(Discovery.id == discovery_id).first()
    if discovery:       
        db.delete(discovery)
        db.commit()
        return True
    return False