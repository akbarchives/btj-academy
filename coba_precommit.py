class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound!")


def CalculateSum(a, b):
    return a + b


def main():
    dog = Animal("Buddy", "Dog")
    cat = Animal("Whiskers", "Cat")

    dog.make_sound()
    cat.make_sound()

    result = CalculateSum(3, 5)
    print(f"The sum is: {result}")


if __name__ == "__main__":
    main()
