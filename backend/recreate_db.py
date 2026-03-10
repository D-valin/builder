import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base
from app.models import (
    User, Product, Sale, SaleItem, Supplier, 
    PurchaseOrder, PurchaseOrderItem, StockMovement, AuditLog, ProductSupplier
)
from app.core.security import get_password_hash
from sqlalchemy.orm import Session
from app.database import SessionLocal

def recreate_db():
    print("--- Recreando base de datos con nuevo esquema (Many-to-Many) ---")
    
    # Truncate all tables using CASCADE for PostgreSQL
    tables = [
        "sale_items", "sales", "purchase_order_items", "purchase_orders", 
        "stock_movements", "audit_logs", "product_supplier", "products", "suppliers", "users"
    ]
    
    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            for table in tables:
                print(f"Limpiando {table}...")
                connection.execute(text(f"TRUNCATE TABLE {table} CASCADE"))
            transaction.commit()
            print("Tablas truncadas con CASCADE.")
        except Exception as e:
            transaction.rollback()
            print(f"Fallo el truncado: {e}")
            # Fallback a drop_all standar
            Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)
    
    print("Base de datos limpia y lista.")
    
    # Re-seed Admin
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
