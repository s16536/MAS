from object_plus.object_plus_plus import ObjectPlusPlus
from object_plus.roles import Role, RoleConstraint


class Person(ObjectPlusPlus):
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name
        super().__init__()

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.player: RoleConstraint(1, Role.person, True),
            Role.owner: RoleConstraint(1, Role.person, True)
        }