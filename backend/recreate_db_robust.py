import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import text, inspect
from app.database import engine, Base
from app.models import * # Ensure all models are loaded
from app.core.security import get_password_hash
from app.database import SessionLocal
from app.models.user import User

def recreate_db():
    print("--- Recreando base de datos con CASCADE total ---")
    
    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            # 1. Obtener todas las tablas existentes
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            
            # 2. Dropear cada tabla con CASCADE
            for table in tables:
                print(f"Dropeando tabla {table} con CASCADE...")
                connection.execute(text(f"DROP TABLE IF EXISTS {table} CASCADE"))
            
            transaction.commit()
            print("Tablas eliminadas exitosamente.")
        except Exception as e:
            transaction.rollback()
            print(f"Error durante el DROP CASCADE: {e}")
            return

    # 3. Recrear todo segun los modelos actuales
    print("Creando nuevas tablas...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas.")
    
    # 4. Re-seed Admin
    db = SessionLocal()
    try:
        admin_user = User(
            username="Yhorman_Gar23",
            full_name="Yhorman Garcia",
            email="yhormangarcia07@gmail.com",
            hashed_password=get_password_hash("Yhorman_Gar23"),
            role="ADMIN"
        )
        db.add(admin_user)
        db.commit()
        print(f"Usuario {admin_user.username} recreado correctamente.")
    except Exception as e:
        print(f"Error recreando admin: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    recreate_db()
