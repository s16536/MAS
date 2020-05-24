from enum import Enum, auto


class Role(Enum):
    Player = auto()
    EscapeRoom = auto()
    Recommendation = auto()
    Owner = auto()
    OwnedEscapeRoom = auto()
    Visit = auto()
    Group = auto()

    def __str__(self):
        return self.name
