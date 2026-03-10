import os

# Define the root path of the project
project_root = r"c:\Users\yhorm\OneDrive\Desktop\Proyecto67"
output_file = os.path.join(project_root, "compendio_tecnico_completo.txt")

# List of files to include in order (relative to project_root)
files_to_include = [
    # Backend Core & Configs
    r"backend\.env",
    r"backend\requirements.txt",
    r"backend\database_init.sql",
    r"backend\app\main.py",
    r"backend\app\database.py",
    r"backend\app\config.py",
    r"backend\app\api\deps.py",
    
    # Backend API Endpoints
    r"backend\app\api\auth.py",
    r"backend\app\api\users.py",
    r"backend\app\api\products.py",
    r"backend\app\api\sales.py",
    r"backend\app\api\suppliers.py",
    r"backend\app\api\purchase_orders.py",
    r"backend\app\api\reports.py",
    r"backend\app\api\stock_movements.py",
    
    # Backend Models
    r"backend\app\models\user.py",
    r"backend\app\models\product.py",
    r"backend\app\models\supplier.py",
    r"backend\app\models\sale.py",
    r"backend\app\models\purchase_order.py",
    r"backend\app\models\stock_movement.py",
    r"backend\app\models\audit_log.py",
    
    # Backend Schemas
    r"backend\app\schemas\user.py",
    r"backend\app\schemas\product.py",
    r"backend\app\schemas\supplier.py",
    r"backend\app\schemas\sale.py",
    r"backend\app\schemas\purchase_order.py",
    r"backend\app\schemas\stock_movement.py",
    r"backend\app\schemas\token.py",
    
    # Backend Services
    r"backend\app\services\alert_service.py",
    r"backend\app\services\email_service.py",
    r"backend\app\services\profit_service.py",
    r"backend\app\services\stock_service.py",
    
    # Frontend Contexts
    r"product-tracker\src\context\AuthContext.jsx",
    r"product-tracker\src\context\InventoryContext.jsx",
    r"product-tracker\src\context\NotificationContext.jsx",
    r"product-tracker\src\context\SearchContext.jsx",
    r"product-tracker\src\context\ThemeContext.jsx",
    
    # Frontend Pages & Services
    r"product-tracker\src\services\api.js",
    r"product-tracker\src\pages\Dashboard.jsx",
    r"product-tracker\src\pages\Login.jsx",
    r"product-tracker\src\pages\Signup.jsx",
    r"product-tracker\src\pages\ForgotPassword.jsx",
    r"product-tracker\src\pages\ResetPassword.jsx",
    r"product-tracker\src\pages\POS.jsx",
    r"product-tracker\src\pages\Inventory.jsx",
    r"product-tracker\src\pages\Suppliers.jsx",
    r"product-tracker\src\pages\PurchaseOrders.jsx",
    r"product-tracker\src\pages\Reports.jsx",
    
    # Configuration
    r"product-tracker\package.json"
]

def build_compendium():
    print(f"Generating {output_file}...")
    with open(output_file, "w", encoding="utf-8") as outfile:
        for rel_path in files_to_include:
            abs_path = os.path.join(project_root, rel_path)
            if not os.path.exists(abs_path):
                print(f"Warning: File not found: {abs_path}")
                continue
            
            # Use forward slashes for the label as requested (similar to user example)
            label_path = rel_path.replace("\\", "/")
            outfile.write(f"========== ARCHIVO: {label_path} ==========\n")
            
            try:
                with open(abs_path, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
            except Exception as e:
                outfile.write(f"Error reading file: {e}")
            
            outfile.write("\n\n")
    print("Done!")

if __name__ == "__main__":
    build_compendium()
