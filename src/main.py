import sys

sys.path.append(".")

from src.file_handler import TextFileHandler
from src.menu.menu import InventoryMenu


def main():
    file_handler = TextFileHandler()
    items_file = "data/items.txt"
    items = file_handler.read_items(items_file)
    menu = InventoryMenu()
    menu.display_welcome_menu()
    menu.display_main_menu(items, items_file)


if __name__ == "__main__":
    main()
