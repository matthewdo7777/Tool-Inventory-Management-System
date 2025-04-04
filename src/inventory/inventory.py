from src.inventory.query import InventoryQuery
from src.file_handler import TextFileHandler

class InventoryManager:
    def __init__(self):
        self.file_handler = TextFileHandler()
        self.query = InventoryQuery()
    
    def add_item(self, file_path, id, name, quantity, price, supplier_id, items):
        items.append({
                        'id': id,
                        'name': name,
                        'quantity': int(quantity),
                        'price': float(price),
                        'supplier_id':supplier_id
                    })
        self.file_handler.update(file_path, items)
        print()
        print("===============")
        print("Adding item...")
        print("Item has been added successfully!")
        print("===============")

    def delete_tool(self, search_value, items, file_path): 
        items_to_delete = self.query.search_item(search_value, items)
        if(items_to_delete):
            if isinstance(items_to_delete, dict):
                items_to_delete = [items_to_delete]
            for item in items_to_delete:
                if item in items:
                    items.remove(item)
            
            self.file_handler.update(file_path, items)
            print()
            print("===============")
            print("deleting item(s)...")
            print("Item(s) has been deleted successfully!")
            print("===============")
        else:
            print(f"No item with the ID or name '{search_value}' was found.")
