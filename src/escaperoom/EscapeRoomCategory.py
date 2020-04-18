from enum import Enum, auto


class EscapeRoomCategory(Enum):
    HORROR = auto()
    ADVENTURE = auto()
    THRILLER = auto()
    MYSTERY = auto()

    def __str__(self):
        return self.name