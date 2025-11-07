# TBD for authentication and user management
from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    avatar_url = Column(String, nullable=True)
    display_name = Column(String, nullable=True)
    #email = Column(String, unique=True, index=True, nullable=False)
    # hashed_password = Column(String, nullable=False)
    discoveries = relationship("Discovery",back_populates="user", cascade="all, delete-orphan")
    

    def __repr__(self):
        return f"<User(username='{self.username}', display_name='{self.display_name}')>"

