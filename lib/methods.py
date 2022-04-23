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


def create_bird_class(name, migratory):
    """
    This function parses data and creates Bird class
    :param name: str: bird name
    :param migratory: str: is migratory
    :return: Bird class
    """
    if migratory == "true" or migratory == "false":
        migratory = True
    elif migratory == "false":
        migratory = False
    else:
        raise ValueError

    return Bird(name=name, migratory=migratory)


def create_fish_class(name, areas):
    """
    This function parses data and creates Fish class
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

    return Fish(name=name, area=successful_parsed_areas)


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
    if type(animal) == Bird:
        return f"Type: bird.\t\tName: {animal.name}.\t  Is migratory: {animal.migratory}."
    elif type(animal) == Fish:
        return f"Type: fish.\t\tName: {animal.name}.\t  Area: {', '.join(animal.area)}."


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
    if len(line) != 3:
        raise ValueError

    description = {
        "type": line[0].lower(),
        "name": line[1].lower(),
        "features": line[2].lower()
    }
    # Parse data for Bird
    if description["type"] == "bird":
        animal = create_bird_class(description["name"], description["features"])
    # Parse data for Fish
    elif description["type"] == "fish":
        animal = create_fish_class(description["name"], description["features"])
    # Raise exception if given unknown type of animal
    else:
        raise ValueError

    return animal


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
