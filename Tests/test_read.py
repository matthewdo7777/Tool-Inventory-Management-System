import unittest
import sys
import io

sys.path.append(".")

from src.file_handler import TextFileHandler


class TestRead(unittest.TestCase):

    def test_read_items(self):
        filepath = "data/mock_items.txt"
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

        result = TextFileHandler().read_items(filepath)
        self.assertEqual(result, expected_items)



    def test_items_file_notFound(self):

        # send to buffer
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        filepath = "data/non_existing_item_file.txt"
        result = TextFileHandler().read_items(filepath)
        self.assertEqual(result, [])

        # revert to normal
        sys.stdout = sys.__stdout__



    def test_read_supplier(self):
        filepath = "data/mock_suppliers.txt"
        expected_suppliers = [
            {
                "id": "50001",
                "company name": "GeniousBuilders",
                "address": "788 30th St., SE, Calgary",
                "sales person contact": "Fred",
            },
            {
                "id": "50002",
                "company name": "Pong Ping",
                "address": "749 Dufferin Blvd., SE, Calgary",
                "sales person contact": "Jacob",
            },
        ]

        result = TextFileHandler().read_suppliers(filepath)
        self.assertEqual(result, expected_suppliers)



    def test_suppliers_file_notFound(self):

        # send to buffer
        suppress_text = io.StringIO()
        sys.stdout = suppress_text

        filepath = "data/non_existing_supplier_file.txt"
        result = TextFileHandler().read_suppliers(filepath)
        self.assertEqual(result, [])

        # revert to normal
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
