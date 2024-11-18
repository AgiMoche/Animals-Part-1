import pytest
from animals.animals import Animal, Cat, Dog, Home


@pytest.fixture
def animal():
    animal = Animal("Shrek")
    return animal


@pytest.fixture
def dog():
    dog = Dog()
    return dog


@pytest.fixture
def cat():
    cat = Cat()
    return cat


@pytest.fixture
def home():
    home = Home()
    return home


class Butterfly:
    def __init__(self, name="Tyla"):
        self.name = name


def test_animal_eats(animal, dog, cat):
    assert animal.eat() == "Shrek eats"
    assert dog.eat() == "Rax eats"
    assert cat.eat() == "Stormy eats"


def test_animal_sounds(animal, dog, cat):
    assert animal.sound() == "sound..."
    assert dog.sound() == "Bark"
    assert cat.sound() == "Meow"


def test_make_all_sounds_when_home_has_no_pets(home):
    assert home.make_all_sounds() == []


def test_home_instance_initially_has_no_pets(home):
    assert len(home.adopted_pets) == 0


def test_adopt_pet(home, dog, cat):
    assert home.adopt_pet(dog) == 1
    assert home.adopt_pet(cat) == 2


def test_make_all_sounds(home, animal, dog, cat):
    home.adopt_pet(animal)
    home.adopt_pet(dog)
    home.adopt_pet(cat)
    assert home.make_all_sounds() == ["sound...", "Bark", "Meow"]


def test_adopt_pet_twice(home, dog):
    home.adopt_pet(dog)

    with pytest.raises(
        ValueError,
        match="You have already adopted this animal. You cannot adopt the same animal twice. Please choose another animal to adopt.",
    ):
        home.adopt_pet(dog)


def test_adopt_pet_accepts_animal_instances_only(home):
    with pytest.raises(
        TypeError,
        match="You cannot adopt this animal - Please only adopt a pet that is an instance of Cat, Dog or Animal",
    ):
        butterfly = Butterfly()
        home.adopt_pet(butterfly)
