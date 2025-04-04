from src.inventory.query import InventoryQuery
from src.file_handler import TextFileHandler

class InputValidator:
    def __init__(self) -> None:
        self.query = InventoryQuery()
        self.file_handler = TextFileHandler()

    def validate_item_id(self, items, message_prompt):
        while True:
            user_input_id = self.validate_numerical_input(message_prompt)
            item_id =  self.query.search_by_id(user_input_id, items)
            if not item_id:
                return user_input_id
            print("Conflicting item ID, Please enter a unique ID.")
                
    def validate_numerical_input(self, message_prompt, allow_float=False):
        while True:
            user_input_numerical = input(message_prompt).strip()
            if not user_input_numerical:
                print("Input cannot be empty, please enter a number.")
                continue

            value = self.check_negative_string(user_input_numerical, allow_float)
            if value is not None:
                return value

    def check_negative_string(self, user_input, allow_float):
        try:
            value = float(user_input) if allow_float else int(user_input)          
            if value < 0:
                print("Input must be a positive number")
                return None
            return value
        except ValueError:
            print("Input must be a valid number.")
            return None

    def validate_quantity(self, message_prompt):
        return self.validate_numerical_input(message_prompt, allow_float=False)
    
    def validate_price(self, message_prompt):
        return self.validate_numerical_input(message_prompt, allow_float=True)

    def validate_supplier_id(self, message_prompt):
            suppliers = self.file_handler.read_suppliers("data/suppliers.txt")
            while True:
                user_input_supplier_id = self.validate_numerical_input(message_prompt)
                for supplier in suppliers:
                    if str(user_input_supplier_id) == supplier['id']:
                        return user_input_supplier_id
                print("Supplier ID not found.")