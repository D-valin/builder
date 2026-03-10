import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def patch_database():
    with engine.connect() as conn:
        print("Applying patch for RF36: Partial Receiving...")
        try:
            # Add received_quantity to purchase_order_items
            conn.execute(text("ALTER TABLE purchase_order_items ADD COLUMN IF NOT EXISTS received_quantity INTEGER DEFAULT 0 NOT NULL"))
            conn.commit()
            print("Successfully added received_quantity to purchase_order_items.")
        except Exception as e:
            print(f"Error applying patch: {e}")

if __name__ == "__main__":
    patch_database()
