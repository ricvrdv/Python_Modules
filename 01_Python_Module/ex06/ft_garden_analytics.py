#!/usr/bin/python3

class Plant:
    def __init__(self, name: str, height: int):
        self._name = name
        self._height = height
        self._initial_height = height

    def grow(self, inc: int):
        self._height += inc
        print(f"{self._name} grew {inc}cm")

    def growth_achieved(self) -> int:
        return self._height - self._initial_height

    def get_report_details(self):
        return f"{self._name}: {self._height}cm"

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self._color = color

    def get_report_details(self):
        return f"{super().get_report_details()}, {self._color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self._points = points

    def get_report_details(self):
        return f"{super().get_report_details()}, Prize points: {self._points}"

class GardenManager:
    total_gardens = 0

    def __init__(self, owner: str):
        self._owner = owner
        self._plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant):
        self._plants += [plant]
        print(f"Added {plant._name} to {self._owner}'s garden")

    def grow_all(self, inc: int):
        print(f"\n{self._owner} is helping all plants to grow...")
        for plant in self._plants:
            plant.grow(inc)

    def get_summary(self):
        print(f"\n=== {self._owner}'s Garden Report ===")
        print("Plants in garden:")

        total_growth = 0
        for p in self._plants:
            print(f"- {p.get_report_details()}")
            total_growth += p.growth_achieved()

        print(f"\nPlants added: {len(self._plants)}, Total growth: {total_growth}cm")
        stats = self.GardenStats(self._plants)
        print(stats.get_type_breakdown())

    class GardenStats:
        def __init__(self, plants):
            self._plants = plants

        def calculate_score(self):
            score = 0

        def get_type_breakdown(self):
            reg = 0
            flow = 0
            prize = 0

            for p in self._plants:
                class_name = type(p).__name__
                if class_name == "PrizeFlower":
                    prize += 1
                elif class_name == "FloweringPlant":
                    flow += 1
                elif class_name == "Plant":
                    reg += 1

            return f"Plant types: {reg} regular, {flow} flowering, {prize} prize flowers"

    @classmethod
    def create_garden_network(cls, *managers):
        scores_str = ""

        for i in range(len(managers)):
            m = managers[i]
            stats = cls.GardenStats(m._plants)
            score = stats.calculate_score()

            scores_str += f"{m._owner}: {score}"

            if i < len(managers) - 1:
                scores_str += ", "
        print(f"Garden scores - {scores_str}")
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_heights(plants):
        all_valid = True
        for p in plants:
            if p._height <= 10:
                all_valid = False

        print(f"Height validation test: {all_valid}")
        return all_valid


def main():
    print("=== Garden Management System Demo ===\n")

    alice = GardenManager("Alice")
    alice.add_plant(Plant("Oak Tree", 100))
    alice.add_plant(FloweringPlant("Rose", 25, "red"))
    alice.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))

    alice.grow_all(1)
    alice.get_summary()

    bob = GardenManager("Bob")
    bob.add_plant(Plant("Bush", 92))

    bob.grow_all(1)
    bob.get_summary()

    GardenManager.validate_heights(alice._plants)
    GardenManager.create_garden_network(alice, bob)

if __name__ == "__main__":
    main()
