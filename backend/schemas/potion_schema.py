from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, ConfigDict
from models.potion_model import Rarity, Potion

# Base
class PotionBase(BaseModel):
    name: str
    rarity: Rarity
    effects: List[str] = Field(default_factory=list)
    essences: Dict[str, Any] = Field(default_factory=dict)
    gold_award: int = 0
    xp_award: int = 0

# Create
class PotionCreate(PotionBase):
    signature_hash: str

# Update
class PotionUpdate(BaseModel):
    name: Optional[str] = None
    rarity: Optional[Rarity] = None
    effects: Optional[List[str]] = None
    essences: Optional[Dict[str, Any]] = None
    gold_award: Optional[int] = None
    xp_award: Optional[int] = None
  
# Read (Response)
class PotionRead(PotionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    signature_hash: str
    created_at: datetime
