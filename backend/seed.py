from sqlalchemy.orm import create_engine
from sqlalchemy.orm import sessionmaker

from models.user import User
from.models.potion_model import Rarity, Potion
from models.discovery_model import Discovery

from database import Base, DATABASE_URL

# Create the database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
