from src.inventory.validation import InputValidator
from src.inventory.query import InventoryQuery
from src.inventory.inventory import InventoryManager

class InventoryMenu:
    def __init__(self):
        self.validator = InputValidator()
        self.query = InventoryQuery()
        self.inventory = InventoryManager()
    
    def display_welcome_menu(self):
        print("===========================")
        print("Welcome to Inventory Menu!")
        print("===========================")

    def display_main_menu(self, items, file_path):
        while True:
            print("")
            print("1. Modify Inventory")
            print("2. Search Inventory")
            print("3. Exit")
            print()
            user_input = input("Please select an option (1-3): ").strip()
            match user_input:
                case "1":
                    self.display_modify_inventory(items, file_path)
                    # Removed break; we want to return to the menu after modifying inventory
                case "2":
                    self.display_search_inventory(items, file_path)
                    # Removed break; we want to return to the menu after modifying inventory
                case "3":
                    print("===============")
                    print("GoodBye!")
                    print("===============")
                    return #exit the function and stop the loop
                case _: 
                    print("Invalid please try again")

    def display_modify_inventory(self, items, file_path):
        while True:
            print("")
            print("1. Add tool")
            print("2. Delete tool")
            print("3. Update inventory")
            print("4. Back")
            user_input = input("Please select an option (1-4): ").strip()
            match user_input:
                case "1":
                    user_input_id = self.validator.validate_item_id(items, "Please input ID of tool: ")
                    user_input_name = input("Please input name of tool: ").strip()
                    user_input_quantity = self.validator.validate_quantity("Please input quantity of tool: ")
                    user_input_price = self.validator.validate_price("Please input price of tool: ")
                    user_input_supplier_id = self.validator.validate_supplier_id("Please input supplier ID: ")
                    self.inventory.add_item(file_path, user_input_id, user_input_name, user_input_quantity, user_input_price, user_input_supplier_id, items)
                case "2":
                    user_input_search_id = input("Please input the ID or name of the tool: ").strip()
                    self.inventory.delete_tool(user_input_search_id, items, file_path)
                case "3":
                    self.query.check_item_quantity_allocation(items)
                case "4":
                    print("")
                    return  # Exit this menu and return control to the main menu
                case _:
                    print("Invalid please try again")

    def display_search_inventory(self, items, file_path): 
        while True:
            print("")
            print("1. Search Name")
            print("2. Search ID")
            print("3. Back")
            user_input = input("Please select an option (1-3): ").strip()
            match user_input:
                case "1":
                    user_search_name = input("Please input name here: ").strip()
                    found = self.query.search_by_name(user_search_name, items)
                    if(found):
                        print(found)
                    else:
                        print(f"No item with the Name '{user_search_name}' was found.")
                    
                case "2":
                    user_search_ID = input("Please input ID here: ").strip()
                    found = self.query.search_by_id(user_search_ID, items)
                    if(found):
                        print(found)
                    else:
                        print(f"No item with the ID '{user_search_ID}' was found.")

                case "3":
                    return  # Exit this menu and return control to the main menu
                case _:
                    print("Invalid please try again")