from classes.user import User
from object_plus.object_plus import ObjectPlus
from object_plus.object_plus_plus import ObjectPlusPlus
from object_plus.roles import Role, RoleConstraint


class Address(object):
    def __init__(self, street: str, city: str, country: str):
        self._street = street
        self._city = city
        self._country = country

    def __str__(self):
        return ", ".join([self._street, self._city, self._country])


class EscapeRoomOwner(ObjectPlusPlus):
    def __init__(self, address: Address, user: User):
        if user is None:
            raise ValueError("Owner cannot exist without the User!")
        self._address = address
        super().__init__()
        user.add_part(Role.owner, Role.user, self)

    def get_user(self) -> User:
        return self.get_links(Role.user)[0]

    def __str__(self):
        return f"Escape Room Owner: {self.get_user().username}"

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.owned_escape_room: RoleConstraint(float("inf"), Role.owner),
            Role.user: RoleConstraint(1, Role.owner)
        }

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(EscapeRoomOwner)
