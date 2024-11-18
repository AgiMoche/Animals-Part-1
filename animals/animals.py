class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} eats"

    def sound(self):
        return "sound..."


class Dog(Animal):
    def __init__(self, name="Rax"):
        super().__init__(name)

    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name="Stormy"):
        super().__init__(name)

    def sound(self):
        return "Meow"


class Home:
    def __init__(self):
        self.adopted_pets = []

    def adopt_pet(self, pet):
        if pet in self.adopted_pets:
            raise ValueError(
                "You have already adopted this animal. You cannot adopt the same animal twice. Please choose another animal to adopt."
            )

        if not isinstance(pet, Animal):
            raise TypeError(
                "You cannot adopt this animal - Please only adopt a pet that is an instance of Cat, Dog or Animal"
            )

        self.adopted_pets.append(pet)
        return len(self.adopted_pets)

    def make_all_sounds(self):
        return [animal.sound() for animal in self.adopted_pets]
