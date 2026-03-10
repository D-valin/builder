from app.database import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def repair_admin():
    db = SessionLocal()
    try:
        username = "Yhorman_Gar23"
        password = "123456789Ae"
        email = "yhormangarcesballestas@gmail.com"
        
        user = db.query(User).filter(User.username == username).first()
        if user:
            print(f"User {username} found. Updating credentials...")
            user.email = email
            user.hashed_password = get_password_hash(password)
            user.role = "ADMIN"
            user.is_active = True
        else:
            print(f"User {username} not found. Creating new admin...")
            user = User(
                username=username,
                email=email,
                hashed_password=get_password_hash(password),
                role="ADMIN",
                is_active=True,
                full_name="Yhorman Garcés"
            )
            db.add(user)
        
        db.commit()
        print("Admin user repaired successfully.")
    except Exception as e:
        print(f"Error repairing admin: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    repair_admin()
