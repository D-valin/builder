import sys
import os

def replace_in_file(filepath, search_text, replacement_text):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_text not in content:
        print(f"Error: Search text not found in {filepath}")
        return False
    
    new_content = content.replace(search_text, replacement_text)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Success: Updated {filepath}")
    return True

# Inventory.jsx Add Modal
inv_path = r'c:\Users\yhorm\OneDrive\Desktop\Proyecto67\product-tracker\src\pages\Inventory.jsx'
search1 = """                                    <div>
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Ubicación</label>
                                        <input name="location" className={inputClass} placeholder="Pasillo 1, Estante A" required />
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Vencimiento (Opcional)</label>"""

repl1 = """                                    <div>
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Ubicación</label>
                                        <input name="location" className={inputClass} placeholder="Pasillo 1, Estante A" required />
                                    </div>
                                    <div className="md:col-span-2">
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Proveedor</label>
                                        <select name="supplier_id" className={inputClass}>
                                            <option value="">Seleccionar Proveedor</option>
                                            {suppliers.map(s => (
                                                <option key={s.id} value={s.id}>{s.name}</option>
                                            ))}
                                        </select>
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Vencimiento (Opcional)</label>"""

# Inventory.jsx Edit Modal
search2 = """                                    <div>
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Ubicación</label>
                                        <input
                                            name="location"
                                            defaultValue={editingProduct.location}
                                            className={inputClass}
                                            required
                                        />
                                    </div>
                                    <div className="md:col-span-2">
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Fecha de Vencimiento (Opcional)</label>"""

repl2 = """                                    <div>
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Ubicación</label>
                                        <input
                                            name="location"
                                            defaultValue={editingProduct.location}
                                            className={inputClass}
                                            required
                                        />
                                    </div>
                                    <div className="md:col-span-2">
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Proveedor</label>
                                        <select
                                            name="supplier_id"
                                            defaultValue={editingProduct.supplier_id || ''}
                                            className={inputClass}
                                        >
                                            <option value="">Seleccionar Proveedor</option>
                                            {suppliers.map(s => (
                                                <option key={s.id} value={s.id}>{s.name}</option>
                                            ))}
                                        </select>
                                    </div>
                                    <div className="md:col-span-2">
                                        <label className="block text-sm font-medium text-slate-700 dark:text-slate-300 mb-1">Fecha de Vencimiento (Opcional)</label>"""

po_path = r'c:\Users\yhorm\OneDrive\Desktop\Proyecto67\product-tracker\src\pages\PurchaseOrders.jsx'
# Supplier select
search3 = """                                    <select
                                        name="supplier_id"
                                        className="w-full px-3 py-2 border border-slate-300 dark:border-slate-700 dark:bg-slate-800 dark:text-white rounded-lg focus:ring-2 focus:ring-primary/50 outline-none"
                                        required
                                    >"""

repl3 = """                                    <select
                                        name="supplier_id"
                                        value={selectedSupplierId}
                                        onChange={(e) => {
                                            setSelectedSupplierId(e.target.value);
                                            setOrderItems([]); 
                                        }}
                                        className="w-full px-3 py-2 border border-slate-300 dark:border-slate-700 dark:bg-slate-800 dark:text-white rounded-lg focus:ring-2 focus:ring-primary/50 outline-none"
                                        required
                                    >"""

# Product select in PO
search4 = """                                                        <option value="">Seleccionar</option>
                                                        {products.filter(p => !p.archived).map(p => (
                                                            <option key={p.id} value={p.id}>{p.name}</option>
                                                        ))}"""

repl4 = """                                                        <option value="">Seleccionar</option>
                                                        {products
                                                            .filter(p => !p.archived && (!selectedSupplierId || p.supplier_id === parseInt(selectedSupplierId)))
                                                            .map(p => (
                                                                <option key={p.id} value={p.id}>{p.name}</option>
                                                            ))}"""

replace_in_file(inv_path, search1, repl1)
replace_in_file(inv_path, search2, repl2)
replace_in_file(po_path, search3, repl3)
replace_in_file(po_path, search4, repl4)
