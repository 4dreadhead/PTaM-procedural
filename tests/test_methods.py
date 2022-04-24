import unittest
import random
from lib.methods import *
from lib.classes import *


class TestMethods(unittest.TestCase):
    def test_create_container(self):
        """Test method 'create_container'"""
        self.assertEqual(
            create_container(),
            Container(),
            "Method 'create_container' must return initialized Container class."
        )

    def test_allowed_areas(self):
        """Test method 'allowed_areas'"""
        self.assertIsInstance(
            allowed_areas(),
            list,
            msg="Method 'test_allowed_areas' must return list of allowed areas for fish."
        )
        self.assertTrue(
            len(allowed_areas()) > 0,
            msg="Allowed areas must not be empty."
        )

    def test_allowed_beast_types(self):
        """Test method 'allowed_beast_types'"""
        self.assertIsInstance(
            allowed_beast_types(),
            list,
            msg="Method 'test_allowed_areas' must return list of allowed beast types."
        )
        self.assertTrue(
            len(allowed_beast_types()) > 0,
            msg="Beast types must not be empty."
        )

    def test_add(self):
        """Test method 'add'"""
        animal = Animal(name="animal", age=5, animal_class=Beast(beast_type=["beast_type_1, beast_type_2"]))
        container = create_container()
        size = container.size
        full_container = create_container()

        add(container, animal)
        for _ in range(MAX_CONTAINER_SIZE):
            add(full_container, animal)

        self.assertEqual(
            container.data[0],
            animal,
            msg="Method 'add' must add animal to container."
        )
        self.assertEqual(
            container.size,
            size + 1,
            msg="Method 'add' must increase size by 1 for each added animal"
        )
        self.assertRaises(
            BufferError,
            add,
            full_container,
            animal
        )

    def test_create_fish_class(self):
        """Test method 'create_fish_class'"""
        name = "fish_name"
        age = "5"
        area = f"{random.choice(allowed_areas())}+{random.choice(allowed_areas())}"

        wrong_age = "some_wrong_value"
        wrong_area = "some_wrong_value"

        self.assertEqual(
            create_fish_class(name, area, age),
            Animal(name=name, age=5, animal_class=Fish(area=area.split("+"))),
            msg="Method 'create_fish_class' must parse data from given args and create Animal."
        )
        self.assertRaises(
            ValueError,
            create_fish_class,
            name,
            wrong_area,
            age
        )
        self.assertRaises(
            ValueError,
            create_fish_class,
            name,
            area,
            wrong_age
        )

    def test_create_bird_class(self):
        """Test method 'create_bird_class'"""
        name = "bird_name"
        age = "5"
        migratory = "true"

        wrong_age = "some_wrong_value"
        wrong_migratory = "some_wrong_value"

        self.assertEqual(
            create_bird_class(name, migratory, age),
            Animal(name=name, age=5, animal_class=Bird(migratory=True)),
            msg="Method 'create_bird_class' must parse data from given args and create Animal."
        )
        self.assertRaises(
            ValueError,
            create_bird_class,
            name,
            wrong_migratory,
            age
        )
        self.assertRaises(
            ValueError,
            create_bird_class,
            name,
            migratory,
            wrong_age
        )

    def test_create_beast_class(self):
        """Test method 'create_beast_class'"""
        name = "beast_name"
        age = "5"
        beast_type = f"{random.choice(allowed_beast_types())}+{random.choice(allowed_beast_types())}"

        wrong_age = "some_wrong_value"
        wrong_beast_type = "some_wrong_value"

        self.assertEqual(
            create_beast_class(name, beast_type, age),
            Animal(name=name, age=5, animal_class=Beast(beast_type=beast_type.split("+"))),
            msg="Method 'create_beast_class' must parse data from given args and create Animal."
        )
        self.assertRaises(
            ValueError,
            create_beast_class,
            name,
            wrong_beast_type,
            age
        )
        self.assertRaises(
            ValueError,
            create_beast_class,
            name,
            beast_type,
            wrong_age
        )

    def test_clear(self):
        """Test method 'clear'"""
        container = create_container()
        animal = Animal(name="animal", age=5, animal_class=Beast(beast_type=["beast_type_1, beast_type_2"]))

        for _ in range(MAX_CONTAINER_SIZE):
            add(container, animal)

        clear(container)

        self.assertEqual(
            len(container.data),
            0,
            "Method 'clear' must clear all data from container"
        )
        self.assertEqual(
            container.size,
            0,
            "Method 'clear' must set container.size at 0"
        )

    def test_string_conversion(self):
        """Test method 'string_conversion'"""
        beast = Animal(name="my_beast", age=10, animal_class=Beast(beast_type=["test_beast_type"]))
        fish = Animal(name="my_fish", age=5, animal_class=Fish(area=["test_fish_aria"]))
        bird = Animal(name="my_bird", age=3, animal_class=Bird(migratory=True))

        self.assertEqual(
            string_conversion(beast),
            f"Type: beast.\t\tName: {beast.name}.\tAge: {beast.age}. \t"
            f"Type: {', '.join(beast.animal_class.beast_type)}.",
            msg="Method 'string_conversion' must returns right str description of beast."
        )
        self.assertEqual(
            string_conversion(fish),
            f"Type: fish.\t\tName: {fish.name}.\tAge: {fish.age}. \t"
            f"Area: {', '.join(fish.animal_class.area)}.",
            msg="Method 'string_conversion' must returns right str description of fish."
        )
        self.assertEqual(
            string_conversion(bird),
            f"Type: bird.\t\tName: {bird.name}.\tAge: {bird.age}. \t"
            f"Is migratory: {bird.animal_class.migratory}."
        )

    def test_read_file(self):
        """Test method 'read_file'"""
        file_path = "./tmp/test_input.txt"
        container = create_container()

        beast = Animal(name="my_beast", age=10, animal_class=Beast(beast_type=["predator", "herbivores"]))
        fish = Animal(name="my_fish", age=5, animal_class=Fish(area=["river", "sea"]))
        bird = Animal(name="my_bird", age=3, animal_class=Bird(migratory=True))

        read_file(container, file_path)
        self.assertTrue(
            len(container.data) == 3,
            msg="Method 'read_file' must correctly parse data from file and put it in container."
        )
        for parsed_animal, animal in zip(container.data, [beast, fish, bird]):
            self.assertEqual(
                parsed_animal,
                animal,
                msg="Method 'read_file' must correctly parse data from file and put it in container."
            )

    def test_write_file(self):
        """Test method 'write_file'"""
        file_path_in = "./tmp/test_input.txt"
        file_path_out = "./tmp/test_output.txt"
        file_path_out_example = "./tmp/output_example.txt"
        container = create_container()

        read_file(container, file_path_in)
        write_file(container, file_path_out)

        with open(file_path_out, "r+") as file, open(file_path_out_example, "r+") as example:
            self.assertEqual(
                file.read(),
                example.read(),
                msg="Method 'write_file' must write right content."
            )
            file.truncate(0)

    def test_parse_line_and_create_animal_class(self):
        """Test method 'parse_line_and_create_animal_class'"""
        beast_line = "beast my_beast predator+herbivores 10"
        fish_line = "fish my_fish river+sea 5"
        bird_line = "bird my_bird true 3"

        beast = Animal(name="my_beast", age=10, animal_class=Beast(beast_type=["predator", "herbivores"]))
        fish = Animal(name="my_fish", age=5, animal_class=Fish(area=["river", "sea"]))
        bird = Animal(name="my_bird", age=3, animal_class=Bird(migratory=True))

        for animal_line, animal_class in zip([beast_line, fish_line, bird_line], [beast, fish, bird]):
            self.assertEqual(
                parse_line_and_create_animal_class(animal_line),
                animal_class,
                msg="Method 'parse_line_and_create_animal_class' must create right animal class."
            )

    def test_sort_by_name_length(self):
        """Test method 'test_sort_by_name_length'"""
        container = create_container()

        short_name_animal = Animal(name="short", age=3, animal_class=Bird(migratory=True))
        medium_name_animal = Animal(name="medium_length", age=5, animal_class=Fish(area=["sea"]))
        long_name_animal = Animal(name="very_very_very_long_name", age=10, animal_class=Beast(["predator"]))

        for animal in [short_name_animal, medium_name_animal, long_name_animal]:
            add(container, animal)

        sort_by_name_length(container)

        for container_animal, animal in zip(container.data, [long_name_animal, medium_name_animal, short_name_animal]):
            self.assertEqual(
                container_animal,
                animal,
                msg="Method 'sort_by_name_length' must sort data correctly in descending order."
            )
