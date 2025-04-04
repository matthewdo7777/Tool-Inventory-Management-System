from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read_items(self, file_path):
        pass

    @abstractmethod
    def read_suppliers(self, file_path):
        pass

    @abstractmethod
    def remove_content(self, file_path):
        pass

    @abstractmethod
    def update(self, file_path, items):
        pass


class TextFileHandler(FileHandler):
    def read_items(self, file_path):
        items = []
        try:
            with open(file_path, "r") as f:
                for line in f:
                    part = line.strip().split(";")
                    items.append(
                        {
                            "id": (part[0]),
                            "name": part[1],
                            "quantity": int(part[2]),
                            "price": float(part[3]),
                            "supplier_id": (part[4]),
                        }
                    )
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        return items

    def read_suppliers(self, file_path):
        suppliers = []
        try:
            with open(file_path, "r") as f:
                for line in f:
                    part = line.strip().split(";")
                    suppliers.append(
                        {
                            "id": (part[0]),
                            "company name": part[1],
                            "address": part[2],
                            "sales person contact": part[3],
                        }
                    )
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        return suppliers

    def remove_content(self, file_path):
        try:
            with open(file_path, "r+") as f:
                f.seek(0)
                f.truncate()

        except FileNotFoundError:
            print(f"File not found: {file_path}")

    def update(self, file_path, items):
        self.remove_content(file_path)
        try:
            with open(file_path, "w") as f:
                for item in items:
                    new_item = f"{item['id']};{item['name']};{item['quantity']};{item['price']};{item['supplier_id']}\n"
                    f.write(new_item)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
