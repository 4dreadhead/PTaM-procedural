from dataclasses import dataclass, field
from collections import deque


MAX_CONTAINER_SIZE = 128


@dataclass
class Bird:
    """
    This is class of the birds
    """
    name: str = "Not specified"
    migratory: bool = "Not specified"


@dataclass
class Fish:
    """
    This is class of the fish
    """
    name: str = "Not specified"
    area: list = field(default_factory=list)


@dataclass
class Beast:
    """
    This is class of the beast
    """
    name: str = "Not specified"
    beast_type: list = field(default_factory=list)


@dataclass
class Container:
    """
    This is container class
    """
    max_size = MAX_CONTAINER_SIZE
    data = deque(maxlen=max_size)
    size = 0
