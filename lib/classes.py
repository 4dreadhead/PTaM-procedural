from dataclasses import dataclass, field
from collections import deque


MAX_CONTAINER_SIZE = 128


@dataclass
class Bird:
    """
    This is class of the birds
    """
    migratory: bool


@dataclass
class Fish:
    """
    This is class of the fish
    """
    area: list


@dataclass
class Beast:
    """
    This is class of the beast
    """
    beast_type: list


@dataclass
class Animal:
    """
    This is general class for any animal
    """
    name: str
    age: int
    animal_class: dataclass


@dataclass
class Container:
    """
    This is container class
    """
    max_size = MAX_CONTAINER_SIZE
    data = deque(maxlen=max_size)
    size = 0
