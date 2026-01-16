#!/usr/bin/python3

def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("=== Garden Watering System ===")
    good_list = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(good_list)

    print("Testing with error...")

    print("Cleanup always happens, even with errors!")

if __name__ == "__main__":
    test_watering_system()
