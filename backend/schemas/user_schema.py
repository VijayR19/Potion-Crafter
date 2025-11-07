from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

# User
class UserBase(BaseModel):
    username: str
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None

# Create
class UserCreate(UserBase):
    # Add email / password later if you want authentication
    pass

# Read
class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime