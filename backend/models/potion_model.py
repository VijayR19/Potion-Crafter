from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import JSON
from database import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime
import enum

class Rarity(str, enum.Enum):
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    MYTHIC = "MYTHIC"

    
class Potion(Base):
        __tablename__ = "potions"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, nullable=False)
        rarity=Column(Enum(Rarity), nullable=False)
        effects = Column(JSON, nullable=False, default=list) 
        essences = Column(JSON, nullable=False, default=dict)
        signature_hash = Column(String, unique=True, index=True)
        gold_award = Column(Integer)
        xp_award = Column(Integer)
        created_at = Column(DateTime(timezone=True), server_default=func.now())

        def __repr__(self):
             return f"<Potion(name='{self.name}', rarity='{self.rarity.value}', signature='{self.signature_hash[:8]}')>"