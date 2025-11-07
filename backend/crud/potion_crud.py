from typing import List, Optional
from sqlalchemy.orm import Session
from models.potion_model import Potion
from schemas.potion_schema import PotionCreate

def get_all_potions(db: Session) -> List[Potion]:
    return db.query(Potion).all()

def get_potion_by_id(db: Session, potion_id: int) -> Optional[Potion]:
    return db.query(Potion).filter(Potion.id == potion_id).first()

def create_potion(db: Session, create_db: PotionCreate) -> Potion:
    new_order = create_db.model_dump()
    db_potion = Potion(**new_order)
    db.add(db_potion)
    db.commit()
    db.refresh(db_potion)
    return db_potion