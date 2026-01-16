#!/usr/bin/python3

class GardenError(Exception):
    def __init__(self, message="A general garden error occurred"):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)

def check_plant_health(is_wilting: bool):
    if is_wilting:
        raise PlantError()

def check_water_level(tank_empty: bool):
    if tank_empty:
        raise WaterError()

def main():
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant_health(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water_level(True)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant_health(True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water_level(True)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    
    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    main()
