#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

def main():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    print(plant1.name + f": {plant1.height}cm, {plant1.age} days old")
    print(plant2.name + f": {plant2.height}cm, {plant2.age} days old")
    print(plant3.name + f": {plant3.height}cm, {plant3.age} days old")

if __name__ == "__main__":
    main()
