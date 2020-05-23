from datetime import date

from classes.user import User, Address


class EscapeRoomOwner(User):
    def __init__(self, username: str, password: str, name: str, surname: str, date_of_birth: date, address: Address):
        super().__init__(username, password, name, surname, date_of_birth, address)

    @classmethod
    def get_role_constraints(cls):
        return {
            "ownedEscapeRoom": float("inf")
        }
