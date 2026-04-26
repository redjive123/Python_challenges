import copy
def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"rating": 4.2}
            }
        }
    ]
def apply_discount(data, roll_number):
    length = len(data)
    index_to_modify = roll_number % length
    for i in range(len(data)):
        data[i]["details"]["price"] *= 0.9
        if i == index_to_modify:
            data[i]["details"]["stock"] -= 5
    return data
def compare_data(original, modified):
    changed = 0
    unchanged = 0
    for i in range(len(original)):
        if original[i] != modified[i]:
            changed += 1
        else:
            unchanged += 1
    return (changed, unchanged)
roll_number = 23
original_inventory = create_inventory()
shallow_copy = original_inventory.copy()
deep_copy = copy.deepcopy(original_inventory)
apply_discount(shallow_copy, roll_number)
apply_discount(deep_copy, roll_number)
print("\nOriginal Inventory:")
print(original_inventory)
print("\nShallow Copy:")
print(shallow_copy)
print("\nDeep Copy:")
print(deep_copy)
shallow_result = compare_data(original_inventory, shallow_copy)
deep_result = compare_data(original_inventory, deep_copy)
print("\nComparison Results:")
print("Shallow Copy ->", shallow_result)
print("Deep Copy ->", deep_result)