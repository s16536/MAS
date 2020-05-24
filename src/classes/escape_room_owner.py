from datetime import date

from classes.user import User, Address
from object_plus.object_plus import ObjectPlus
from object_plus.roles import Role


class EscapeRoomOwner(User):
    def __init__(self, username: str, password: str, name: str, surname: str, date_of_birth: date, address: Address):
        super().__init__(username, password, name, surname, date_of_birth, address)

    @classmethod
    def get_role_constraints(cls):
        return {
            Role.OwnedEscapeRoom: float("inf")
        }

    @staticmethod
    def get_extent(class_name=None):
        return ObjectPlus.get_extent(EscapeRoomOwner)