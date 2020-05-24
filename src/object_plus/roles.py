from enum import Enum, auto


class Role(Enum):
    player = auto()
    escape_room = auto()
    recommendation = auto()
    owner = auto()
    owned_escape_room = auto()
    visit = auto()
    group = auto()

    def __str__(self):
        return self.name


class RoleConstraint():
    def __init__(self, limit, reverse_role: Role):
        self.limit = limit
        self.reverse_role_name = reverse_role
