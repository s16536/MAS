from enum import Enum, auto


class Role(Enum):
    player = auto()
    escape_room = auto()
    recommendation = auto()
    owner = auto()
    owned_escape_room = auto()
    visit = auto()
    group = auto()
    person = auto()
    user = auto()

    def __str__(self):
        return self.name


class RoleConstraint():
    def __init__(self, limit, reverse_role: Role, is_composition_owner: bool = False):
        self.limit = limit
        self.reverse_role_name = reverse_role
        self.is_composition_owner = is_composition_owner


def first_or_unknown(obj, role: Role):
    links = obj.get_links(role)

    if links is not None and len(links) > 0:
        return links[0]
    else:
        return f"Unknown {role}"
