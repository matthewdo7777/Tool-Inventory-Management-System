import unittest
import sys
sys.path.append('.')

from src.inventory.inventory import InventoryManager
from src.file_handler import TextFileHandler

class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.query = InventoryManager()
        self.items = [
            {
                "id": "0001",
                "name": "item_1",
                "quantity": 98,
                "price": 10.10,
                "supplier_id": "00001",
            },
        ]
        self.filepath = "data/mock_items2.txt"
    
    def test_add_item(self):
        self.query.add_item(self.filepath, '0002', 'item_2', '99', '99.99', '00002', self.items)
        result = TextFileHandler().read_items(self.filepath)
        expected_items = [
            {
                "id": "0001",
                "name": "item_1",
                "quantity": 98,
                "price": 10.10,
                "supplier_id": "00001",
            },
            {
                "id": "0002",
                "name": "item_2",
                "quantity": 99,
                "price": 99.99,
                "supplier_id": "00002",
            },
        ]
        self.assertEqual(result, expected_items)
    
    def test_delete_item(self):
        searched_value = "item_1".strip()
        self.query.delete_tool(searched_value, self.items, self.filepath)
        result = TextFileHandler().read_items(self.filepath)
        expected_items = [{
                "id": "0001",
                "name": "item_1",
                "quantity": 98,
                "price": 10.10,
                "supplier_id": "00001",
        }]
        self.assertNotEqual(result, expected_items)
          
        
if __name__ == '__main__':
    unittest.main()