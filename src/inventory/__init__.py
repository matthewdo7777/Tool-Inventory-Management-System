from collections import defaultdict

def find_items_with_same_name(items):
    # Group items by name
    name_groups = defaultdict(list)
    for item in items:
        name = item['name']  # Assuming 'name' is the key for the name field
        name_groups[name].append(item)
