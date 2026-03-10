import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, SessionLocal, Base
from app.models.user import User
from sqlalchemy import text, inspect

def check():
    print("=== REVISIÓN COMPLETA DE BASE DE DATOS ===")
    
    # 1. Probar conexión básica
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            version = result.fetchone()
            print(f"[OK] Conexión a PostgreSQL: {version[0][:60]}")
    except Exception as e:
        print(f"[ERROR] No se puede conectar a PostgreSQL: {e}")
        return

    # 2. Verificar que la base de datos es product_tracker
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT current_database()"))
            dbname = result.fetchone()[0]
            print(f"[OK] Base de datos actual: {dbname}")
    except Exception as e:
        print(f"[ERROR] No se puede obtener nombre de BD: {e}")

    # 3. Verificar tablas existentes
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"[OK] Tablas encontradas ({len(tables)}): {tables}")
    except Exception as e:
        print(f"[ERROR] No se pueden listar tablas: {e}")
        return

    if not tables:
        print("[WARN] ¡NO HAY TABLAS! Ejecuta init_db.py para crear las tablas.")
        return

    # 4. Contar registros en cada tabla
    db = SessionLocal()
    try:
        for table in tables:
            try:
                result = db.execute(text(f'SELECT COUNT(*) FROM "{table}"'))
                count = result.fetchone()[0]
                print(f"  - {table}: {count} registros")
            except Exception as e:
                print(f"  - {table}: ERROR - {e}")
    finally:
        db.close()

    # 5. Verificar usuario juanma123
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == "juanma123").first()
        if user:
            print(f"[OK] Usuario 'juanma123' existe - rol: {user.role}, activo: {user.is_active}")
        else:
            print("[WARN] Usuario 'juanma123' NO encontrado en la BD.")
    except Exception as e:
        print(f"[ERROR] No se puede consultar usuarios: {e}")
    finally:
        db.close()

    print("=== FIN DE REVISIÓN ===")

if __name__ == "__main__":
    check()
