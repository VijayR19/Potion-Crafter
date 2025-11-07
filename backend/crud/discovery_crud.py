from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from models.discovery_model import Discovery
from schemas.discovery_schema import DiscoveryRead

def get_all_discoveries(db: Session) -> List[Discovery]:
    return db.query(Discovery).all()