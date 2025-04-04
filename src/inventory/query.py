from src.inventory.order import OrderManager
from src.file_handler import TextFileHandler
from collections import defaultdict


class InventoryQuery:
    def __init__(self):
        self.file_handler = TextFileHandler()
        self.order = OrderManager()

    def search_item(self, search_value, items):
        items_list = []
        for item in items:
            if item["id"] == str(search_value) or item["name"] == str(search_value):
                items_list.append(item)

        if len(items_list) == 1:
            return items_list[0]
        elif items_list:
            return items_list
        else:
            return None

    def search_by_name(self, search_value, items):
        items_list = []
        for item in items:
            if item["name"].lower() == str(search_value).lower():
                items_list.append(item)

        if len(items_list) == 1:
            return items_list[0]
        elif items_list:
            return items_list
        else:
            return None

    def search_by_id(self, search_value, items):
        for item in items:
            if item["id"] == str(search_value):
                return item

    def filter_duplicate(self, items_list):
        duplicate_items_list = defaultdict(list)
        duplicate = []

        for item in items_list:
            item_name = item["name"]
            duplicate_items_list[item_name].append(item)

        for obj_group in duplicate_items_list.values():
            if len(obj_group) > 1:
                duplicate.extend(obj_group)
        return duplicate

    def convert_duplicate_to_keys(self, duplicate_list):
        dict1 = {}
        for item in duplicate_list:
            name = item["name"]

            if name not in dict1:
                dict1[name] = []

            new_dict = {}
            for key, value in item.items():
                if key != "name":
                    new_dict[key] = value

            dict1[name].append(new_dict)

        return dict1

    def check_quantity(self, name, converted_to_key_list):
        total_quantity = 0
        for key, items in converted_to_key_list.items():
            if key == name:
                for item in items:
                    quantity_value = item["quantity"]
                    total_quantity += quantity_value
        return total_quantity

    def remove_item_in_list(self, name, item_list):
        new_item_list = []
        for items in item_list:
            if items["name"] != name:
                new_item_list.append(items)
        return new_item_list

    def display_order_allocation_list(self, item_list, current_quantity, name):
        needed_quantity = 30 - current_quantity
        remaining_quantity = needed_quantity
        for i, item_object in enumerate(item_list):
            max_order_quantity = remaining_quantity
            supplier_name = self.get_supplier_name(item_object["supplier_id"])
            if item_object["name"] == name:
                if i + 1 >= len(item_list) or item_list[i + 1]["name"] != name:
                    print(
                        f"The remaning quantity of {remaining_quantity} went to {supplier_name}"
                    )
                    item_object["user_quantity"] = remaining_quantity
                    remaining_quantity = 0
                    break
                else:
                    next_item = item_list[i + 1]
                    if next_item["name"] == name:
                        while True:
                            try:
                                order_quantity = int(
                                    input(
                                        f"How much do you want to order from {supplier_name}? ({max_order_quantity} quantity is left) "
                                    )
                                )
                                if order_quantity > max_order_quantity:
                                    print(
                                        f"You cannot order more than {max_order_quantity}. Try again."
                                    )
                                elif order_quantity < 0:
                                    print(f"you cannot enter negatives inputs")
                                else:
                                    break
                            except ValueError:
                                print("Please enter a valid number.")
                        item_object["user_quantity"] = order_quantity
                        remaining_quantity -= order_quantity
        return item_list


    def create_order_allocation_list(self, item_list):
        
        filited_item_list = self.filter_duplicate(item_list)
        final_filtered_item_list = filited_item_list
        broken_down_duplicate_list_by_name = self.convert_duplicate_to_keys(
            filited_item_list
        )
        for item_name in broken_down_duplicate_list_by_name:
            print("===============")
            print(f"Ordering for: {item_name}")
            print("===============")
            total_quanity = self.check_quantity(
                item_name, broken_down_duplicate_list_by_name
            )
            if total_quanity >= 10:

                final_filtered_item_list = self.remove_item_in_list(
                    item_name, filited_item_list
                )
            else:
                allocated_list = self.display_order_allocation_list(
                    final_filtered_item_list, total_quanity, item_name
                )
        return allocated_list

    def check_item_quantity_allocation(self, item_list):
        allocated_list = self.create_order_allocation_list(item_list)
        list_of_names = self.convert_duplicate_to_keys(allocated_list)
        names_of_dups = []
        
        less_ten_items = []

        for item in item_list:
            if item["quantity"] < 10:
                less_ten_items.append(item)
        for key, items in list_of_names.items():
             names_of_dups.append(key)

        for names in names_of_dups:
            for lesser_item in less_ten_items[:]:
                if names.lower() == lesser_item["name"].lower():
                    print(f"{names}, {lesser_item['name']}")
                    print(names.lower() == lesser_item["name"].lower())
                    less_ten_items.remove(lesser_item)
                
        if less_ten_items:
            self.order.create_order_list(less_ten_items)
       
        if allocated_list:
            self.order.create_order_list_duplicate(allocated_list)
        
        if less_ten_items:
            self.display_create_orderlist(less_ten_items)
        else:
            self.display_create_orderlist(allocated_list)

    def display_create_orderlist(self, item_list):
        if item_list:
            print()
            print("===============")
            print("Creating orderlist...")
            print("Order list has been created!")
            print("===============")
        else:
            print("===============")
            print("There are no items below 10 quantity")
            print("===============")

    def get_supplier_name(self, supplier_id):
        suppliers = self.file_handler.read_suppliers("data/suppliers.txt")
        for supplier in suppliers:
            if supplier["id"] == supplier_id:
                return supplier["company name"]
