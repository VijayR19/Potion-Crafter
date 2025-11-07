# backend/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()  # Loads .env file if present

# If you’re using Postgres, add this to your .env:
# DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/potion_crafter_db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./potion_crafter.db")

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
