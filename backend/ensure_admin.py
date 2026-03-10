import sys
import os
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User
from app.core import security

def check_create_user():
    db = SessionLocal()
    try:
        username = "Yhorman_Gar23"
        user = db.query(User).filter(User.username == username).first()
        if not user:
            print(f"User {username} not found. Creating...")
            user = User(
                username=username,
                email="yhorman@example.com",
                hashed_password=security.get_password_hash("admin123"),
                full_name="Yhorman Administrator",
                role="ADMIN",
                is_active=True
            )
            db.add(user)
            db.commit()
            print(f"User {username} created successfully with password 'admin123'.")
        else:
            print(f"User {username} already exists.")
            # Reset password just in case
            user.hashed_password = security.get_password_hash("admin123")
            user.role = "ADMIN"
            db.commit()
            print(f"Password for {username} reset to 'admin123' and role to 'ADMIN'.")
    finally:
        db.close()

if __name__ == "__main__":
    # Add project root to path so 'app' module can be found
    sys.path.append(os.getcwd())
    check_create_user()
