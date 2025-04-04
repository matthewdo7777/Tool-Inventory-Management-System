import unittest
import sys
sys.path.append('.')

from src.inventory.order import OrderManager
from src.file_handler import TextFileHandler

class TestOrderManager(unittest.TestCase):
        def setUp(self):
            self.query = OrderManager()
            
        def read_items(self, file_path):
            orders = []
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        if "====" in line or line.strip() == "" or line.startswith("ORDER ID:") or line.startswith("Date Ordered:"):
                            continue
                        part = line.strip().split(":")
                        if part[0] == "ORDER ID.":
                            continue
                        if len(part) == 2:
                            orders.append({
                                'key': part[0].strip(),
                                'value': part[1].strip()
                            })
                        else:
                            print(f"Skipping line (no valid key-value pair): {line.strip()}")
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            
            return orders

        
        def test_create_order_list(self):
            low_stock_items = [{'id': '3040', 'name': 'Inny Outies', 'quantity': 3, 'price': 3.45, 'supplier_id': '50010'}]
            
            expected_results_item_desc = "Inny Outies"
            expected_results_amount_ordered = "27"
            expected_results_supplier =  "50010"
            expected_results_total_cost = "$93.15"
            
            filepath = "data/orders.txt"
            self.query.create_order_list(low_stock_items)
            result = self.read_items(filepath)
            self.assertEqual(result[0]["value"], expected_results_item_desc)
            self.assertEqual(result[1]["value"], expected_results_amount_ordered)
            self.assertEqual(result[2]["value"], expected_results_supplier)
            self.assertEqual(result[3]["value"], expected_results_total_cost)
            

if __name__ == '__main__':
    unittest.main()