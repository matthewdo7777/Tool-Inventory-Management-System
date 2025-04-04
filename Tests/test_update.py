import unittest
import sys
import os
import tempfile

sys.path.append(".")

from src.file_handler import TextFileHandler


class TestFileHandler(unittest.TestCase):

    def test_remove_content(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(b"Hello World")
            file_path = tmp_file.name

        TextFileHandler().remove_content(file_path)
        with open(file_path, "r") as f:
            content = f.read()
            self.assertEqual(content, "")

        os.remove(file_path)

    # Update method
    def test_update(self):

        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            file_path = tmp_file.name

        items = [
            {
                "id": "3000",
                "name": "Knock Bits",
                "quantity": 18,
                "price": 12.67,
                "supplier_id": "50015",
            },
            {
                "id": "3001",
                "name": "Widgets",
                "quantity": 10,
                "price": 35.50,
                "supplier_id": "50004",
            },
            {
                "id": "3002",
                "name": "Grommets",
                "quantity": 20,
                "price": 23.45,
                "supplier_id": "50001",
            },
        ]

        TextFileHandler().update(file_path, items)

        expected_content = (
            "3000;Knock Bits;18;12.67;50015\n"
            "3001;Widgets;10;35.5;50004\n"
            "3002;Grommets;20;23.45;50001\n"
        )
        with open(file_path, "r") as f:
            content = f.read()
            self.assertEqual(content, expected_content)

        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
