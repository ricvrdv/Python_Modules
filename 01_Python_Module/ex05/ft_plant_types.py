#!/usr/bin/python3

"""
Specialized Plant types module.

Demonstrates inheritance and batch creation.
"""

class Plant:
    """
    Base class for common plant attributes.

    Attributes:
        _name (str): The common name of the plant species.
        _height (int): The height in centimeters.
        _age (int): The age in days.
    """
    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

class Flower(Plant):
    """
    Subclass of Plant representing a flower.

    Attributes:
        _color (str): The color of the flower.
    """
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color

    def bloom(self):
        print(f"{self._name} (Flower): {self._height}cm, {self._age} days, {self._color} color")
        print(self._name + " is blooming beautifully!")

class Tree(Plant):
    """
    Subclass of Plant representing a tree.

    Attributes:
        _trunk_diameter (int): The diameter of the tree's trunk in centimeters.
    """
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self._name} (Tree): {self._height}cm, {self._age} days, {self._trunk_diameter}cm diameter")
        shade_area = int(3.14 * (self._trunk_diameter / 10) ** 2)
        print(self._name + f" provides {shade_area} square meters of shade")

class Vegetable(Plant):
    """
    Subclass of Plant representing a vegetable.

    Attributes:
        _harvest_season (str): The season for ideal harvesting.
        _nutritional_value str): The nutrient the vegetable is rich in.
    """
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value
        print(f"{self._name} (Vegetable): {self._height}cm, {self._age} days, {self._harvest_season} harvest")
        print(f"{self._name} is rich in {self._nutritional_value}")

def main():
    """Create and display 2 instances of each plant type."""
    print("=== Garden Plant Types ===\n")

    flowers = [("Rose", 25, 30, "red"), ("Lily", 40, 15, "white")]
    trees = [("Oak", 500, 1825, 50), ("Pine", 300, 730, 25)]
    vegetables = [("Tomato", 80, 90, "summer", "vitamin C"), ("Carrot", 20, 60, "autumn", "vitamin A")]

    for i in range(2):
        f = Flower(*flowers[i])
        f.bloom()
        print()

        t = Tree(*trees[i])
        t.produce_shade()
        print()

        v = Vegetable(*vegetables[i])
        print("==========================")

if __name__ == "__main__":
    main()

