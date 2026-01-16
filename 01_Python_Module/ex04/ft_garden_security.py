#!/usr/bin/python3

"""
This module provides the SecurePlant class, which uses encapsulation
to prevent data corruption through input validation.
"""

class SecurePlant:
    """
    A plant class that protects its attributes from invalid data.

    Attributes:
        _name (str): The common name of the plant species.
        _height (int): The height in centimeters (must be non-negative).
        _age (int): The age in days (must be non-negative).
    """
    def __init__(self, name: str):
        """Initialize a plant with just a name."""
        self._name = name
        self._height = 0
        self._age = 0
        print("Plant created: " + self._name.capitalize())

    def get_height(self) -> int:
        """Return the current height."""
        return self._height

    def get_age(self) -> int:
        """Return the current age."""
        return self._age

    def set_height(self, value: int):
        """
        Validate and set the plant height.

        Args:
            value (int): The new height in centimeters.
        """
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int):
        """
        Validate and set the plant age.

        Args:
            value (int): The new age in days.
        """
        if value < 0:
            print(f"Invalid operation attempted: age {value}days [REJECTED]")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_info(self):
        """Return a string summary of the plant's current state."""
        print(f"Current plant: {self._name} ({self.get_height()}cm, {self.get_age()} days)")

def main():
    """Demonstrate the security system by attempting valid and invalid updates."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose")
    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.get_info()

if __name__ == "__main__":
    main()
