#!/usr/bin/python3

def garden_operations():
    print("\nTesting ValueError...")
    try:
        value = int("forty-two")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("\nTesting ZeroDivisionError...")
    try:
        value = 42/0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("\nTesting FileNotFoundError...")
    try:
        open("file_not_found.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("\nTesting KeyError...")
    try:
        garden = {"rose": "white", "sunflower": "yellow", "poppy": "red"}
        print(garden["tulip"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("\nTesting multiple errors together...")
    try:
        value = 1010/0
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("\nAll errors types tested successfully!")

if __name__ == "__main__":
    test_error_types()
