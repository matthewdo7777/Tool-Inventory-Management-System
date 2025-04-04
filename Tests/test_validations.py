import unittest
import sys

sys.path.append('.')

from src.inventory.validation import InputValidator
from unittest.mock import patch, MagicMock

class TestInputValidation(unittest.TestCase):

    def setUp(self):
        self.validator = InputValidator()
        self.validator.query = MagicMock()
        self.validator.file_handler = MagicMock()
        self.items = [{'id':'3000', 'name':'Knock Bits', 'quantity':18, 'price':12.67, 'supplier_id': '50015'},
                      {'id':'3001', 'name':'Widgets', 'quantity':10, 'price': 35.50, 'supplier_id': '50004'},
                      {'id':'3002', 'name':'Grommets', 'quantity':20, 'price':23.45, 'supplier_id': '50001'}
        ]
        self.suppliers = [
            {'id': '10001', 'company name': 'Supplier A', 'address': 'Hi town', 'sales person contact': 'bob'},
            {'id': '10002', 'name': 'Supplier B', 'address': 'Bye town', 'sales person contact': 'the'},
            {'id': '10003', 'name': 'Supplier C', 'address': 'Welcome town', 'sales person contact': 'builder'}
        ]


    @patch('builtins.print')
    def test_validate_item_id_match_(self, mocked_print):
        self.validator.validate_numerical_input = MagicMock(side_effect='3000')
        self.validator.query.search_by_id.side_effect = [self.items[0], None]

        result = self.validator.validate_item_id(self.items, "Enter ID: ")
        
        mocked_print.assert_called_with("Conflicting item ID, Please enter a unique ID.")


    @patch('builtins.print')
    def test_validate_item_id_unique(self, mocked_print):
        self.validator.validate_numerical_input = MagicMock(side_effect=['3000', '3003'])
        self.validator.query.search_by_id.side_effect = [self.items, None]

        result = self.validator.validate_item_id(self.items, "Enter ID: ")

        self.assertEqual(result, '3003')
        

    @patch('builtins.print')
    def test_validate_supplier_id_exist(self, mocked_print):
        self.validator.validate_numerical_input = MagicMock(return_value='10002')
        self.validator.file_handler.read_suppliers.return_value = [self.suppliers[1], None]
        
        result = self.validator.validate_supplier_id("Enter ID: ")
        
        self.assertEqual(result, '10002')
        

    @patch('builtins.print')
    def test_validate_supplier_id_not_found(self, mocked_print):
        self.validator.validate_numerical_input = MagicMock(side_effect=['10004', StopIteration])
        self.validator.file_handler.read_suppliers.return_value = self.suppliers

        with patch('builtins.input', side_effect=StopIteration):
            with self.assertRaises(StopIteration):
                result = self.validator.validate_supplier_id("Enter ID: ")

        mocked_print.assert_called_with("Supplier ID not found.")


    @patch('builtins.input', side_effect=['', StopIteration])
    @patch('builtins.print')
    def test_validate_numerical_input_empty(self, mock_print, mock_input):
        with self.assertRaises(StopIteration):
            self.validator.validate_numerical_input("Enter a number: ")
        
        mock_print.assert_called_with("Input cannot be empty, please enter a number.")


    @patch('builtins.input', side_effect=['abc', StopIteration])
    @patch('builtins.print')
    def test_validate_numerical_input_invalid(self, mock_print, mock_input):
        with self.assertRaises(StopIteration):
            self.validator.validate_numerical_input("Enter a number: ")
        
        mock_print.assert_called_with("Input must be a valid number.")


    @patch('builtins.input', side_effect=['-1', StopIteration])
    @patch('builtins.print')
    def test_validate_numerical_input_negative(self, mock_print, mock_input):
        with self.assertRaises(StopIteration):
            self.validator.validate_numerical_input("Enter a number: ")
        
        mock_print.assert_called_with("Input must be a positive number")

    
    #we already checked for empty, negative inputs in the numerical_input test methods
    @patch('builtins.print')
    def test_check_negative_string_integer(self, mock_print):
        result = self.validator.check_negative_string("10", allow_float=False)
        self.assertEqual(result, 10)


    @patch('builtins.print')
    def test_check_negative_string_float(self, mock_print):
        result = self.validator.check_negative_string("10.50", allow_float=True)
        self.assertEqual(result, 10.50)

    #because this is uses method delegation, we will be testing for invalid input since valid has been done
    @patch('builtins.input', side_effect=['10.5', StopIteration])
    @patch('builtins.print')
    def test_validate_quantity_invalid_float(self, mock_print, mock_input):
        with self.assertRaises(StopIteration):
            result = self.validator.validate_quantity("Enter quantity: ")
        
        mock_print.assert_called_with("Input must be a valid number.")

    #price takes in int or floats
    @patch('builtins.input', side_effect=['9.99', '10'])
    def test_validate_price_valid_any_type(self, mock_input):
        result = self.validator.validate_price("Enter price: ")
        self.assertEqual(result, 9.99)

        result_two = self.validator.validate_price("Enter price: ")
        self.assertEqual(result_two, 10)

    
if __name__ == '__main__':
    unittest.main()
    
