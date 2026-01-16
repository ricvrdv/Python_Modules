#!/usr/bin/python3

"""
This module provides a Plant class and automates the creation of multiple Plant objects.
"""

class Plant:
    """
    Represent a plant with specific growth metrics.

    Attributes:
        _name (str): Common name of the plant species.
        _height (int): Height in centimeters.
        _age (int): Age in days.
    """
    def __init__(self, name: str, height: int, age: int):
        """Initialize a Plant and immediately report its creation."""
        self._name = name
        self._height = height
        self._age = age
        print(f"Created: {self._name} ({self._height}cm, {self._age} days)")

def main():
    """Execute the factory process to initialize multiple plants."""
    print("=== Plant Factory Output ===")
    plant_data = [
            ("Rose", 25, 30),
            ("Oak", 200, 365),
            ("Cactus", 5, 90),
            ("Sunflower", 80, 45),
            ("Fern", 15, 120)]

    plants = [Plant(*data) for data in plant_data]
    print(f"\nTotal plants created: {len(plants)}")

if __name__ == "__main__":
    main()
