#!/usr/bin/python3

"""
This module provides a Plant class to simulate garden growth tracking.
"""

class Plant:
    """
    Represent a plant and track its growth through the days.

    Attributes:
        _name (str): The common name of the plant species.
        _height (int): The current height of the plant in centimeters
        _age (int): THe current age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int):
        """Initialize a new Plant instance with name, heigh, and age."""
        self._name = name
        self._height = height
        self._age = age

    def grow(self, inc: int):
        """
        Increase the plant height by the passed argument.

        Args:
            inc (int): The increment in centimeters.
        """
        if inc > 0:
            self._height += inc

    def age(self, inc: int):
        """
        Increase the plant age by the passed argument.

        Args:
            inc (int): The increment in days.
        """
        if inc > 0:
            self._age += inc

    def get_info(self):
        """Display current plant status."""
        print(self._name + f": {self._height}cm, {self._age} days old")

def main():
    """Execute a 7-day growth simulator for a Rose plant."""
    plant = Plant("Rose", 25, 30)
    height_start = plant._height
    age_start = plant._age
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.get_info()
        plant.grow(1)
        plant.age(1)

    if (plant._height > height_start):
        print(f"Growth this week: +{plant._height - height_start}cm")
    elif (plant._height < height_start):
        print(f"Growth this week: -{plant._height - height_start}cm")
    else:
        print("No growth this week")

if __name__ == "__main__":
    main()
