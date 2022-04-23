import sys
from lib.classes import *


def create_container() -> Container:
    """
    This function creates animal container
    :return: animal container
    """
    return Container()


def allowed_areas() -> list:
    """
    This function returns list of the allowed areas for the fish
    :return: list of allowed areas
    """
    return ["canal", "lake", "ocean", "pool", "pond", "river", "sea", "spring"]


def allowed_beast_types() -> list:
    """
    This function returns list of the allowed beast types
    :return: list of allowed beast types
    """
    return ["predator", "herbivores", "omnivores", "insectivores"]


def add(container: Container, animal) -> None:
    """
    This function adds animal to container
    :param container: Container: animal's container;
    :param animal: animal objects
    :return: None
    """
    # Check for container is not full
    if container.size >= container.max_size:
        raise BufferError

    # Add data
    container.data.append(animal)
    container.size += 1


def create_bird_class(name, migratory, age):
    """
    This function parses data and creates Bird class
    :param name: str: bird name
    :param migratory: str: is migratory
    :param age: str: bird age
    :return: Bird class
    """
    if migratory == "true" or migratory == "false":
        migratory = True
    elif migratory == "false":
        migratory = False
    else:
        raise ValueError

    return Animal(name=name, age=age, animal_class=Bird(migratory=migratory))


def create_fish_class(name, areas, age):
    """
    This function parses data and creates Fish class
    :param age: str: fish age
    :param name: str: fish name
    :param areas: str: fish area
    :return: Fish class
    """
    successful_parsed_areas = []
    areas = areas.split("+")
    for area in areas:
        if area in allowed_areas():
            successful_parsed_areas.append(area)
    if len(successful_parsed_areas) == 0:
        raise ValueError

    return Animal(name=name, age=age, animal_class=Fish(area=successful_parsed_areas))


def create_beast_class(name, types, age):
    """
    This function parses data and creates Fish class
    :param age: str: beast age
    :param name: str: beast name
    :param types: str: beast type
    :return: Beast class
    """
    successful_parsed_types = []
    types = types.split("+")
    for beast_type in types:
        if beast_type in allowed_beast_types():
            successful_parsed_types.append(beast_type)
    if len(successful_parsed_types) == 0:
        raise ValueError

    return Animal(name=name, age=age, animal_class=Beast(beast_type=successful_parsed_types))


def clear(container: Container) -> None:
    """
    This function clears container
    :param container: container to clear
    :return: None
    """
    container.size = 0
    container.data.clear()


def write_file(container: Container, file_out: str) -> None:
    """
    This function prints container tmp
    :param container: container with tmp
    :param file_out: path to output file
    :return: None
    """
    with open(file_out, "w") as file:
        print(f"Animal count: {container.size}.", end=" ")
        file.write(f"Animal count: {container.size}. ")
        if container.size > 0:
            print("Animals:")
            file.write("Animals:\n")
        else:
            print()

        for i in range(container.size):
            animal = string_conversion(container.data[i])
            file.write(f"{i + 1}: {animal}\n")
            print(f"{i + 1}: {animal}")


def string_conversion(animal) -> str:
    """
    This function converses Animal object to string
    :param animal: Bird or Fish object to converse
    :return: conversed to string Animal object
    """
    if type(animal.animal_class) == Bird:
        return f"Type: bird.\t\tName: {animal.name}.\tAge: {animal.age}. \t" +\
               f"Is migratory: {animal.animal_class.migratory}."
    elif type(animal.animal_class) == Fish:
        return f"Type: fish.\t\tName: {animal.name}.\tAge: {animal.age}. \t" +\
               f"Area: {', '.join(animal.animal_class.area)}."
    elif type(animal.animal_class) == Beast:
        return f"Type: beast.\t\tName: {animal.name}.\tAge: {animal.age}. \t" +\
               f"Type: {', '.join(animal.animal_class.beast_type)}."


def read_file(container: Container, file_in: str) -> None:
    """
    This function reads input file and puts data to container
    :param container: container to save tmp
    :param file_in: path to the file
    :return: None
    """
    errors_count = 0
    try:
        with open(file_in) as file:
            lines = file.readlines()
            for line in lines:
                try:
                    animal = parse_line_and_create_animal_class(line)
                    add(container, animal)
                except ValueError:
                    errors_count += 1
                except BufferError:
                    print(f"! Warning: Container is full. Read only {container.max_size} lines.")
                    break
        # Sorting
        sort_by_name_length(container)

    except FileNotFoundError:
        print("Incorrect command line: No such input file.")
        sys.exit()

    print(f"Input file read with {errors_count} errors.")


def parse_line_and_create_animal_class(line):
    """
    This function parses data from line of file and returns animal class
    :param line: str: file line
    :return: animal object
    """
    line = line.replace("\n", "").split()
    if len(line) != 4:
        raise ValueError

    description = {
        "type": line[0].lower(),
        "name": line[1].lower(),
        "features": line[2].lower(),
        "age": int(line[3].lower())
    }
    # Parse data for Bird
    if description["type"] == "bird":
        animal = create_bird_class(description["name"], description["features"], description["age"])
    # Parse data for Fish
    elif description["type"] == "fish":
        animal = create_fish_class(description["name"], description["features"], description["age"])
    # Raise exception if given unknown type of animal
    elif description["type"] == "beast":
        animal = create_beast_class(description["name"], description["features"], description["age"])
    else:
        raise ValueError

    return animal


def print_name_length_of_each_animal(container):
    """
    This function prints length of name of each animal
    :param container: Container
    :return: None
    """
    for index, animal in enumerate(container.data):
        print(f"{index + 1}: name: {animal.name}, length: {len(animal.name)}")


def sort_by_name_length(container):
    """
    This function sorts animals by length of name
    :param container: Container
    :return: None
    """
    if container.size == 0:
        print("Empty container.")
        return

    print_name_length_of_each_animal(container)

    for _ in range(container.size):
        for i in range(container.size - 1):
            if len(container.data[i].name) < len(container.data[i + 1].name):
                container.data[i], container.data[i + 1] = container.data[i + 1], container.data[i]

    print("Container sorted by name length.\n")


def helping_info() -> None:
    """
    This function prints info for user
    :return: None
    """
    print("----------------------------------------------------------------------------------------------------")
    print("Example of command line:")
    print("app.py file_in.txt file_out.txt\n")
    print("You need to fill input file with tmp of animals.")
    print(f"Default max size of container: 128.\n")
    print("Example of input file:")
    print("bird Stork True")
    print("bird Eagle false")
    print("bird Macaw tRuE")
    print("fish Carp river+sea+pool")
    print("fish Shark ocean\n")
    print("You can write lines in any case.\n")
    print("Last parameter for the fish: is migratory: true or false.")
    print("Last parameter for the fish: area. Write it split '+', if fish lives in different areas.")
    print('Accepted area names: "canal", "lake", "ocean", "pool", "pond", "river", "sea", "spring".\n')
    print("If you write other area, it will not be included to the list.")
    print("If optional parameter of animal will be wrong or empty, line will not be included to the container.")
    print("----------------------------------------------------------------------------------------------------")
