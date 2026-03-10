import sys
import os

# Add the current directory to sys.path to allow imports from 'app'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base, SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def main():
    print("--- Creating Admin User: juanma123 ---")
    
    # 1. Ensure tables exist
    print("Ensuring tables exist...")
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Warning/Error creating tables (might be connection issue): {e}")
        return

    # 2. Add user
    db = SessionLocal()
    try:
        username = "juanma123"
        password = "admin123"
        
        user = db.query(User).filter(User.username == username).first()
        if user:
            print(f"User {username} already exists. Updating password...")
            user.hashed_password = get_password_hash(password)
            user.role = "ADMIN"
            user.is_active = True
        else:
            print(f"Creating user {username}...")
            user = User(
                username=username,
                email="juanma@producttracker.com",
                hashed_password=get_password_hash(password),
                full_name="Juan Manuel (Admin)",
                role="ADMIN",
                is_active=True
            )
            db.add(user)
        
        db.commit()
        print(f"User {username} created/updated successfully.")
    except Exception as e:
        print(f"ERROR: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()
