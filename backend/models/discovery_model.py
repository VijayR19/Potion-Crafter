from sqlalchemy import Column, Integer, ForeignKey, Boolean
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Discovery(Base):
        __tablename__ = "discoveries"

        id = Column(Integer, primary_key=True, index=True)
        user_id = Column(ForeignKey("users.id"), index=True, nullable=False)
        potion_id = Column(ForeignKey("potions.id"), index=True, nullable=False)
        awarded_gold = Column(Integer, nullable=False, default=0)
        awarded_xp = Column(Integer, nullable=False, default=0)
        first_time_discovery = Column(Boolean, nullable=False, default=False)
        created_at = Column(DateTime(timezone=True), server_default=func.now())# 1 for True, 0 for False

        # relationships
        user = relationship("User", back_populates="discoveries")
        potion = relationship("Potion", back_populates ="discoveries")

        def __repr__(self):
                return f"<Discovery(potion_id={self.potion_id}, gold={self.awarded_gold}, xp={self.awarded_xp}, first={self.first_time_discovery})>"

  