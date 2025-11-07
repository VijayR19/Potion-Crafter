from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user_model import User
from models.potion_model import Rarity, Potion
from models.discovery_model import Discovery

from database import Base, DATABASE_URL

# Create the database engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_database(drop=True):
    # Create all tables
    if drop:
        print("Dropping existing database tables...")
        Base.metadata.drop_all(bind=engine)
    
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

    # Create a new session
    db = SessionLocal()

    try:
        # Seed Users
        print("clearing existinng rows...")
        db.query(Discovery).delete()
        db.query(Potion).delete()
        db.query(User).delete()
        db.commit()

        print("Inserting seed rows...")

        user = User(username="player_one", display_name="Player One")
        db.add(user)
        db.flush()  #get user.id

        # Potions
        p1 = Potion(
            name="Whisker Draught of Mist",
            rarity = Rarity.COMMON,
            effects=["Luck +1"],
            essences={"weather": "mist", "prime": False},
            signature_hash="sig_common_001",
            gold_award=5,
            xp_award=5,
        )
        p2 = Potion(
            name="Prime Sphinx Elixir of Tempest",
            rarity = Rarity.RARE,
            effects=["Luck +2", "Focus +1"],
            essences={"weather": "rain", "prime": True, "wind": "breeze"},
            signature_hash="sig_rare_073",
            gold_award=20,
            xp_award=15,
        )

        db.add_all([p1, p2])
        db.flush()  #get potion ids

        # Discoveries (history)
        d1 = Discovery(
            potion_id=p1.id,
            user_id=user.id if hasattr(Discovery, "user_id") else None,
            awarded_gold=p1.gold_award,
            awarded_xp=p1.xp_award,
            first_time_discovery=True
        )

        d2 = Discovery(
            potion_id=p2.id,
            user_id=user.id if hasattr(Discovery, "user_id") else None,
            awarded_gold=int(p2.gold_award * 1.5),
            awarded_xp = p2.xp_award + 5,
            first_time_discovery=True
            )
        
        db.add_all([d1, d2])
        db.commit()
        print("Seed data inserted successfully.")

    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database(drop=True)
