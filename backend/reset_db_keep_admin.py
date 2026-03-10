import sys
import os

# Add the current directory to sys.path to allow imports from 'app'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import engine, SessionLocal
from app.models import (
    User, Product, Sale, SaleItem, Supplier, 
    PurchaseOrder, PurchaseOrderItem, StockMovement, AuditLog
)

def reset_data():
    print("--- Iniciando limpieza de datos (Manteniendo Usuarios) ---")
    
    db = SessionLocal()
    try:
        # Tables to truncate in order (respecting foreign keys)
        # We use raw SQL truncate for simplicity and speed, or delete if truncate is blocked by FKs
        tables = [
            "sale_items",
            "sales",
            "purchase_order_items",
            "purchase_orders",
            "stock_movements",
            "audit_logs",
            "products",
            "suppliers"
        ]
        
        with engine.connect() as connection:
            transaction = connection.begin()
            try:
                for table in tables:
                    print(f"Limpiando tabla: {table}...")
                    connection.execute(text(f"DELETE FROM {table}"))
                transaction.commit()
                print("--- Limpieza de datos completada ---")
            except Exception as e:
                transaction.rollback()
                print(f"ERROR durante la limpieza de tablas: {e}")
                return

        print("Verificando usuario administrador...")
        admin = db.query(User).filter(User.username == "Yhorman_Gar23").first()
        if admin:
            print(f"Usuario {admin.username} preservado correctamente.")
        else:
            print("ADVERTENCIA: Usuario administrador no encontrado en la base de datos.")
        
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    reset_data()
