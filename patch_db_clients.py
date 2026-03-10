import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Try loading from backend/.env
load_dotenv("backend/.env")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    # Try alternate name if different
    DATABASE_URL = os.getenv("database_url")

def patch_db():
    if not DATABASE_URL:
        print("ERROR: No se encontró DATABASE_URL en el archivo .env")
        return

    print(f"Conectando a la DB: {DATABASE_URL}")
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Verificando tabla 'sales' para la columna 'client_id'...")
        try:
            # First, make sure Base.metadata.create_all would have run by now
            # because the server is on --reload. If not, this might fail if 'clients' table doesn't exist.
            # But the server should have created it on startup/reload.
            
            # Add column to sales
            conn.execute(text("""
                ALTER TABLE sales ADD COLUMN IF NOT EXISTS client_id INTEGER REFERENCES clients(id);
            """))
            conn.commit()
            print("Columna 'client_id' agregada exitosamente a 'sales'.")
        except Exception as e:
            print(f"Error al parchear la DB: {e}")

if __name__ == "__main__":
    patch_db()
