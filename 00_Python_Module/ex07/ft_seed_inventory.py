'''
Display information about different seed types and quantities.
'''

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit.lower() == "packets":
        print(seed_type.capitalize() + f" seeds: {quantity} {unit.lower()} available")
    elif unit.lower() == "grams":
        print(seed_type.capitalize() + f" seeds: {quantity} {unit.lower()} total")
    elif unit.lower() == "area":
        print(seed_type.capitalize() + f" seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
