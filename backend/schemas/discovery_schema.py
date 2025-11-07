from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from schemas.potion_schema import PotionRead
from schemas.user_schema import UserRead

# Discovery Base
class DiscoveryBase(BaseModel):
    awarded_gold: int = 0
    awarded_xp: int = 0
    first_time_discovery: bool = False

# Discovery Create
class DiscoveryCreate(DiscoveryBase):
    potion_id: int
    # keep user_id optional to support single player mode
    user_id: Optional[int] = None

# Discovery Read (Response)
class DiscoveryRead(DiscoveryBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    potion_id: int
    user_id: Optional[int] = None
    created_at: datetime

# Discovery Read with Relations
class DiscoveryReadWithRelations(DiscoveryRead):
    potion: PotionRead
    user: Optional[UserRead] = None