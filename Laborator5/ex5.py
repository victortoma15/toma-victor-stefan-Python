class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def feed_young(self):
        print(f"{self.name} isi hraneste puii cu lapte.")


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} zboara.")


class Fish(Animal):
    def __init__(self, name, habitat, water_type):
        super().__init__(name, habitat)
        self.water_type = water_type

    def swim(self):
        print(f"{self.name} inoata.")


def main():
    lion = Mammal("Leul", "Savanna", "Golden")
    lion.feed_young()

    eagle = Bird("Vulturul carpatin", "Munti", 2.5)
    eagle.fly()

    shark = Fish("Rechinul sabie", "Ocean", "Apa sarata")
    shark.swim()


main()
