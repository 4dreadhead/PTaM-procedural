import unittest
from lib.classes import *


class TestBird(unittest.TestCase):
    """Tests for Bird class"""
    def setUp(self):
        self.bird_migratory = Bird(migratory=True)
        self.bird_not_migratory = Bird(migratory=False)

    def test_initialized(self):
        self.assertEqual(
            self.bird_migratory.migratory,
            True,
            msg="Bird.migratory must be initialized and must be True when given True."
        )
        self.assertEqual(
            self.bird_not_migratory.migratory,
            False,
            msg="Bird.migratory must be initialized and must be False when given False."
        )
        self.assertRaises(
            TypeError,
            Bird,
            msg="Bird must raise TypeError when required arguments are missing."
        )


class TestFish(unittest.TestCase):
    """Tests for Fish class"""
    def setUp(self):
        self.fish = Fish(area=["area_1", "area_2"])

    def test_initialized(self):
        self.assertEqual(
            self.fish.area,
            ["area_1", "area_2"],
            msg="Fish.area must be initialized correctly."
        )
        self.assertRaises(
            TypeError,
            Fish,
            msg="Fish() must raise TypeError when required arguments are missing."
        )


class TestBeast(unittest.TestCase):
    """Tests for Beast class"""
    def setUp(self):
        self.beast = Beast(beast_type=["type_1", "type_2"])

    def test_initialized(self):
        self.assertEqual(
            self.beast.beast_type,
            ["type_1", "type_2"],
            msg="Beast.beast_type must be initialized correctly."
        )
        self.assertRaises(
            TypeError,
            Beast,
            msg="Beast() must raise TypeError when required arguments are missing."
        )


class TestAnimal(unittest.TestCase):
    """Tests for Animal class"""
    def setUp(self):
        self.beast = Animal(name="my_beast", age=10, animal_class=Beast(beast_type=["test_beast_type"]))
        self.fish = Animal(name="my_fish", age=5, animal_class=Fish(area=["test_fish_aria"]))
        self.bird = Animal(name="my_bird", age=3, animal_class=Bird(migratory=True))

    def test_initialized(self):
        for animal, animal_class in zip([self.beast, self.fish, self.bird], [Beast, Fish, Bird]):
            self.assertIsInstance(
                animal.name,
                str,
                msg="Animal.name must be initialized and must be str type."
            )
            self.assertIsInstance(
                animal.age,
                int,
                msg="Animal.age must be initialized and must be int type."
            )
            self.assertIsInstance(
                animal.animal_class,
                animal_class,
                msg=f"Animal.animal_class must be initialized and must be {animal_class.__name__} type."
            )


class TestContainer(unittest.TestCase):
    """Tests for Container class"""
    def setUp(self):
        self.container = Container()

    def test_initialized(self):
        self.assertIsInstance(
            self.container.data,
            deque,
            msg="Container.data must be initialized and must be deque type"
        )
        self.assertEqual(
            self.container.max_size,
            MAX_CONTAINER_SIZE,
            msg="Container.max_size must be initialized and must be the same as MAX_CONTAINER_SIZE constant."
        )
        self.assertEqual(
            self.container.size,
            len(self.container.data),
            msg="Container.size must be initialized and must be same as 'len(container.data)'."
        )
