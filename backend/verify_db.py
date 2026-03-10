import sys
import os

# Add the current directory to sys.path to allow imports from 'app'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal, engine
from app.models import User
from sqlalchemy import text

def verify():
    print("--- Verificando Conexión y Datos ---")
    try:
        # 1. Probar conexión básica
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print(f"Conexión a PostgreSQL: OK ({result.fetchone()})")
            
        # 2. Consultar usuario
        db = SessionLocal()
        user = db.query(User).filter(User.username == "Yhorman_Gar23").first()
        if user:
            print(f"Usuario encontrado: {user.username}")
            print(f"Rol: {user.role}")
            print(f"Estado Activo: {user.is_active}")
            print("Verificación de datos: OK")
        else:
            print("ERROR: Usuario maestro no encontrado en la base de datos.")
        db.close()
        
    except Exception as e:
        print(f"ERROR durante la verificación: {e}")

if __name__ == "__main__":
    verify()
