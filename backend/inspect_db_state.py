import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy import inspect, text
from app.database import engine

def check_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f"Tablas encontradas: {tables}")
    
    with engine.connect() as connection:
        for table in tables:
            result = connection.execute(text(f"SELECT COUNT(*) FROM {table}"))
            count = result.scalar()
            print(f" - {table}: {count} registros")

if __name__ == "__main__":
    check_tables()
