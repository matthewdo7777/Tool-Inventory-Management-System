import unittest
import sys
sys.path.append('.')
from src.inventory.query import InventoryQuery

class TestInventoryQuery(unittest.TestCase):

    def setUp(self):
        self.query = InventoryQuery()
        self.items = [{'id':'3000', 'name':'Knock Bits', 'quantity':18, 'price':12.67, 'supplier_id': '50015'},
                      {'id':'3001', 'name':'Widgets', 'quantity':10, 'price': 35.50, 'supplier_id': '50004'},
                      {'id':'3002', 'name':'Grommets', 'quantity':20, 'price':23.45, 'supplier_id': '50001'},
                      {'id': '3039', 'name': 'Handy Pandies', 'quantity': 3, 'price': 4.35, 'supplier_id': '50017'},
                      {'id': '3040', 'name': 'Inny Outies', 'quantity': 3, 'price': 3.45, 'supplier_id': '50010'}
        ]
    
    def test_search_by_name_found(self):
        result = self.query.search_by_name('Widgets', self.items)
        self.assertEqual(result, {'id':'3001', 'name':'Widgets', 'quantity':10, 'price': 35.50, 'supplier_id': '50004'})
    
    def test_search_by_name_not_found(self):
        result = self.query.search_by_name('Hammer', self.items)
        self.assertIsNone(result)
    
    def test_search_by_name_case_sensitive(self):
        result = self.query.search_by_name('widgets', self.items)
        self.assertEqual(result, {'id':'3001', 'name':'Widgets', 'quantity':10, 'price': 35.50, 'supplier_id': '50004'})
    
    def test_search_by_name_empty_list(self):
        result = self.query.search_by_name('Widgets', [])
        self.assertIsNone(result)

    def test_search_by_name_non_string(self):
        result = self.query.search_by_name(1234, self.items)
        self.assertIsNone(result)
    
    def test_search_by_name_empty_string(self):
        result = self.query.search_by_name('', self.items)
        self.assertIsNone(result)

    def test_search_by_id_found(self):
        result = self.query.search_by_id('3001', self.items)
        self.assertEqual(result, {'id':'3001', 'name':'Widgets', 'quantity':10, 'price': 35.50, 'supplier_id': '50004'})
    
    def test_search_by_id_not_found(self):
        result = self.query.search_by_id('4000', self.items)
        self.assertIsNone(result)
    
    def test_search_by_id_non_string(self):
        result = self.query.search_by_name(3001, self.items)
        self.assertIsNone(result)
    
    def test_search_by_id_empty_list(self):
        result = self.query.search_by_name('3001', [])
        self.assertIsNone(result)

    def test_search_by_id_empty_string(self):
        result = self.query.search_by_name('', self.items)
        self.assertIsNone(result)
    
    def test_search_item_id_found(self):
        result = self.query.search_item('3001', self.items)
        self.assertEqual(result, {'id':'3001', 'name':'Widgets', 'quantity':10, 'price': 35.50, 'supplier_id': '50004'})
    
    def test_search_item_name_found(self):
        result = self.query.search_item('Widgets', self.items)
        self.assertEqual(result, {'id':'3001', 'name':'Widgets', 'quantity':10, 'price': 35.50, 'supplier_id': '50004'})
    
    def test_search_item_name_not_found(self):
        result = self.query.search_item('Hammer', self.items)
        self.assertIsNone(result)

    def test_search_item_id_not_found(self):
        result = self.query.search_item('4000', self.items)
        self.assertIsNone(result)
     
    def test_search_item_name_case_sensitive(self):
        result = self.query.search_item('widgets', self.items)
        self.assertIsNone(result)
    
    def test_search_by_name_non_string(self):
        result = self.query.search_item(1234, self.items)
        self.assertIsNone(result)        
    
    def test_search_item(self):
        searched_value = 'Knock Bits'
        result = self.query.search_item(searched_value, self.items)
        self.assertEqual(result, {'id':'3000', 'name':'Knock Bits', 'quantity':18, 'price':12.67, 'supplier_id': '50015'})
    
    def test_get_supplier_name(self):
        supplierID = '50004' #{ID from the /data/suppliers.txt
        expected_results = 'WinManufacturing Inc.'
        result = self.query.get_supplier_name(supplierID)
        self.assertEqual(result, expected_results)
      
if __name__ == '__main__':
    unittest.main()