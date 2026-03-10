import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load env from backend/.env
load_dotenv("backend/.env")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL = os.getenv("database_url")

def patch_db():
    if not DATABASE_URL:
        print("ERROR: No se encontró DATABASE_URL")
        return

    print(f"Conectando a la DB para crear tablas de devoluciones...")
    engine = create_engine(DATABASE_URL)
    
    # Normally Base.metadata.create_all handles this if called in main.py
    # But since we are using uvicorn --reload, sometimes it's faster to verify/run manual SQL 
    # for new tables if any issue arises. 
    # However, let's just let it be handled by main.py logic mostly.
    # We will just verify if the tables exist.
    
    with engine.connect() as conn:
        try:
            # We'll just run a harmless query to check if the table exists, 
            # if not we rely on the app reload which calls create_all()
            print("Verificando existencia de tabla 'returns'...")
            conn.execute(text("SELECT 1 FROM returns LIMIT 1"))
            print("Tablas ya existen.")
        except Exception:
            print("Tablas no detectadas. El servidor debería crearlas al reiniciar.")
            print("Si el servidor no las crea, favor reiniciar manualmente uvicorn.")

if __name__ == "__main__":
    patch_db()
