import random
from datetime import datetime
from src.file_handler import TextFileHandler

class OrderManager:
    def __init__(self):
        self.file_handler = TextFileHandler()
    
    def get_supplier_name(self, supplier_id):
        suppliers = self.file_handler.read_suppliers("data/suppliers.txt")
        for supplier in suppliers:
            if supplier["id"] == supplier_id:
                return supplier["company name"]

    
    def create_order_list(self, low_stock_items):
        date_ordered = datetime.now().strftime("%B %d, %Y") 
        with open('data/orders.txt', 'a') as file:
            file.write("=" * 60 + "\n")
            for index, item in enumerate(low_stock_items):
                order_id = str(random.randint(0, 99999)).zfill(5)
                amount_ordered = 30 - item['quantity']
                total_cost =  item['price'] * amount_ordered
                file.write(f"ORDER ID.: {order_id}\n")
                file.write(f"Date Ordered: {date_ordered}\n")
                file.write("\n")
                file.write(f"Item Description: {item['name']}\n")
                file.write(f"Amount ordered: {amount_ordered}\n")
                file.write(f"Supplier: {self.get_supplier_name(item['supplier_id'])}\n")
                file.write("\n")
                file.write(f"Total cost: ${total_cost}\n")
                
                if index < len(low_stock_items) - 1:
                    file.write("-" * 60 + "\n")
            file.write("\n")
   
    
    def create_order_list_duplicate(self, duplicate_stock_items):
        date_ordered = datetime.now().strftime("%B %d, %Y") 
        with open('data/orders.txt', 'a') as file:
            file.write("=" * 60 + "\n")
            for index, item in enumerate(duplicate_stock_items):
                order_id = str(random.randint(0, 99999)).zfill(5)
                total_cost =  item['price'] * item['user_quantity']
                file.write(f"ORDER ID.: {order_id}\n")
                file.write(f"Date Ordered: {date_ordered}\n")
                file.write("\n")
                file.write(f"Item Description: {item['name']}\n")
                file.write(f"Amount ordered: {item['user_quantity']}\n")
                file.write(f"Supplier: {self.get_supplier_name(item['supplier_id'])}\n")
                file.write("\n")
                file.write(f"Total cost: ${total_cost}\n")
                
                if index < len(duplicate_stock_items) - 1:
                    file.write("-" * 60 + "\n")
            file.write("\n")
   