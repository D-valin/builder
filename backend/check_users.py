from app.database import SessionLocal
from app.models.user import User

def check_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        print(f"Total users: {len(users)}")
        for u in users:
            print(f"User: {u.username}, Role: {u.role}, Active: {u.is_active}")
    finally:
        db.close()

if __name__ == "__main__":
    check_users()
