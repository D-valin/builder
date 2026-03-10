import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv(dotenv_path="backend/.env")
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def patch_database():
    with engine.connect() as conn:
        print("Applying patch for RF40: Supplier Credit & Terms...")
        try:
            # Add columns to purchase_orders
            conn.execute(text("ALTER TABLE purchase_orders ADD COLUMN IF NOT EXISTS payment_method VARCHAR(50) DEFAULT 'contado'"))
            conn.execute(text("ALTER TABLE purchase_orders ADD COLUMN IF NOT EXISTS due_date TIMESTAMP WITH TIME ZONE"))
            conn.execute(text("ALTER TABLE purchase_orders ADD COLUMN IF NOT EXISTS is_paid BOOLEAN DEFAULT FALSE"))
            conn.commit()
            print("Successfully added payment fields to purchase_orders.")
        except Exception as e:
            print(f"Error applying patch: {e}")

if __name__ == "__main__":
    patch_database()
